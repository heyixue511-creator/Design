from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "00-books"
REPORT_ROOT = ROOT / "00-books-result"
OUTPUT_ROOT = ROOT / "outputs"
DETAIL_CSV = OUTPUT_ROOT / "00-books-result全量复审明细.csv"
SUMMARY_MD = OUTPUT_ROOT / "00-books-result全量复审报告.md"
QUEUE_CSV = OUTPUT_ROOT / "00-books-result全量复审重写队列.csv"

NEW_TABLE_HEADER = "| 要素类型 | 原文名称 | 标准英文／原文名 | 原文语境 | 可归入议题 | 证据状态 |"
OLD_TABLE_HEADERS = (
    "| 要素类型 | 原文名称 | 原文语境/可归入议题 | 证据状态 |",
    "| 类型 | 原文名称 | 原文语境 | 可归入议题 |",
)
BAD_MARKERS = (
    "源文正文暂未读取",
    "Git blob 读取错误",
    "git blob 读取错误",
    "未能读取源文正文",
    "源文读取失败",
)
GENERIC_MARKERS = (
    "需按源文逐段判断的章节主题",
    "当前切片的核心命题可以从标题",
    "源文不是孤立列举材料，而是通过反复出现的关键词",
    "若源文是论文或章节正文",
)
KNOWLEDGE_NOISE = {
    "images",
    "image",
    "design",
    "history",
    "chapter",
    "section",
    "source",
    "contents",
    "copyright",
    "正文",
    "章节",
    "图片",
}

PRIMARY_SOURCE_PATTERNS = (
    re.compile(r"(?:\*\*)?(?:源文件完整路径|源文文件路径|源文路径)(?:\*\*)?[^\n\r]{0,8}`([^`]*00-books[\\/][^`]+?\.md)`", re.I),
    re.compile(r"(?:源文件完整路径|源文文件路径|源文路径)[^\n\r]{0,8}(00-books[\\/][^\n\r`]+?\.md)", re.I),
)
SOURCE_PATTERNS = (
    re.compile(r"`([^`]*00-books[\\/][^`]+?\.md)`", re.I),
    re.compile(r"(00-books[\\/][^\n\r`]+?\.md)", re.I),
)

REQUIRED_SECTIONS = {
    "source_check": ("源文核验", "内容概述"),
    "document_nature": ("文献性质", "作者立场", "史料等级"),
    "semantic_analysis": ("语义深度分析", "核心命题"),
    "knowledge_elements": ("知识要素解构", "知识要素表"),
    "hierarchy": ("层级体系", "论证结构", "论证层级"),
    "evidence": ("实证归类", "实证材料", "案例与图像线索"),
    "textbook_use": ("现当代设计史", "教材、研究与索引用途", "教材用途"),
    "quote_boundary": ("可引用内容", "不可确认内容", "可用边界与不可用边界"),
    "technical_boundary": ("技术核验", "证据边界"),
    "conclusion": ("复审结论", "审查结论"),
}


@dataclass
class AuditRow:
    report: str
    sources: list[str] = field(default_factory=list)
    mapping: str = ""
    source_chars: int = 0
    report_chars: int = 0
    source_chinese_chars: int = 0
    table_rows: int = 0
    missing_sections: list[str] = field(default_factory=list)
    flags: list[str] = field(default_factory=list)
    severity: str = "P3"


def long_path(path: Path) -> Path:
    resolved = path.resolve()
    return resolved if str(resolved).startswith("\\\\?\\") else Path("\\\\?\\" + str(resolved))


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        pass
    try:
        return long_path(path).read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        pass
    return ""


def exists(path: Path) -> bool:
    try:
        if path.exists():
            return True
    except OSError:
        pass
    try:
        return long_path(path).exists()
    except OSError:
        pass
    return False


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def normalize_source(value: str) -> str:
    value = value.strip().strip("。；;，, )）]'\"").replace("\\", "/")
    pos = value.lower().find("00-books/")
    if pos >= 0:
        value = value[pos:]
    md_pos = value.lower().find(".md")
    if md_pos >= 0:
        value = value[: md_pos + 3]
    return value


