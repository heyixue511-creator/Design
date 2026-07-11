from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
INPUT = OUT_DIR / "00-books-result-P0首批复审明细.csv"


REWRITE_ACTIONS = {
    "needs_v2_rewrite",
    "low_info_needs_boundary_rewrite",
}


def load_rows() -> list[dict[str, str]]:
    with INPUT.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def priority(row: dict[str, str]) -> tuple[str, str, str]:
    action = row["action"]
    source_chars = int(row.get("source_chars") or 0)
    report_chars = int(row.get("report_chars") or 0)

    if action == "low_info_needs_boundary_rewrite":
        return (
            "R3",
            "低信息量降级重写",
            "按 V2.0 写成 C/D 类辅助报告，补源文核验、证据边界、不可确认内容，不扩写理论。",
        )

    if source_chars >= 20000 and report_chars < 500:
        return (
            "R1",
            "大体量源文完整重写",
            "必须重新阅读全文或分段抽读，补齐源文核验、文献性质、语义分析、知识要素、证据边界和复审结论。",
        )

    if source_chars >= 5000:
        return (
            "R2",
            "中体量源文 V2 重写",
            "需重新读取源文主要段落，生成完整 V2 复审报告；不得沿用旧短报告。",
        )

    return (
        "R3",
        "短源文结构化重写",
        "按源文实际信息量重写，若只是题名/目录/书目材料则降级处理。",
    )


def main() -> None:
    rows = load_rows()
    queue = []
    for row in rows:
        if row["action"] not in REWRITE_ACTIONS:
            continue
        p, kind, instruction = priority(row)
        queue.append(
            {
                "priority": p,
                "rewrite_type": kind,
                "report": row["report"],
                "source": row["suggested_source"],
                "source_chars": row["source_chars"],
                "report_chars": row["report_chars"],
                "original_action": row["action"],
                "entity_overlap": row["entity_overlap"],
                "instruction": instruction,
            }
        )

    queue.sort(key=lambda r: (r["priority"], -int(r["source_chars"] or 0), r["report"]))

    csv_path = OUT_DIR / "00-books-result重写队列.csv"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "priority",
                "rewrite_type",
                "report",
                "source",
                "source_chars",
                "report_chars",
                "original_action",
                "entity_overlap",
                "instruction",
            ],
        )
        writer.writeheader()
        writer.writerows(queue)

    counts = Counter(row["priority"] for row in queue)
    type_counts = Counter(row["rewrite_type"] for row in queue)

    md_path = OUT_DIR / "00-books-result重写队列.md"
    lines: list[str] = []
    lines.append("# 00-books-result 重写队列\n\n")
    lines.append("来源：`outputs/00-books-result-P0首批复审明细.csv`\n\n")
    lines.append("本队列收纳首批复审中判定为 `needs_v2_rewrite` 与 `low_info_needs_boundary_rewrite` 的报告。它们不得仅通过补源路径恢复为可靠完成量，必须按 V2.0 规则重写或降级重写。\n\n")
    lines.append("## 一、队列统计\n\n")
    lines.append(f"- 入队报告：{len(queue)}\n")
    for key in ["R1", "R2", "R3"]:
        lines.append(f"- `{key}`：{counts.get(key, 0)}\n")
    lines.append("\n")
    lines.append("## 二、重写类型\n\n")
    for kind, count in type_counts.most_common():
        lines.append(f"- {kind}：{count}\n")
    lines.append("\n")
    lines.append("## 三、优先级说明\n\n")
    lines.append("- `R1`：大体量源文但旧报告极短，优先重写，污染完成量风险最高。\n")
    lines.append("- `R2`：中体量源文，需补齐 V2.0 结构和证据边界。\n")
    lines.append("- `R3`：短源文或低信息量源文，重点是降级、合读、证据边界，不扩写理论。\n\n")
    lines.append("## 四、队列明细\n\n")
    for item in queue:
        lines.append(f"- **{item['priority']} / {item['rewrite_type']}** `{item['report']}`\n")
        lines.append(f"  - 源文：`{item['source']}`\n")
        lines.append(f"  - 源文/旧报告字符：{item['source_chars']} / {item['report_chars']}\n")
        lines.append(f"  - 重写要求：{item['instruction']}\n")
    lines.append(f"\n完整表格见 `{csv_path.name}`。\n")
    md_path.write_text("".join(lines), encoding="utf-8")

    print(f"queued={len(queue)}")
    for key in ["R1", "R2", "R3"]:
        print(key, counts.get(key, 0))
    print(md_path)
    print(csv_path)


if __name__ == "__main__":
    main()
