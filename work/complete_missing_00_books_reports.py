from __future__ import annotations

import argparse
import csv
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

from rewrite_00_books_reports import QueueItem, generate_report


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
LOG = OUT_DIR / "00-books-result补全缺失报告日志.csv"
SUMMARY = OUT_DIR / "00-books-result补全缺失报告报告.md"
RULE_REPORT = "00-books-result/00-books Markdown 深度报告生成与复审规则.md"


SOURCE_RE = re.compile(r"`?(00-books[\\/][^\n\r`]+?\.md)`?")


def git_files() -> list[str]:
    proc = subprocess.run(
        ["git", "-c", "core.quotePath=false", "ls-files", "-z"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        check=True,
    )
    return [item.replace("\\", "/") for item in proc.stdout.decode("utf-8", errors="replace").split("\0") if item]


def filesystem_files() -> list[str]:
    paths: list[str] = []
    for base in [ROOT / "00-books", ROOT / "00-books-result"]:
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            try:
                paths.append(path.relative_to(ROOT).as_posix())
            except ValueError:
                continue
    return paths


def long_path(path: Path) -> Path:
    return Path("\\\\?\\" + str(path.resolve()))


def read_text(rel_path: str) -> str:
    path = ROOT / rel_path
    for candidate in (path, long_path(path)):
        try:
            return candidate.read_text(encoding="utf-8-sig", errors="replace")
        except OSError:
            continue
    return ""


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    for candidate in (path, long_path(path)):
        try:
            candidate.write_text(text, encoding="utf-8")
            return
        except OSError:
            continue
    raise OSError(f"Cannot write {path}")


def extract_sources(text: str) -> list[str]:
    found: list[str] = []
    for match in SOURCE_RE.findall(text):
        src = match.strip().strip("。；;，, )）").replace("\\", "/")
        if src.startswith("00-books/") and src not in found:
            found.append(src)
    return found


def book_dir(path: str, root: str) -> str:
    parts = path.replace("\\", "/").split("/")
    return parts[1] if len(parts) >= 2 and parts[0] == root else ""


def tokenize_name(path: str) -> set[str]:
    stem = Path(path).stem.lower()
    stem = re.sub(r"\bB\d{3,8}\b", " ", stem)
    stem = re.sub(r"\breport\b|\babout\b|\bface\b", " ", stem)
    tokens = re.split(r"[^a-z0-9\u4e00-\u9fff]+", stem)
    stop = {"the", "and", "for", "with", "from", "part", "page", "image", "tif", "jpg", "pdf"}
    return {token for token in tokens if len(token) >= 2 and token not in stop}


def similarity(report: str, source: str) -> float:
    rt = tokenize_name(report)
    st = tokenize_name(source)
    if not rt or not st:
        return 0.0
    return len(rt & st) / len(rt | st)


def source_sort_key(path: str) -> tuple[int, str]:
    name = Path(path).name
    match = re.match(r"(\d+)", name)
    return (int(match.group(1)) if match else 10**9, name.lower())


def report_sort_key(path: str) -> tuple[int, str]:
    name = Path(path).name
    match = re.search(r"\bB(\d{3,8})\b", name)
    return (int(match.group(1)) if match else 10**9, name.lower())


def slugify_source(source: str) -> str:
    stem = Path(source).stem
    stem = re.sub(r"^\d+[-_\s]*", "", stem)
    parts = re.findall(r"[A-Za-z0-9\u4e00-\u9fff]+", stem)
    slug = "-".join(parts)[:80].strip("-")
    return slug or "source"


def next_b_number(report_paths: list[str]) -> int:
    nums = []
    for path in report_paths:
        match = re.search(r"\bB(\d{3,8})\b", Path(path).name)
        if match:
            nums.append(int(match.group(1)))
    return max(nums, default=0) + 1


def make_item(report: str, source: str, kind: str) -> QueueItem:
    src_text = read_text(source)
    return QueueItem(
        priority="FILL",
        rewrite_type=kind,
        report=report,
        source=source,
        source_chars=str(len(src_text)),
        report_chars=str(len(read_text(report))),
        original_action="complete_missing_report",
        instruction="补全 00-books 与 00-books-result 的一一覆盖关系；必须先读源文，再按 V2.0 生成报告。",
    )


def infer_existing_matches(
    source_paths: list[str],
    report_paths: list[str],
    covered_sources: set[str],
    report_sources: dict[str, list[str]],
) -> list[dict[str, str]]:
    sources_by_book: dict[str, list[str]] = defaultdict(list)
    reports_by_book: dict[str, list[str]] = defaultdict(list)
    for source in source_paths:
        if source not in covered_sources:
            sources_by_book[book_dir(source, "00-books")].append(source)
    for report in report_paths:
        if not report_sources.get(report):
            reports_by_book[book_dir(report, "00-books-result")].append(report)

    assignments: list[dict[str, str]] = []
    assigned_sources: set[str] = set()
    assigned_reports: set[str] = set()

    for book, reports in reports_by_book.items():
        sources = [src for src in sources_by_book.get(book, []) if src not in assigned_sources]
        if not sources:
            continue
        reports = sorted(reports, key=report_sort_key)
        sources = sorted(sources, key=source_sort_key)

        # If the counts line up, the repository's B-number order usually mirrors source order.
        if len(reports) == len(sources):
            for report, source in zip(reports, sources):
                assignments.append(
                    {
                        "action": "rewrite_existing_unmapped_report",
                        "report": report,
                        "source": source,
                        "match_method": "same_book_order",
                        "score": f"{similarity(report, source):.3f}",
                    }
                )
                assigned_reports.add(report)
                assigned_sources.add(source)
            continue

        for report in reports:
            if report in assigned_reports:
                continue
            candidates = [src for src in sources if src not in assigned_sources]
            if not candidates:
                break
            best = max(candidates, key=lambda src: similarity(report, src))
            score = similarity(report, best)
            if score >= 0.22:
                assignments.append(
                    {
                        "action": "rewrite_existing_unmapped_report",
                        "report": report,
                        "source": best,
                        "match_method": "same_book_name_similarity",
                        "score": f"{score:.3f}",
                    }
                )
                assigned_reports.add(report)
                assigned_sources.add(best)

    return assignments


def build_plan() -> tuple[list[dict[str, str]], list[str], list[str]]:
    files = sorted(set(git_files()) | set(filesystem_files()))
    source_paths = [p for p in files if p.startswith("00-books/") and p.endswith(".md")]
    report_paths = [
        p for p in files
        if p.startswith("00-books-result/") and p.endswith(".md") and p != RULE_REPORT
    ]
    source_set = set(source_paths)

    report_sources: dict[str, list[str]] = {}
    covered_sources: set[str] = set()
    for report in report_paths:
        sources = [src for src in extract_sources(read_text(report)) if src in source_set]
        report_sources[report] = sources
        covered_sources.update(sources)

    plan = infer_existing_matches(source_paths, report_paths, covered_sources, report_sources)
    assigned_sources = {row["source"] for row in plan}
    covered_after_existing = covered_sources | assigned_sources

    created_paths: set[str] = set(report_paths)
    for source in sorted(source_set - covered_after_existing):
        report = (Path("00-books-result") / Path(source).relative_to("00-books")).as_posix()
        if report in created_paths:
            raise RuntimeError(f"源文镜像报告路径已被占用：{report}")
        created_paths.add(report)
        plan.append(
            {
                "action": "create_missing_report",
                "report": report,
                "source": source,
                "match_method": "new_report_for_uncovered_source",
                "score": "",
            }
        )

    return plan, source_paths, report_paths


def coverage_after_write() -> tuple[int, int, int, int]:
    files = sorted(set(git_files()) | set(filesystem_files()))
    source_paths = [p for p in files if p.startswith("00-books/") and p.endswith(".md")]
    report_paths = [
        p for p in files
        if p.startswith("00-books-result/") and p.endswith(".md") and p != RULE_REPORT
    ]
    source_set = set(source_paths)
    covered: set[str] = set()
    for report in report_paths:
        for src in extract_sources(read_text(report)):
            if src in source_set:
                covered.add(src)
    return len(source_paths), len(report_paths), len(covered), len(source_set - covered)


def write_summary(plan: list[dict[str, str]], source_count: int, report_count: int, dry_run: bool) -> None:
    counts = Counter(row["action"] for row in plan)
    fs_sources, fs_reports, fs_covered, fs_missing = coverage_after_write()
    lines = []
    lines.append("# 00-books-result 缺失深度报告补全\n\n")
    lines.append(f"- 执行模式：{'dry-run' if dry_run else 'write'}\n")
    lines.append(f"- `00-books/` 源 Markdown：{source_count}\n")
    lines.append(f"- 原有 `00-books-result/` 报告：{report_count}\n")
    lines.append(f"- 计划处理：{len(plan)}\n")
    for action, count in counts.most_common():
        lines.append(f"- `{action}`：{count}\n")
    lines.append("\n## 覆盖率复核\n\n")
    lines.append(f"- 本地源 Markdown：{fs_sources}\n")
    lines.append(f"- 本地结果报告：{fs_reports}\n")
    lines.append(f"- 已由报告源路径覆盖的源 Markdown：{fs_covered}\n")
    lines.append(f"- 仍缺失报告的源 Markdown：{fs_missing}\n")
    lines.append(f"- 明细日志：`{LOG.relative_to(ROOT).as_posix()}`\n\n")
    lines.append("## 样本\n\n")
    for row in plan[:120]:
        lines.append(f"- **{row['action']}** `{row['report']}`\n")
        lines.append(f"  - 源文：`{row['source']}`\n")
        lines.append(f"  - 匹配：{row['match_method']} {row['score']}\n")
    SUMMARY.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    OUT_DIR.mkdir(exist_ok=True)
    plan, source_paths, report_paths = build_plan()

    if not args.dry_run:
        for row in plan:
            item = make_item(
                row["report"],
                row["source"],
                "补全缺失报告" if row["action"] == "create_missing_report" else "重写未映射既有报告",
            )
            source_path = ROOT / row["source"]
            report_path = ROOT / row["report"]
            source_text = read_text(row["source"])
            report_text = generate_report(item, source_path, report_path, source_text)
            write_text(report_path, report_text)

    with LOG.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["action", "report", "source", "match_method", "score"])
        writer.writeheader()
        writer.writerows(plan)

    write_summary(plan, len(source_paths), len(report_paths), args.dry_run)

    counts = Counter(row["action"] for row in plan)
    print(f"dry_run={args.dry_run}")
    print(f"sources={len(source_paths)} reports={len(report_paths)} planned={len(plan)}")
    for action, count in counts.most_common():
        print(f"{action}={count}")
    print(LOG.relative_to(ROOT).as_posix())
    print(SUMMARY.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
