from __future__ import annotations

import argparse
import csv
import os
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "00-books"
REPORT_ROOT = ROOT / "00-books-result"
OUTPUT_ROOT = ROOT / "outputs"
DETAIL_GLOB = "00-books-result*.csv"
MANIFEST = OUTPUT_ROOT / "00-books-result报告镜像重命名清单.csv"
SUMMARY = OUTPUT_ROOT / "00-books-result报告镜像重命名报告.md"
EXPECTED_SOURCES = 15369

REPORT_PATH_RE = re.compile(
    r"(?m)^(?P<prefix>-\s*\*\*报告文件路径\*\*[:：]\s*)`[^`]*`\s*$"
)
SOURCE_PATH_RE = re.compile(
    r"(?m)^(?P<line>-\s*\*\*(?:源文件完整路径|源文文件路径|源文路径)\*\*[:：].*)$"
)
DOCUMENT_ID_RE = re.compile(r"(?m)^#\s+((?:B|P)\d+)\b", re.I)


@dataclass(frozen=True)
class RenameItem:
    source: str
    old_report: str
    new_report: str
    temp_report: str


def extended(path: Path) -> str:
    resolved = str(path.resolve())
    if os.name == "nt" and not resolved.startswith("\\\\?\\"):
        return "\\\\?\\" + resolved
    return resolved


def path_exists(path: Path) -> bool:
    return os.path.exists(extended(path))


def read_text(path: Path) -> str:
    with open(extended(path), "r", encoding="utf-8-sig", errors="replace") as handle:
        return handle.read()


def write_text(path: Path, value: str) -> None:
    with open(extended(path), "w", encoding="utf-8", newline="") as handle:
        handle.write(value)


def move(old: Path, new: Path) -> None:
    os.makedirs(extended(new.parent), exist_ok=True)
    os.replace(extended(old), extended(new))


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def find_detail_csv() -> Path:
    for path in OUTPUT_ROOT.glob(DETAIL_GLOB):
        if path.stat().st_size < 4_000_000:
            continue
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            header = next(csv.reader(handle), [])
        if "severity" in header and "report" in header and "sources" in header:
            return path
    raise RuntimeError("未找到全量复审明细 CSV")


def load_items() -> tuple[list[RenameItem], int]:
    detail = find_detail_csv()
    with detail.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    mapped = [row for row in rows if row.get("sources")]
    orphan_count = len(rows) - len(mapped)
    if len(mapped) != EXPECTED_SOURCES:
        raise RuntimeError(f"有效映射应为 {EXPECTED_SOURCES}，实际为 {len(mapped)}")

    items: list[RenameItem] = []
    for index, row in enumerate(mapped, 1):
        sources = row["sources"].split(" | ")
        if len(sources) != 1:
            raise RuntimeError(f"报告不是一对一源文映射：{row['report']}")
        source = sources[0].replace("\\", "/")
        source_path = Path(source)
        if not source.startswith("00-books/") or source_path.suffix.lower() != ".md":
            raise RuntimeError(f"非法源文路径：{source}")
        new_report = (Path("00-books-result") / source_path.relative_to("00-books")).as_posix()
        temp_report = (
            Path("00-books-result") / ".codex-report-rename-temp" / f"{index:05d}.tmp"
        ).as_posix()
        items.append(RenameItem(source, row["report"], new_report, temp_report))
    return items, orphan_count


def validate(items: list[RenameItem]) -> None:
    source_inventory = {rel(path) for path in SOURCE_ROOT.rglob("*.md")}
    mapped_sources = {item.source for item in items}
    if source_inventory != mapped_sources:
        missing = sorted(source_inventory - mapped_sources)
        extra = sorted(mapped_sources - source_inventory)
        raise RuntimeError(f"映射与源文清单不一致：缺失 {len(missing)}，多出 {len(extra)}")

    old_paths = {item.old_report.lower() for item in items}
    new_paths = [item.new_report.lower() for item in items]
    if len(set(new_paths)) != len(new_paths):
        raise RuntimeError("目标报告路径存在重复")

    for item in items:
        if not path_exists(ROOT / item.source):
            raise RuntimeError(f"源文不存在：{item.source}")
        if not path_exists(ROOT / item.old_report):
            raise RuntimeError(f"原报告不存在：{item.old_report}")
        if path_exists(ROOT / item.temp_report):
            raise RuntimeError(f"临时路径已存在：{item.temp_report}")
        target = ROOT / item.new_report
        if item.new_report.lower() not in old_paths and path_exists(target):
            if os.path.isdir(extended(target)):
                children = list(os.scandir(extended(target)))
                child_rels = {
                    rel(Path(child.path.replace("\\\\?\\", ""))).lower()
                    for child in children
                }
                if any(child.is_dir() for child in children) or not child_rels <= old_paths:
                    raise RuntimeError(f"目标目录含非参与文件：{item.new_report}")
            else:
                raise RuntimeError(f"目标路径被非参与文件占用：{item.new_report}")


