from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path

from rewrite_00_books_reports import QueueItem, generate_report


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
LOG = OUT_DIR / "00-books-result修复GitBlob读取错误日志.csv"
SUMMARY = OUT_DIR / "00-books-result修复GitBlob读取错误报告.md"

BAD_MARKERS = [
    "源文正文暂未读取",
    "Git blob 读取错误",
    "blob 读取错误",
]

SOURCE_PATTERNS = [
    re.compile(r"`(00-books[\\/][^`]+?\.md)`"),
    re.compile(r"HEAD:(00-books[\\/].+?\.md)"),
    re.compile(r"(00-books[\\/][^\n\r`]+?\.md)"),
]


def long_path(path: Path) -> Path:
    return Path("\\\\?\\" + str(path.resolve()))


def read_text_path(path: Path) -> str:
    for candidate in (path, long_path(path)):
        try:
            return candidate.read_text(encoding="utf-8-sig", errors="replace")
        except OSError:
            continue
    return ""


def write_text_path(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    for candidate in (path, long_path(path)):
        try:
            candidate.write_text(text, encoding="utf-8")
            return
        except OSError:
            continue
    raise OSError(f"Cannot write {path}")


def normalize_source(src: str) -> str:
    src = src.strip().strip("。；;，, )）]'\"")
    src = src.replace("\\", "/")
    # Trim Python exception tail if a quoted path was captured too generously.
    marker = ".md"
    if marker in src:
        src = src[: src.find(marker) + len(marker)]
    return src


def extract_source(text: str) -> str:
    for pattern in SOURCE_PATTERNS:
        for match in pattern.findall(text):
            src = normalize_source(match)
            if src.startswith("00-books/") and src.endswith(".md"):
                return src
    return ""


def iter_bad_reports() -> list[Path]:
    reports = []
    for path in (ROOT / "00-books-result").rglob("*report.md"):
        text = read_text_path(path)
        if any(marker in text for marker in BAD_MARKERS):
            reports.append(path)
    return reports


def make_item(report_rel: str, source_rel: str, source_text: str, report_text: str) -> QueueItem:
    return QueueItem(
        priority="REPAIR",
        rewrite_type="修复 Git blob 读取错误报告",
        report=report_rel,
        source=source_rel,
        source_chars=str(len(source_text)),
        report_chars=str(len(report_text)),
        original_action="repair_git_blob_error",
        instruction="旧报告未读取源文正文；必须从本地 00-books/ 源 Markdown 重新读取并覆盖写入。",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    OUT_DIR.mkdir(exist_ok=True)
    bad_reports = iter_bad_reports()
    if args.limit:
        bad_reports = bad_reports[: args.limit]

    rows: list[dict[str, str]] = []
    for report_path in bad_reports:
        report_text = read_text_path(report_path)
        report_rel = report_path.relative_to(ROOT).as_posix()
        source_rel = extract_source(report_text)
        status = "pending"
        chars = "0"

        if not source_rel:
            status = "missing_source_path"
        else:
            source_path = ROOT / source_rel
            source_text = read_text_path(source_path)
            if not source_path.exists() and not long_path(source_path).exists():
                status = "source_path_not_found"
            else:
                status = "rewritten" if source_text.strip() else "rewritten_empty_source_boundary"
                if args.dry_run:
                    status = "would_rewrite" if source_text.strip() else "would_rewrite_empty_source_boundary"
                chars = str(len(source_text))
                if not args.dry_run:
                    item = make_item(report_rel, source_rel, source_text, report_text)
                    new_report = generate_report(item, source_path, report_path, source_text)
                    write_text_path(report_path, new_report)

        rows.append(
            {
                "status": status,
                "report": report_rel,
                "source": source_rel,
                "source_chars": chars,
            }
        )

    with LOG.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["status", "report", "source", "source_chars"])
        writer.writeheader()
        writer.writerows(rows)

    counts = Counter(row["status"] for row in rows)
    remaining = 0
    if not args.dry_run:
        remaining = len(iter_bad_reports())

    lines = []
    lines.append("# 00-books-result Git blob 读取错误修复报告\n\n")
    lines.append(f"- 执行模式：{'dry-run' if args.dry_run else 'write'}\n")
    lines.append(f"- 扫描到待修复报告：{len(rows)}\n")
    for status, count in counts.most_common():
        lines.append(f"- `{status}`：{count}\n")
    if not args.dry_run:
        lines.append(f"- 修复后仍含错误标记的报告：{remaining}\n")
    lines.append(f"- 明细日志：`{LOG.relative_to(ROOT).as_posix()}`\n\n")
    lines.append("## 样本\n\n")
    for row in rows[:120]:
        lines.append(f"- **{row['status']}** `{row['report']}`\n")
        if row["source"]:
            lines.append(f"  - 源文：`{row['source']}`；源文字数：{row['source_chars']}\n")
    SUMMARY.write_text("".join(lines), encoding="utf-8")

    print(f"dry_run={args.dry_run}")
    print(f"reports={len(rows)}")
    for status, count in counts.most_common():
        print(f"{status}={count}")
    if not args.dry_run:
        print(f"remaining_bad_markers={remaining}")
    print(LOG.relative_to(ROOT).as_posix())
    print(SUMMARY.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