def extract_sources(text: str) -> list[str]:
    for patterns in (PRIMARY_SOURCE_PATTERNS, SOURCE_PATTERNS):
        found: list[str] = []
        for pattern in patterns:
            for match in pattern.findall(text):
                source = normalize_source(match)
                if source.startswith("00-books/") and source.endswith(".md") and source not in found:
                    found.append(source)
        if found:
            # Legacy prose may mention neighbouring files; only the first verified
            # source is treated as the report's primary correspondence.
            return found[:1]
    return []


def exact_fallback(report: Path) -> str:
    parent = report.relative_to(REPORT_ROOT).parent
    source_dir = SOURCE_ROOT / parent
    if not exists(source_dir):
        return ""
    stem = re.sub(r"-report$", "", report.stem, flags=re.I)
    stems = [stem, re.sub(r"^B\d+[-_]", "", stem, flags=re.I)]
    for candidate_stem in stems:
        candidate = source_dir / f"{candidate_stem}.md"
        if exists(candidate):
            return rel(candidate)
    try:
        files = list(source_dir.glob("*.md"))
    except OSError:
        files = []
    return rel(files[0]) if len(files) == 1 else ""


def visible_chars(text: str) -> int:
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    return len(re.sub(r"\s+", "", text))


def table_block(text: str) -> str:
    match = re.search(
        r"(?ms)^##\s*(?:4\.|四[、.．]).*?(?:知识要素|核心概念).*?(?=^##\s*(?:5\.|五[、.．])|\Z)",
        text,
    )
    return match.group(0) if match else ""


def table_rows(block: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in block.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) == 6 and cells[0] not in {"要素类型", "---"} and not all(set(c) <= {"-", ":"} for c in cells):
            rows.append(cells)
    return rows


def copied_source_chars(source: str, report: str) -> tuple[int, int]:
    copied = 0
    longest = 0
    source_lines = {
        re.sub(r"\s+", " ", line).strip()
        for line in source.splitlines()
        if len(re.sub(r"\s+", "", line)) >= 180
    }
    for line in report.splitlines():
        clean = re.sub(r"^\s*(?:[-*]|\d+[.)]|\|)?\s*", "", line).strip()
        if clean.endswith("|"):
            clean = clean[:-1].strip()
        clean = re.sub(r"\s+", " ", clean)
        if len(clean) < 180 or clean.startswith("#"):
            continue
        if clean in source_lines:
            copied += len(clean)
            longest = max(longest, len(clean))
    return copied, longest


def has_section(text: str, hints: tuple[str, ...]) -> bool:
    headings = "\n".join(re.findall(r"(?m)^#{2,4}\s+.+$", text))
    return any(hint in headings for hint in hints)


def classify(row: AuditRow) -> None:
    if any(flag.startswith("P0:") for flag in row.flags):
        row.severity = "P0"
    elif any(flag.startswith("P1:") for flag in row.flags):
        row.severity = "P1"
    elif any(flag.startswith("P2:") for flag in row.flags):
        row.severity = "P2"
    else:
        row.severity = "P3"