def update_report_path(text: str, new_report: str) -> tuple[str, bool]:
    replacement = lambda match: f"{match.group('prefix')}`{new_report}`"
    updated, count = REPORT_PATH_RE.subn(replacement, text, count=1)
    if count == 1:
        return updated, True
    updated, count = SOURCE_PATH_RE.subn(
        lambda match: f"{match.group('line')}\n- **报告文件路径**：`{new_report}`",
        text,
        count=1,
    )
    if count == 1:
        return updated, True
    heading = re.search(r"(?m)^#\s+.+$", text)
    if heading:
        position = heading.end()
        updated = text[:position] + f"\n\n- **报告文件路径**：`{new_report}`" + text[position:]
        return updated, True
    return f"- **报告文件路径**：`{new_report}`\n\n{text}", True


def repair_metadata() -> tuple[list[dict[str, str]], int]:
    with MANIFEST.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    repaired = 0
    missing = 0
    for row in rows:
        report_path = ROOT / row["new_report"]
        if not path_exists(report_path):
            missing += 1
            continue
        if row["metadata_updated"] != "yes":
            text = read_text(report_path)
            updated, success = update_report_path(text, row["new_report"])
            if success:
                write_text(report_path, updated)
                row["metadata_updated"] = "yes"
                repaired += 1
    if missing:
        raise RuntimeError(f"长路径复核发现目标报告缺失：{missing}")
    print(f"metadata_repaired={repaired} targets_verified={len(rows)}", flush=True)
    return rows, 491


def execute(items: list[RenameItem]) -> list[dict[str, str]]:
    staged: list[RenameItem] = []
    try:
        for item in items:
            if item.old_report.lower() == item.new_report.lower():
                continue
            move(ROOT / item.old_report, ROOT / item.temp_report)
            staged.append(item)
    except Exception:
        for item in reversed(staged):
            if path_exists(ROOT / item.temp_report):
                move(ROOT / item.temp_report, ROOT / item.old_report)
        raise

    blocking_directories = {
        item.new_report for item in items if os.path.isdir(extended(ROOT / item.new_report))
    }
    for directory in sorted(blocking_directories, key=len, reverse=True):
        os.rmdir(extended(ROOT / directory))

    rows: list[dict[str, str]] = []
    for index, item in enumerate(items, 1):
        source_path = ROOT / item.source
        current = ROOT / (item.temp_report if path_exists(ROOT / item.temp_report) else item.old_report)
        text = read_text(current)
        updated, metadata_updated = update_report_path(text, item.new_report)
        if updated != text:
            write_text(current, updated)
        document_id = ""
        match = DOCUMENT_ID_RE.search(updated)
        if match:
            document_id = match.group(1).upper()
        if current != ROOT / item.new_report:
            move(current, ROOT / item.new_report)
        rows.append(
            {
                "source": item.source,
                "old_report": item.old_report,
                "new_report": item.new_report,
                "document_id": document_id,
                "metadata_updated": "yes" if metadata_updated else "no_field",
            }
        )
        if index % 500 == 0:
            print(f"progress={index}/{len(items)}", flush=True)
    temp_root = REPORT_ROOT / ".codex-report-rename-temp"
    if os.path.isdir(extended(temp_root)):
        os.rmdir(extended(temp_root))
    return rows


def write_outputs(rows: list[dict[str, str]], orphan_count: int, dry_run: bool) -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    if not dry_run:
        with MANIFEST.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=["source", "old_report", "new_report", "document_id", "metadata_updated"],
            )
            writer.writeheader()
            writer.writerows(rows)
    changed = sum(row["old_report"].lower() != row["new_report"].lower() for row in rows)
    metadata = sum(row["metadata_updated"] == "yes" for row in rows)
    SUMMARY.write_text(
        "# 00-books-result 报告镜像重命名报告\n\n"
        f"- 执行模式：{'dry-run' if dry_run else 'write'}\n"
        f"- 有效源文与报告：{len(rows)}\n"
        f"- 实际需要重命名：{changed}\n"
        f"- 已同步报告路径字段：{metadata}\n"
        f"- 未参与的无源旧报告：{orphan_count}\n"
        "- 命名规则：`00-books/<相对路径>.md` 对应 `00-books-result/<相对路径>.md`\n"
        f"- 明细清单：`{rel(MANIFEST)}`\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="实际执行重命名")
    parser.add_argument("--repair-metadata", action="store_true", help="依据清单补齐报告路径字段")
    args = parser.parse_args()
    if args.repair_metadata:
        rows, orphan_count = repair_metadata()
        write_outputs(rows, orphan_count, False)
        return
    items, orphan_count = load_items()
    validate(items)
    if args.apply:
        rows = execute(items)
    else:
        rows = [
            {
                "source": item.source,
                "old_report": item.old_report,
                "new_report": item.new_report,
                "document_id": "",
                "metadata_updated": "not_checked",
            }
            for item in items
        ]
    write_outputs(rows, orphan_count, not args.apply)
    changed = sum(item.old_report.lower() != item.new_report.lower() for item in items)
    print(f"validated={len(items)} changed={changed} orphans_untouched={orphan_count} apply={args.apply}")


if __name__ == "__main__":
    main()
