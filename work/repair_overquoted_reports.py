from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path

from repair_git_blob_error_reports import extract_source, long_path, read_text_path, write_text_path
from rewrite_00_books_reports import QueueItem, generate_report


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
LOG = OUT_DIR / "00-books-result修复长篇原文搬运日志.csv"
SUMMARY = OUT_DIR / "00-books-result修复长篇原文搬运报告.md"


def is_problem_report(text: str) -> tuple[bool, int, int]:
    lines = text.splitlines()
    max_line = max((len(line) for line in lines), default=0)
    h1_len = len(lines[0]) if lines else 0
    return max_line > 650 or h1_len > 180, h1_len, max_line


def iter_problem_reports() -> list[tuple[Path, int, int]]:
    found: list[tuple[Path, int, int]] = []
    for path in (ROOT / "00-books-result").rglob("*report.md"):
        text = read_text_path(path)
        bad, h1_len, max_line = is_problem_report(text)
        if bad:
            found.append((path, h1_len, max_line))
    return found


def make_item(report_rel: str, source_rel: str, source_text: str, report_text: str) -> QueueItem:
    return QueueItem(
        priority="COMPACT",
        rewrite_type="修复长篇原文搬运报告",
        report=report_rel,
        source=source_rel,
        source_chars=str(len(source_text)),
        report_chars=str(len(report_text)),
        original_action="repair_overquoted_source",
        instruction="旧报告包含超长标题或大段源文搬运；必须压缩为分析型 V2.0 深度报告。",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    OUT_DIR.mkdir(exist_ok=True)
    reports = iter_problem_reports()
    if args.limit:
        reports = reports[: args.limit]

    rows: list[dict[str, str]] = []
    for report_path, old_h1, old_max_line in reports:
        report_text = read_text_path(report_path)
        report_rel = report_path.relative_to(ROOT).as_posix()
        source_rel = extract_source(report_text)
        status = "pending"
        new_h1 = ""
        new_max_line = ""
        new_chars = ""

        if not source_rel:
            status = "missing_source_path"
        else:
            source_path = ROOT / source_rel
            source_text = read_text_path(source_path)
            if not source_path.exists() and not long_path(source_path).exists():
                status = "source_path_not_found"
            else:
                status = "would_rewrite" if args.dry_run else "rewritten"
                if not args.dry_run:
                    item = make_item(report_rel, source_rel, source_text, report_text)
                    new_report = generate_report(item, source_path, report_path, source_text)
                    write_text_path(report_path, new_report)
                    lines = new_report.splitlines()
                    new_h1 = str(len(lines[0]) if lines else 0)
                    new_max_line = str(max((len(line) for line in lines), default=0))
                    new_chars = str(len(new_report))

        rows.append(
            {
                "status": status,
                "report": report_rel,
                "source": source_rel,
                "old_h1_len": str(old_h1),
                "old_max_line_len": str(old_max_line),
                "new_h1_len": new_h1,
                "new_max_line_len": new_max_line,
                "new_chars": new_chars,
            }
        )

    with LOG.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "status",
                "report",
                "source",
                "old_h1_len",
                "old_max_line_len",
                "new_h1_len",
                "new_max_line_len",
                "new_chars",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    counts = Counter(row["status"] for row in rows)
    remaining = 0 if args.dry_run else len(iter_problem_reports())

    lines = []
    lines.append("# 00-books-result 长篇原文搬运修复报告\n\n")
    lines.append(f"- 执行模式：{'dry-run' if args.dry_run else 'write'}\n")
    lines.append(f"- 扫描到超长行/超长标题报告：{len(rows)}\n")
    for status, count in counts.most_common():
        lines.append(f"- `{status}`：{count}\n")
    if not args.dry_run:
        lines.append(f"- 修复后仍存在超长行/超长标题报告：{remaining}\n")
    lines.append(f"- 明细日志：`{LOG.relative_to(ROOT).as_posix()}`\n\n")
    lines.append("## 样本\n\n")
    for row in rows[:120]:
        lines.append(f"- **{row['status']}** `{row['report']}`\n")
        lines.append(f"  - 源文：`{row['source']}`\n")
        lines.append(f"  - 修复前 H1/最长行：{row['old_h1_len']} / {row['old_max_line_len']}\n")
        if row["new_h1_len"]:
            lines.append(f"  - 修复后 H1/最长行：{row['new_h1_len']} / {row['new_max_line_len']}\n")
    SUMMARY.write_text("".join(lines), encoding="utf-8")

    print(f"dry_run={args.dry_run}")
    print(f"reports={len(rows)}")
    for status, count in counts.most_common():
        print(f"{status}={count}")
    if not args.dry_run:
        print(f"remaining_overquoted={remaining}")
    print(LOG.relative_to(ROOT).as_posix())
    print(SUMMARY.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