def audit_report(path: Path) -> AuditRow:
    report_text = read_text(path)
    row = AuditRow(report=rel(path), report_chars=visible_chars(report_text))
    if not report_text:
        row.flags.append("P0:报告不可读或为空")
        classify(row)
        return row

    explicit_sources = extract_sources(report_text)
    row.sources = explicit_sources
    row.mapping = "explicit" if explicit_sources else ""
    if not row.sources:
        fallback = exact_fallback(path)
        if fallback:
            row.sources = [fallback]
            row.mapping = "exact_fallback"
            row.flags.append("P2:报告缺少显式源路径（已精确定位）")
        else:
            row.flags.append("P0:报告无法定位对应源文")

    source_texts: list[str] = []
    for source in row.sources:
        source_path = ROOT / source
        if not exists(source_path):
            row.flags.append(f"P0:引用源文件不存在:{source}")
            continue
        source_text = read_text(source_path)
        source_texts.append(source_text)
    source_text = "\n".join(source_texts)
    row.source_chars = visible_chars(source_text)
    row.source_chinese_chars = len(re.findall(r"[\u3400-\u9fff]", source_text))
    if row.sources and not source_text.strip():
        row.flags.append("P2:对应源文为空或不可读")

    for marker in BAD_MARKERS:
        if marker in report_text:
            row.flags.append(f"P0:残留读取失败标记:{marker}")
    for marker in GENERIC_MARKERS:
        if marker in report_text:
            row.flags.append(f"P1:残留通用占位表述:{marker}")

    is_high_info = row.source_chars >= 3000
    row.missing_sections = [name for name, hints in REQUIRED_SECTIONS.items() if not has_section(report_text, hints)]
    if is_high_info and row.missing_sections:
        row.flags.append("P1:高信息量源文缺少V2核心节:" + ",".join(row.missing_sections))
    elif row.missing_sections and len(row.missing_sections) >= 5:
        row.flags.append("P2:低/中信息量报告结构过度缺省:" + ",".join(row.missing_sections))

    block = table_block(report_text)
    rows = table_rows(block)
    row.table_rows = len(rows)
    if not block:
        row.flags.append("P1:缺少知识要素节")
    elif NEW_TABLE_HEADER not in block:
        row.flags.append("P1:知识要素表不是规范六列表头")
    if any(header in report_text for header in OLD_TABLE_HEADERS):
        row.flags.append("P1:残留旧版知识要素表")
    if block and not rows and row.source_chars >= 700:
        row.flags.append("P1:知识要素表无有效六列数据行")
    if rows:
        names = [cells[1].strip().lower() for cells in rows]
        noise = sorted({name for name in names if name in KNOWLEDGE_NOISE})
        if noise:
            row.flags.append("P2:知识要素含噪声词:" + ",".join(noise))
        if row.source_chinese_chars >= 500:
            chinese_rows = sum(bool(re.search(r"[\u3400-\u9fff]", cells[1])) for cells in rows)
            if chinese_rows == 0:
                row.flags.append("P1:中文源文的知识要素表没有中文名称")
            elif chinese_rows < min(3, len(rows)):
                row.flags.append("P2:中文源文的中文知识要素覆盖偏少")

    if is_high_info and row.report_chars < 1800:
        row.flags.append("P0:高信息量源文对应报告过短")
    elif row.source_chars >= 1000 and row.report_chars < 900:
        row.flags.append("P1:报告篇幅不足以支撑源文复审")

    if source_text:
        copied, longest = copied_source_chars(source_text, report_text)
        if longest >= 900 or copied >= 5000 or (row.report_chars and copied / row.report_chars >= 0.45 and copied >= 1800):
            row.flags.append(f"P0:疑似长篇搬运源文:复制字符={copied},最长段={longest}")
        elif longest >= 500 or copied >= 2500:
            row.flags.append(f"P1:源文摘录偏长:复制字符={copied},最长段={longest}")

    classify(row)
    return row


def source_inventory() -> list[str]:
    return sorted(rel(path) for path in SOURCE_ROOT.rglob("*.md"))


