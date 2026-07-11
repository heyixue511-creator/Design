from __future__ import annotations

import csv
import argparse
import re
from collections import Counter
from pathlib import Path

from repair_bilingual_knowledge_tables import path_exists, read_text_path, write_text_path
from rewrite_00_books_reports import QueueItem, ROOT, generate_report


OUTPUTS = ROOT / "outputs"
DETAIL = OUTPUTS / "00-books-result全量复审明细.csv"
MAPPING = OUTPUTS / "00-books-result源文映射重建日志.csv"
LOG = OUTPUTS / "00-books-result全量语义重写日志.csv"
SUMMARY = OUTPUTS / "00-books-result全量语义重写报告.md"
REPORT_ROOT = ROOT / "00-books-result"


def make_item(priority: str, report: str, source: str, source_chars: str = "") -> QueueItem:
    return QueueItem(
        priority=priority,
        rewrite_type="semantic_v2_full",
        report=report,
        source=source,
        source_chars=source_chars,
        report_chars="",
        original_action="full_audit_queue",
        instruction="重新读取源文，按文献类型生成 V2.0 语义报告",
    )


def safe_name(source: str, index: int) -> str:
    stem = Path(source).stem
    stem = re.sub(r"[^0-9A-Za-z\u3400-\u9fff._-]+", "-", stem).strip("-._")
    stem = stem[:72] or "source"
    return f"B9{index:07d}-{stem}-report.md"


def new_report_path(source: str, index: int) -> str:
    source_path = Path(source)
    candidate = Path("00-books-result") / source_path.relative_to("00-books")
    if path_exists(ROOT / candidate):
        raise RuntimeError(f"源文镜像报告路径已被占用：{candidate.as_posix()}")
    return candidate.as_posix()


def existing_generated_report(source: str) -> str:
    source_path = Path(source)
    directory = REPORT_ROOT / source_path.relative_to("00-books").parent
    if not path_exists(directory):
        return ""
    marker = f"`{source}`"
    for report in directory.glob("*.md"):
        if marker in read_text_path(report)[:2400]:
            return report.relative_to(ROOT).as_posix()
    return ""


def load_items() -> tuple[list[QueueItem], int]:
    detail_rows = list(csv.DictReader(DETAIL.open(encoding="utf-8-sig")))
    items: dict[str, QueueItem] = {}
    unmapped = 0
    for row in detail_rows:
        if row["severity"] == "P3":
            continue
        source = row["sources"].split(" | ")[0] if row["sources"] else ""
        if not source:
            unmapped += 1
            continue
        items[row["report"]] = make_item(row["severity"], row["report"], source, row["source_chars"])

    mapping_rows = list(csv.DictReader(MAPPING.open(encoding="utf-8-sig")))
    new_index = 1
    for row in mapping_rows:
        if row["status"] == "mapped":
            items[row["report"]] = make_item("P1", row["report"], row["source"])
        elif row["status"] in {"needs_new_report", "unmatched_source"}:
            report = existing_generated_report(row["source"]) or new_report_path(row["source"], new_index)
            new_index += 1
            items[report] = make_item("P0", report, row["source"])
    return sorted(items.values(), key=lambda item: (item.priority, item.report)), unmapped


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    items, unmapped = load_items()
    if args.limit:
        items = items[: args.limit]
    rows: list[dict[str, str]] = []
    for number, item in enumerate(items, 1):
        report_path = ROOT / item.report
        source_path = ROOT / item.source
        old_report = read_text_path(report_path) if path_exists(report_path) else ""
        if "模型语义复审" in old_report:
            rows.append({"status": "skipped_manual_p3", "report": item.report, "source": item.source, "chars": str(len(old_report))})
            continue
        if not path_exists(source_path):
            rows.append({"status": "missing_source", "report": item.report, "source": item.source, "chars": "0"})
            continue
        source_text = read_text_path(source_path)
        if not source_text.strip():
            rows.append({"status": "empty_source", "report": item.report, "source": item.source, "chars": "0"})
            continue
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report = generate_report(item, source_path, report_path, source_text)
        if not args.dry_run:
            write_text_path(report_path, report)
        action = "rewritten" if old_report else "created"
        rows.append({"status": f"would_{action}" if args.dry_run else action, "report": item.report, "source": item.source, "chars": str(len(report))})
        if number % 500 == 0:
            print(f"progress={number}/{len(items)}")

    with LOG.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["status", "report", "source", "chars"])
        writer.writeheader()
        writer.writerows(rows)

    counts = Counter(row["status"] for row in rows)
    SUMMARY.write_text(
        "# 00-books-result 全量语义重写报告\n\n"
        "- 依据：全量复审明细、源文映射重建日志与 V2.0 规则\n"
        f"- 纳入处理：{len(items)}\n"
        f"- 已重写：{counts['rewritten']}\n"
        f"- 已新建：{counts['created']}\n"
        f"- 预计重写：{counts['would_rewritten']}\n"
        f"- 预计新建：{counts['would_created']}\n"
        f"- 跳过人工 P3：{counts['skipped_manual_p3']}\n"
        f"- 源文为空：{counts['empty_source']}\n"
        f"- 源文缺失：{counts['missing_source']}\n"
        f"- 无可靠源文映射旧报告：{unmapped}\n\n"
        "无可靠源文映射的旧报告未强行改写；它们保留在映射异常处置清单中。\n",
        encoding="utf-8",
    )
    print(f"items={len(items)} counts={dict(counts)} unmapped={unmapped}")


if __name__ == "__main__":
    main()
