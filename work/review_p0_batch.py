from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs"
BATCH_SIZE = 120


LOW_INFO_HINTS = [
    "cover",
    "title",
    "titlepage",
    "copyright",
    "credits",
    "dedication",
    "acknowledg",
    "bibliography",
    "index",
    "toc",
    "contents",
    "封面",
    "扉页",
    "目录",
    "版权",
    "索引",
]


def long_path(path: Path) -> Path:
    return Path("\\\\?\\" + str(path.resolve()))


def read_text(rel_path: str) -> str:
    path = ROOT / rel_path.replace("/", "\\")
    for candidate in (path, long_path(path)):
        try:
            return candidate.read_text(encoding="utf-8-sig", errors="replace")
        except OSError:
            continue
    return ""


def normalize(text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def tokenize(text: str) -> set[str]:
    return {
        token.lower()
        for token in re.findall(r"[A-Za-z][A-Za-z0-9'\-]{2,}", text)
        if token.lower() not in {"the", "and", "for", "with", "from", "this", "that", "chapter", "source", "report"}
    }


def top_entity_overlap(source_text: str, report_text: str) -> float | None:
    source_tokens = list(tokenize(source_text))
    if len(source_tokens) < 20 or len(normalize(report_text)) < 500:
        return None
    counts = Counter(source_tokens)
    top = [token for token, _ in counts.most_common(50)]
    report_lower = report_text.lower()
    hits = sum(1 for token in top if token in report_lower)
    return hits / len(top)


def is_low_info(path: str, source_text: str) -> bool:
    norm = normalize(source_text)
    lower = path.lower()
    if len(norm) < 800:
        return True
    return any(hint.lower() in lower for hint in LOW_INFO_HINTS)


def v2_markers(report_text: str) -> int:
    markers = [
        "源文件完整路径",
        "原始文件",
        "文本完整性",
        "相邻文件",
        "文献类型",
        "文件性质",
        "源文",
        "原文实际",
        "证据边界",
        "可引用",
        "不可确认",
        "复审结论",
        "审查结论",
        "OCR",
        "待核",
    ]
    return sum(1 for marker in markers if marker in report_text)


def classify(row: dict[str, str]) -> dict[str, str]:
    report = row["report"]
    source = row["suggested_source"]
    report_text = read_text(report)
    source_text = read_text(source)
    source_norm = normalize(source_text)
    report_norm = normalize(report_text)
    low_info = is_low_info(source, source_text)
    overlap = top_entity_overlap(source_text, report_text)
    markers = v2_markers(report_text)
    source_declared = source in report_text

    if not source_text:
        action = "source_unreadable_exclude"
        reason = "建议源文无法读取；不能恢复为可靠完成量。"
    elif not report_text:
        action = "report_unreadable_rebuild"
        reason = "报告无法读取；需重建。"
    elif source_declared and markers >= 7 and (low_info or (overlap is None or overlap >= 0.12)):
        action = "already_recoverable_reaudit"
        reason = "报告已含源路径和基本 V2 证据边界，可从 P0 移出，转入 P1/P2 人工复审。"
    elif low_info:
        boundary_ok = any(term in report_text[:5000] for term in ["低信息量", "无论证结构", "仅作", "不宜", "不能", "题名", "封面", "目录", "索引"])
        if boundary_ok:
            action = "low_info_auxiliary_recoverable"
            reason = "源文低信息量，报告已有边界限制；可作为 C/D 类辅助报告复核。"
        else:
            action = "low_info_needs_boundary_rewrite"
            reason = "源文低信息量，报告需降级并补证据边界，禁止理论扩写。"
    elif markers < 6:
        action = "needs_v2_rewrite"
        reason = "报告缺少 V2 复审核心字段，需按规则重写或大幅补写。"
    elif overlap is not None and overlap < 0.12:
        action = "mismatch_or_underread_manual"
        reason = "源文与报告关键词重合偏低，疑似未充分读取源文或源文错配。"
    elif not source_declared:
        action = "patch_source_path_then_reaudit"
        reason = "源文可读且匹配度尚可，但报告未明确写入源文件路径。"
    else:
        action = "manual_reaudit"
        reason = "需人工复审确认是否达到可靠完成标准。"

    return {
        "action": action,
        "report": report,
        "suggested_source": source,
        "suggestion_score": row.get("suggestion_score", ""),
        "source_chars": str(len(source_norm)),
        "report_chars": str(len(report_norm)),
        "low_info_source": str(low_info),
        "v2_marker_count": str(markers),
        "source_declared": str(source_declared),
        "entity_overlap": "" if overlap is None else f"{overlap:.3f}",
        "reason": reason,
    }


def main() -> None:
    p0_csv = OUT_DIR / "00-books-result-P0执行清单.csv"
    rows = list(csv.DictReader(p0_csv.open("r", encoding="utf-8-sig", newline="")))
    candidates = [
        row
        for row in rows
        if row["action"] == "locate_source_then_reaudit"
        and row["suggestion_confidence"] == "high"
        and row["suggested_source"]
    ]
    candidates.sort(key=lambda row: (-float(row["suggestion_score"]), row["report"]))
    selected = candidates[:BATCH_SIZE]
    reviewed = [classify(row) for row in selected]

    csv_path = OUT_DIR / "00-books-result-P0首批复审明细.csv"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "action",
                "report",
                "suggested_source",
                "suggestion_score",
                "source_chars",
                "report_chars",
                "low_info_source",
                "v2_marker_count",
                "source_declared",
                "entity_overlap",
                "reason",
            ],
        )
        writer.writeheader()
        writer.writerows(reviewed)

    counts = Counter(row["action"] for row in reviewed)
    md_path = OUT_DIR / "00-books-result-P0首批复审结论.md"
    lines: list[str] = []
    lines.append("# 00-books-result P0 首批复审结论\n\n")
    lines.append(f"本批处理对象：`locate_source_then_reaudit` 中自动匹配置信度为 high 的前 {len(reviewed)} 份报告。\n\n")
    lines.append("## 一、动作统计\n\n")
    for action, count in counts.most_common():
        lines.append(f"- `{action}`：{count}\n")
    lines.append("\n## 二、处理原则\n\n")
    lines.append("- `already_recoverable_reaudit`：从 P0 移出，但仍需按 P1/P2 做人工复审。\n")
    lines.append("- `patch_source_path_then_reaudit`：补入源文件完整路径后，再做 V2 证据边界核验。\n")
    lines.append("- `needs_v2_rewrite`：报告结构不足，不能靠补路径解决。\n")
    lines.append("- `mismatch_or_underread_manual`：源文与报告重合度低，优先人工核查。\n")
    lines.append("- `low_info_auxiliary_recoverable`：可作为低信息量辅助报告保留，不计为核心理论报告。\n\n")
    lines.append("## 三、首批明细\n\n")
    for item in reviewed:
        lines.append(f"- **{item['action']}** `{item['report']}`\n")
        lines.append(f"  - 源文：`{item['suggested_source']}`\n")
        lines.append(
            f"  - 源文/报告字符：{item['source_chars']} / {item['report_chars']}；V2 标记：{item['v2_marker_count']}；实体重合：{item['entity_overlap'] or 'NA'}\n"
        )
        lines.append(f"  - 理由：{item['reason']}\n")
    lines.append(f"\n完整明细见 `{csv_path.name}`。\n")
    md_path.write_text("".join(lines), encoding="utf-8")

    print(f"reviewed={len(reviewed)}")
    for action, count in counts.most_common():
        print(action, count)
    print(md_path)
    print(csv_path)


if __name__ == "__main__":
    main()
