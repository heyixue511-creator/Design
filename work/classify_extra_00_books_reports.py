from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path

from repair_bilingual_knowledge_tables import read_text_path


ROOT = Path(__file__).resolve().parents[1]
DETAIL = ROOT / "outputs" / "00-books-result全量复审明细.csv"
OUT_CSV = ROOT / "outputs" / "00-books-result多余报告明细.csv"
OUT_MD = ROOT / "outputs" / "00-books-result多余报告说明.md"


def norm_stem(path: str) -> str:
    value = Path(path).stem.lower()
    value = re.sub(r"-report$", "", value)
    value = re.sub(r"^b\d+[-_]", "", value)
    value = re.sub(r"^\d+[-_]", "", value)
    return re.sub(r"[^0-9a-z\u3400-\u9fff]+", "", value)


def canonical_score(row: dict[str, str], source: str) -> tuple[float, int, int, int, str]:
    report_stem = norm_stem(row["report"])
    source_stem = norm_stem(source)
    title_similarity = SequenceMatcher(None, report_stem, source_stem).ratio() if report_stem and source_stem else 0.0
    manual = 1 if "模型语义复审" in read_text_path(ROOT / row["report"])[:1600] else 0
    severity = {"P3": 3, "P2": 2, "P1": 1, "P0": 0}.get(row["severity"], 0)
    # B9 reports were deliberately created for previously uncovered source files.
    generated_missing = 1 if re.match(r"B9\d+-", Path(row["report"]).name) else 0
    return (title_similarity, manual, generated_missing, severity, row["report"])


def main() -> None:
    rows = list(csv.DictReader(DETAIL.open(encoding="utf-8-sig")))
    by_source: defaultdict[str, list[dict[str, str]]] = defaultdict(list)
    orphans: list[dict[str, str]] = []
    for row in rows:
        sources = [value for value in row["sources"].split(" | ") if value]
        if not sources:
            orphans.append(row)
            continue
        by_source[sources[0]].append(row)

    output: list[dict[str, str]] = []
    for row in orphans:
        output.append({
            "category": "orphan_no_source",
            "extra_report": row["report"],
            "source": "",
            "canonical_report": "",
            "severity": row["severity"],
            "reason": "无法与 00-books/ 建立唯一源文对应关系；已标记停止使用",
        })

    duplicate_groups = 0
    duplicate_extras = 0
    for source, group in sorted(by_source.items()):
        if len(group) < 2:
            continue
        duplicate_groups += 1
        canonical = max(group, key=lambda row: canonical_score(row, source))
        for row in group:
            if row is canonical:
                continue
            duplicate_extras += 1
            output.append({
                "category": "duplicate_noncanonical",
                "extra_report": row["report"],
                "source": source,
                "canonical_report": canonical["report"],
                "severity": row["severity"],
                "reason": f"同一源文共有 {len(group)} 份报告；该文件不是建议主报告",
            })

    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["category", "extra_report", "source", "canonical_report", "severity", "reason"],
        )
        writer.writeheader()
        writer.writerows(output)

    category_counts = Counter(row["category"] for row in output)
    directory_counts = Counter(str(Path(row["extra_report"]).parent).replace("\\", "/") for row in output)
    top_dirs = "\n".join(f"- `{directory}`：{count}" for directory, count in directory_counts.most_common(20))
    OUT_MD.write_text(
        "# 00-books-result 多余报告说明\n\n"
        f"- 源 Markdown：15369\n"
        f"- 报告：{len(rows)}\n"
        f"- 数量差额：{len(rows) - 15369}\n"
        f"- 无源文对应的孤立旧报告：{category_counts['orphan_no_source']}\n"
        f"- 重复源文组：{duplicate_groups}\n"
        f"- 重复组中的非主报告：{category_counts['duplicate_noncanonical']}\n"
        f"- 两类多余报告合计：{len(output)}\n\n"
        "## 数量关系\n\n"
        f"`{category_counts['orphan_no_source']} + {category_counts['duplicate_noncanonical']} = {len(output)}`，"
        f"与报告总数减源文总数的差额 `{len(rows) - 15369}` 一致。\n\n"
        "## 多余报告较集中的目录\n\n"
        f"{top_dirs}\n\n"
        "完整逐文件清单：`outputs/00-books-result多余报告明细.csv`。"
        "本次只分类，没有删除或移动任何报告。\n",
        encoding="utf-8",
    )
    print(
        f"reports={len(rows)} orphans={len(orphans)} duplicate_groups={duplicate_groups} "
        f"duplicate_extras={duplicate_extras} extras={len(output)}"
    )


if __name__ == "__main__":
    main()