def write_outputs(rows: list[AuditRow], sources: list[str]) -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    referenced: defaultdict[str, list[str]] = defaultdict(list)
    for row in rows:
        for source in row.sources:
            if exists(ROOT / source):
                referenced[source].append(row.report)

    missing_sources = [source for source in sources if source not in referenced]
    duplicate_sources = {source: reports for source, reports in referenced.items() if len(reports) > 1}
    severity_counts = Counter(row.severity for row in rows)
    flag_counts: Counter[str] = Counter()
    for row in rows:
        categories = {flag.split(":", 1)[1].split(":", 1)[0] for flag in row.flags}
        flag_counts.update(categories)

    fieldnames = [
        "severity", "report", "sources", "mapping", "source_chars", "report_chars",
        "source_chinese_chars", "table_rows", "missing_sections", "flags",
    ]
    with DETAIL_CSV.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({
                "severity": row.severity,
                "report": row.report,
                "sources": " | ".join(row.sources),
                "mapping": row.mapping,
                "source_chars": row.source_chars,
                "report_chars": row.report_chars,
                "source_chinese_chars": row.source_chinese_chars,
                "table_rows": row.table_rows,
                "missing_sections": " | ".join(row.missing_sections),
                "flags": " | ".join(row.flags),
            })

    queue = [row for row in rows if row.severity in {"P0", "P1"}]
    with QUEUE_CSV.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["priority", "report", "source", "reasons"])
        writer.writeheader()
        for row in sorted(queue, key=lambda item: (item.severity, item.report)):
            writer.writerow({
                "priority": row.severity,
                "report": row.report,
                "source": " | ".join(row.sources),
                "reasons": " | ".join(row.flags),
            })
        for source in missing_sources:
            writer.writerow({"priority": "P0", "report": "", "source": source, "reasons": "源文没有对应报告"})

    top_flags = "\n".join(f"- {name}：{count}" for name, count in flag_counts.most_common(20)) or "- 未发现问题"
    duplicate_examples = "\n".join(
        f"- `{source}`：{len(reports)} 篇报告" for source, reports in list(duplicate_sources.items())[:20]
    ) or "- 无"
    missing_examples = "\n".join(f"- `{source}`" for source in missing_sources[:20]) or "- 无"
    SUMMARY_MD.write_text(
        f"""# 00-books-result 全量复审报告

- 审查日期：{date.today().isoformat()}
- 依据：`00-books-result/00-books Markdown 深度报告生成与复审规则.md` V2.1
- 审查模式：只读审查；未改写 `00-books-result/` 报告

## 总体结果

| 项目 | 数量 |
|---|---:|
| `00-books/` 源 Markdown | {len(sources)} |
| `00-books-result/` 深度报告 | {len(rows)} |
| 已被报告覆盖的源文 | {len(referenced)} |
| 缺失深度报告的源文 | {len(missing_sources)} |
| 被多篇报告重复引用的源文 | {len(duplicate_sources)} |
| P0 必须重写／补全 | {severity_counts['P0']} |
| P1 重要修订 | {severity_counts['P1']} |
| P2 规范修订 | {severity_counts['P2']} |
| P3 未发现自动审计问题 | {severity_counts['P3']} |

说明：P0/P1/P2 是自动复审优先级，不等同于学术质量最终判定。P3 仅表示未触发本轮机器规则，仍需抽样人工深读。

## 主要问题

{top_flags}

## 覆盖缺口（前 20 项）

{missing_examples}

## 重复映射（前 20 项）

{duplicate_examples}

## 审查口径

- 读取并核对每篇报告所指向的 `00-books/` 源文；源路径缺失时只采用同目录同名或单文件目录的精确回退，不以模糊标题猜测覆盖。
- 检查读取失败标记、源文缺失、报告过短、通用占位表述、V2.0 核心结构、六列知识要素表、中英文名称覆盖、旧表残留及知识要素噪声。
- 以报告中可定位到源文的长段落为依据检查原文搬运；阈值用于发现高风险对象，不替代人工引文判断。

## 输出

- 完整明细：`outputs/00-books-result全量复审明细.csv`
- P0/P1 重写与补全队列：`outputs/00-books-result全量复审重写队列.csv`
""",
        encoding="utf-8",
    )

    print(f"sources={len(sources)} reports={len(rows)} covered={len(referenced)} missing={len(missing_sources)}")
    print(f"severity={dict(severity_counts)} duplicate_sources={len(duplicate_sources)}")
    print(f"details={DETAIL_CSV.relative_to(ROOT).as_posix()}")
    print(f"summary={SUMMARY_MD.relative_to(ROOT).as_posix()}")
    print(f"queue={QUEUE_CSV.relative_to(ROOT).as_posix()}")


def main() -> None:
    rule = REPORT_ROOT / "00-books Markdown 深度报告生成与复审规则.md"
    reports = sorted(path for path in REPORT_ROOT.rglob("*.md") if path != rule)
    with ThreadPoolExecutor(max_workers=8) as pool:
        rows = list(pool.map(audit_report, reports, chunksize=32))
    write_outputs(rows, source_inventory())


if __name__ == "__main__":
    main()
