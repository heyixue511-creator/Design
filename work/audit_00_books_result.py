from __future__ import annotations

import csv
import hashlib
import os
import re
import subprocess
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = "00-books/"
RESULT_ROOT = "00-books-result/"
OUT_DIR = ROOT / "outputs"


LOW_INFO_HINTS = [
    "cover",
    "封面",
    "title",
    "扉页",
    "contents",
    "目录",
    "copyright",
    "版权",
    "bibliography",
    "参考文献",
    "index",
    "索引",
    "notes",
    "注释",
    "acknowledg",
    "致谢",
    "illustration",
    "图版",
    "image",
    "图片",
    "backmatter",
]

STATUS_HINTS = [
    "已完成可靠复审",
    "已生成，待二次复审",
    "待二次复审",
    "需局部修订",
    "需大幅重写",
    "应废弃重建",
    "待合读",
    "低信息量辅助文件",
    "重复文件",
]

V2_BUCKETS = {
    "report_header": ["执行状态", "建议等级", "图像状态", "源文件完整路径", "报告文件路径", "文本完整性", "相邻文件"],
    "source_check": ["源文核验", "原文实际", "源文件实际", "复核状态", "已读取源"],
    "document_type": ["文献类型", "文件性质", "作者立场", "史料性质", "责任者"],
    "semantic_analysis": ["语义深度", "核心命题", "论证", "概念之间", "深度分析"],
    "knowledge_elements": ["知识要素", "人物", "机构", "作品", "项目", "技术", "材料"],
    "terminology": ["术语", "英文原名", "原文名", "译名", "标准化"],
    "hierarchy": ["层级", "一级", "二级", "三级", "论证结构"],
    "evidence_classification": ["实证归类", "案例", "作品", "史料", "参考文献", "图像"],
    "textbook_use": ["现当代设计史", "具体用途", "可用于", "章节"],
    "quotable_boundary": ["可引用", "不可确认", "待核", "不能确认"],
    "technical_boundary": ["OCR", "技术核验", "证据边界", "版本", "页码"],
    "review_conclusion": ["复审结论", "审查结论", "可靠完成", "当前报告"],
}


@dataclass
class FileStats:
    chars: int = 0
    lines: int = 0
    images: int = 0
    headings: int = 0
    emptyish: bool = False
    low_info: bool = False
    image_heavy: bool = False


@dataclass
class ReportAudit:
    report: str
    b_number: str = ""
    source_paths: list[str] = field(default_factory=list)
    existing_sources: list[str] = field(default_factory=list)
    missing_sources: list[str] = field(default_factory=list)
    status: str = ""
    grade: str = ""
    v2_score: int = 0
    missing_v2: list[str] = field(default_factory=list)
    report_chars: int = 0
    source_chars: int = 0
    source_images: int = 0
    low_info_source: bool = False
    entity_overlap: float | None = None
    flags: list[str] = field(default_factory=list)
    severity: str = "P3"
    report_exists_in_worktree: bool = True


def git_files() -> list[str]:
    proc = subprocess.run(
        ["git", "-c", "core.quotePath=false", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
    )
    text = proc.stdout.decode("utf-8", errors="replace")
    return [item.replace("\\", "/") for item in text.split("\0") if item]


def read_text(rel_path: str) -> str:
    path = ROOT / rel_path
    for candidate in (path, Path("\\\\?\\" + str(path.resolve()))):
        try:
            return candidate.read_text(encoding="utf-8-sig", errors="replace")
        except OSError:
            continue
    return ""


def exact_worktree_path_exists(rel_path: str) -> bool:
    current = ROOT
    for part in rel_path.split("/"):
        try:
            names = {entry.name for entry in current.iterdir()}
        except OSError:
            return False
        if part not in names:
            return False
        current = current / part
    return True


def normalize_text(text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def file_stats(rel_path: str, text: str) -> FileStats:
    norm = normalize_text(text)
    lower_path = rel_path.lower()
    lower_head = text[:800].lower()
    images = len(re.findall(r"!\[[^\]]*\]\([^)]+\)", text))
    headings = len(re.findall(r"(?m)^#{1,6}\s+", text))
    chars = len(norm)
    hint_low = any(h.lower() in lower_path or h.lower() in lower_head for h in LOW_INFO_HINTS)
    return FileStats(
        chars=chars,
        lines=text.count("\n") + 1 if text else 0,
        images=images,
        headings=headings,
        emptyish=chars < 80,
        low_info=hint_low or chars < 700,
        image_heavy=images >= 3 and chars < 1600,
    )


def extract_sources(report_text: str) -> list[str]:
    candidates = []
    patterns = [
        r"`(00-books[\\/][^`]+?\.md)`",
        r"(00-books[\\/][^\n\r`]+?\.md)",
    ]
    for pat in patterns:
        for match in re.findall(pat, report_text):
            cleaned = match.strip().strip("。；;，, )）")
            cleaned = cleaned.replace("\\", "/")
            if cleaned.startswith(SOURCE_ROOT) and cleaned not in candidates:
                candidates.append(cleaned)
    return candidates


def extract_b_number(rel_path: str, report_text: str) -> str:
    match = re.search(r"\b(B\d{4,8})\b", Path(rel_path).name)
    if match:
        return match.group(1)
    match = re.search(r"\b(B\d{4,8})\b", report_text[:300])
    return match.group(1) if match else ""


def extract_status(report_text: str) -> str:
    found = [hint for hint in STATUS_HINTS if hint in report_text[:1500]]
    return "；".join(found)


def extract_grade(report_text: str) -> str:
    head = report_text[:2000]
    match = re.search(r"建议等级[^A-E]{0,30}([A-E])\s*类", head)
    if match:
        return match.group(1)
    match = re.search(r"\b([A-E])\s*类", head)
    return match.group(1) if match else ""


def v2_coverage(report_text: str) -> tuple[int, list[str]]:
    missing = []
    for bucket, hints in V2_BUCKETS.items():
        if not any(h in report_text for h in hints):
            missing.append(bucket)
    return len(V2_BUCKETS) - len(missing), missing


def entity_overlap(source_text: str, report_text: str) -> float | None:
    if len(normalize_text(source_text)) < 1000 or len(normalize_text(report_text)) < 1000:
        return None
    candidates = re.findall(r"\b[A-Z][A-Za-z][A-Za-z'\-]{2,}\b", source_text)
    stop = {
        "The",
        "This",
        "That",
        "With",
        "From",
        "Source",
        "Section",
        "Chapter",
        "Press",
        "University",
        "London",
        "New",
        "York",
        "Design",
        "History",
    }
    counts = Counter(tok for tok in candidates if tok not in stop)
    top = [tok for tok, _ in counts.most_common(40)]
    if len(top) < 8:
        return None
    report_lower = report_text.lower()
    hits = sum(1 for tok in top if tok.lower() in report_lower)
    return hits / len(top)


def case_collisions(paths: list[str]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for path in paths:
        groups[path.lower()].append(path)
    return {key: vals for key, vals in groups.items() if len(vals) > 1}


def normalized_hash(text: str) -> str:
    norm = normalize_text(text)
    norm = re.sub(r"\bB\d{4,8}\b", "BXXXX", norm)
    norm = re.sub(r"`00-books/[^`]+?\.md`", "`SOURCE.md`", norm)
    return hashlib.sha1(norm.encode("utf-8", errors="replace")).hexdigest()


def set_severity(audit: ReportAudit) -> None:
    rank = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    severity = "P3"
    for flag in audit.flags:
        if flag.startswith("P0:"):
            severity = "P0"
            break
        if flag.startswith("P1:") and rank[severity] > 1:
            severity = "P1"
        elif flag.startswith("P2:") and rank[severity] > 2:
            severity = "P2"
    audit.severity = severity


def audit_reports(paths: list[str], source_set: set[str], source_stats: dict[str, FileStats]) -> list[ReportAudit]:
    audits: list[ReportAudit] = []
    for report in paths:
        text = read_text(report)
        audit = ReportAudit(report=report)
        audit.report_exists_in_worktree = exact_worktree_path_exists(report)
        audit.report_chars = len(normalize_text(text))
        audit.b_number = extract_b_number(report, text)
        audit.source_paths = extract_sources(text)
        audit.status = extract_status(text)
        audit.grade = extract_grade(text)
        audit.v2_score, audit.missing_v2 = v2_coverage(text)

        if not audit.report_exists_in_worktree:
            audit.flags.append("P0:tracked report path not materialized in Windows worktree")
            set_severity(audit)
            audits.append(audit)
            continue

        if not audit.source_paths:
            audit.flags.append("P0:no source path declared")
        for src in audit.source_paths:
            if src in source_set:
                audit.existing_sources.append(src)
            else:
                audit.missing_sources.append(src)
        if audit.missing_sources:
            audit.flags.append("P0:declared source path not found")

        if audit.existing_sources:
            src = audit.existing_sources[0]
            s_text = read_text(src)
            stats = source_stats[src]
            audit.source_chars = stats.chars
            audit.source_images = stats.images
            audit.low_info_source = stats.low_info or stats.image_heavy or stats.emptyish
            audit.entity_overlap = entity_overlap(s_text, text)

            reliable = "已完成可靠复审" in audit.status
            boundary_terms = ["无论证结构", "仅作", "不能", "不宜", "低信息量", "题名", "封面", "目录", "索引", "待二次复审"]
            has_low_info_boundary = any(term in text[:4000] for term in boundary_terms)
            if stats.chars == 0 and audit.report_chars > 500:
                audit.flags.append("P0:source unreadable/empty but report generated")
            elif stats.emptyish and audit.grade in {"A", "B"}:
                audit.flags.append("P1:empty/near-empty source graded high")
            elif stats.emptyish and audit.report_chars > 5000 and not has_low_info_boundary:
                audit.flags.append("P1:empty/near-empty source may be over-reported")
            if audit.low_info_source and audit.grade == "A":
                audit.flags.append("P1:low-information source graded A")
            if audit.low_info_source and audit.report_chars > max(3500, stats.chars * 6):
                audit.flags.append("P1:low-information source has overlong report")
            if reliable and audit.v2_score < 8:
                audit.flags.append("P1:marked reliable but lacks V2 coverage")
            if reliable and "已读取源" not in text and "复核状态" not in text and "源文" not in text and "原文" not in text:
                audit.flags.append("P1:marked reliable without explicit source-reading evidence")
            if audit.entity_overlap is not None and audit.entity_overlap < 0.18 and not audit.low_info_source:
                audit.flags.append("P1:low source/report entity overlap")
            if audit.v2_score < 6:
                audit.flags.append("P2:very incomplete V2 structure")
            elif audit.v2_score < 9:
                audit.flags.append("P2:partial V2 structure")
        elif audit.source_paths:
            audit.flags.append("P2:source cannot be measured")

        if not audit.flags and audit.v2_score < 10:
            audit.flags.append("P3:minor V2 omissions")
        set_severity(audit)
        audits.append(audit)
    return audits


def write_csv(audits: list[ReportAudit], path: Path) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(
            [
                "severity",
                "report",
                "b_number",
                "status",
                "grade",
                "v2_score",
                "missing_v2",
                "source_paths",
                "missing_sources",
                "report_chars",
                "source_chars",
                "source_images",
                "low_info_source",
                "entity_overlap",
                "flags",
                "report_exists_in_worktree",
            ]
        )
        for a in audits:
            writer.writerow(
                [
                    a.severity,
                    a.report,
                    a.b_number,
                    a.status,
                    a.grade,
                    a.v2_score,
                    ";".join(a.missing_v2),
                    "\n".join(a.source_paths),
                    "\n".join(a.missing_sources),
                    a.report_chars,
                    a.source_chars,
                    a.source_images,
                    a.low_info_source,
                    "" if a.entity_overlap is None else f"{a.entity_overlap:.3f}",
                    " | ".join(a.flags),
                    a.report_exists_in_worktree,
                ]
            )


def bullet_list(items: list[str], limit: int = 30) -> str:
    if not items:
        return "- 无\n"
    shown = items[:limit]
    body = "".join(f"- `{item}`\n" for item in shown)
    if len(items) > limit:
        body += f"- ……另有 {len(items) - limit} 项，见 CSV 明细。\n"
    return body


def write_markdown(
    audits: list[ReportAudit],
    source_paths: list[str],
    report_paths: list[str],
    missing_sources_without_reports: list[str],
    duplicate_b: dict[str, list[str]],
    duplicate_source_reports: dict[str, list[str]],
    exact_duplicate_reports: dict[str, list[str]],
    collisions: dict[str, list[str]],
    md_path: Path,
    csv_name: str,
) -> None:
    severity_counts = Counter(a.severity for a in audits)
    flag_counts = Counter(flag for a in audits for flag in a.flags)
    high = [a for a in audits if a.severity in {"P0", "P1"}]
    high.sort(key=lambda a: ({"P0": 0, "P1": 1, "P2": 2, "P3": 3}[a.severity], a.report))

    no_source = [a.report for a in audits if any(f.startswith("P0:no source") for f in a.flags)]
    missing_declared = [a.report for a in audits if any(f.startswith("P0:declared source") for f in a.flags)]
    low_info_a = [a.report for a in audits if any("low-information source graded A" in f for f in a.flags)]
    low_v2_reliable = [a.report for a in audits if any("marked reliable but lacks V2" in f for f in a.flags)]
    low_overlap = [a.report for a in audits if any("low source/report entity overlap" in f for f in a.flags)]

    lines: list[str] = []
    lines.append("# 00-books-result 全量复审审计报告\n\n")
    lines.append("依据：`00-books-result/00-books Markdown 深度报告生成与复审规则.md`（V2.0）。\n\n")
    lines.append("本轮审计重新读取 `00-books/` 与 `00-books-result/` 的本地完整克隆文件，先做全量机器审计，用于定位需要人工复核、局部修订、大幅重写或废弃重建的报告。\n\n")
    lines.append("## 一、总量\n\n")
    lines.append(f"- `00-books/` Markdown 源文件：{len(source_paths)}\n")
    lines.append(f"- `00-books-result/` `*report.md`：{len(report_paths)}\n")
    lines.append(f"- 源文件未被任何报告声明引用：{len(missing_sources_without_reports)}\n")
    lines.append(f"- 声明同一源文件的多个报告组：{len(duplicate_source_reports)}\n")
    lines.append(f"- 重复 B 编号组：{len(duplicate_b)}\n")
    lines.append(f"- 规范化后正文完全相同的报告组：{len(exact_duplicate_reports)}\n")
    lines.append(f"- Git 路径大小写冲突组：{len(collisions)}\n\n")

    lines.append("## 二、风险分层\n\n")
    for sev in ["P0", "P1", "P2", "P3"]:
        lines.append(f"- {sev}：{severity_counts.get(sev, 0)}\n")
    lines.append("\n")

    lines.append("P0 代表报告无法被视为可靠完成量；P1 代表高度疑似不正确，需要优先人工复核；P2 代表结构或覆盖不足；P3 为轻微缺项或低优先级问题。\n\n")

    lines.append("## 三、主要问题类型\n\n")
    for flag, count in flag_counts.most_common(20):
        lines.append(f"- {flag}：{count}\n")
    lines.append("\n")

    lines.append("## 四、优先处理清单\n\n")
    lines.append("### 1. 没有声明源文件路径的报告\n\n")
    lines.append(bullet_list(no_source, 40))
    lines.append("\n### 2. 声明的源文件路径不存在\n\n")
    lines.append(bullet_list(missing_declared, 40))
    lines.append("\n### 3. 低信息量源文件却评为 A 类或过度展开\n\n")
    lines.append(bullet_list(low_info_a, 40))
    lines.append("\n### 4. 标记“已完成可靠复审”但 V2 覆盖不足\n\n")
    lines.append(bullet_list(low_v2_reliable, 40))
    lines.append("\n### 5. 源文与报告英文实体重合度过低\n\n")
    lines.append(bullet_list(low_overlap, 40))

    lines.append("\n## 五、重复与冲突\n\n")
    lines.append("### 1. 重复 B 编号示例\n\n")
    if duplicate_b:
        for bnum, vals in list(sorted(duplicate_b.items()))[:20]:
            lines.append(f"- `{bnum}`：{len(vals)} 个报告\n")
            for item in vals[:4]:
                lines.append(f"  - `{item}`\n")
    else:
        lines.append("- 无\n")

    lines.append("\n### 2. 同一源文件对应多个报告示例\n\n")
    if duplicate_source_reports:
        for src, vals in list(sorted(duplicate_source_reports.items(), key=lambda kv: -len(kv[1])))[:20]:
            lines.append(f"- `{src}`：{len(vals)} 个报告\n")
            for item in vals[:5]:
                lines.append(f"  - `{item}`\n")
    else:
        lines.append("- 无\n")

    lines.append("\n### 3. 大小写路径冲突示例\n\n")
    if collisions:
        for vals in list(collisions.values())[:20]:
            lines.append(f"- {len(vals)} 个路径在 Windows 上冲突：\n")
            for item in vals[:4]:
                lines.append(f"  - `{item}`\n")
    else:
        lines.append("- 无\n")

    lines.append("\n## 六、高风险报告样本\n\n")
    for a in high[:120]:
        flags = "；".join(a.flags)
        src = a.existing_sources[0] if a.existing_sources else (a.source_paths[0] if a.source_paths else "未声明")
        overlap = "NA" if a.entity_overlap is None else f"{a.entity_overlap:.2f}"
        lines.append(f"- **{a.severity}** `{a.report}`\n")
        lines.append(f"  - 源文件：`{src}`\n")
        lines.append(f"  - 状态/等级：{a.status or '未标明'} / {a.grade or '未标明'}；V2 覆盖：{a.v2_score}/12；实体重合：{overlap}\n")
        lines.append(f"  - 问题：{flags}\n")

    lines.append("\n## 七、源文件未覆盖示例\n\n")
    lines.append(bullet_list(missing_sources_without_reports, 80))

    lines.append("\n## 八、复审建议\n\n")
    lines.append("1. 先处理 P0：无源路径、源路径不存在、空源文过度报告、重复 B 编号和大小写冲突。这些不能计入可靠完成量。\n")
    lines.append("2. 再处理 P1：低信息量文件 A 类化、可靠复审但缺 V2 核心章节、源文与报告实体重合度过低。这一类最可能是“根据文件名/旧报告扩写”的错误。\n")
    lines.append("3. 对低信息量源文件，按规则降级为 C/D/E，并明确只能作为版本、目录、图像、索引或合读线索。\n")
    lines.append("4. 对重复切片、整书合并文件和章节拆分文件，建立“可计入可靠完成量”的唯一映射，避免重复计数。\n")
    lines.append("5. 修订报告时每篇必须回填源文件完整路径、文件类型、文本完整性、相邻文件关系、证据边界、可引用/不可确认内容和复审结论。\n")
    lines.append(f"\n完整明细见 `{csv_name}`。\n")

    md_path.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    files = git_files()
    source_paths = [p for p in files if p.startswith(SOURCE_ROOT) and p.lower().endswith(".md")]
    report_paths = [p for p in files if p.startswith(RESULT_ROOT) and p.endswith("report.md")]
    source_set = set(source_paths)

    source_stats = {p: file_stats(p, read_text(p)) for p in source_paths}
    audits = audit_reports(report_paths, source_set, source_stats)

    source_to_reports: dict[str, list[str]] = defaultdict(list)
    b_to_reports: dict[str, list[str]] = defaultdict(list)
    hash_to_reports: dict[str, list[str]] = defaultdict(list)
    for a in audits:
        if a.b_number:
            b_to_reports[a.b_number].append(a.report)
        for src in a.existing_sources:
            source_to_reports[src].append(a.report)
        text = read_text(a.report)
        if text:
            hash_to_reports[normalized_hash(text)].append(a.report)

    duplicate_b = {b: vals for b, vals in b_to_reports.items() if len(vals) > 1}
    duplicate_source_reports = {src: vals for src, vals in source_to_reports.items() if len(vals) > 1}
    exact_duplicate_reports = {h: vals for h, vals in hash_to_reports.items() if len(vals) > 1}
    missing_sources_without_reports = sorted(source_set - set(source_to_reports))
    collisions = case_collisions([p for p in files if p.startswith(SOURCE_ROOT) or p.startswith(RESULT_ROOT)])

    for src, vals in duplicate_source_reports.items():
        for a in audits:
            if a.report in vals:
                a.flags.append("P1:multiple reports declare same source")
                set_severity(a)
    for b, vals in duplicate_b.items():
        for a in audits:
            if a.report in vals:
                a.flags.append("P0:duplicate B number")
                set_severity(a)

    csv_path = OUT_DIR / "00-books-result-audit-details.csv"
    md_path = OUT_DIR / "00-books-result复审审计报告.md"
    write_csv(audits, csv_path)
    write_markdown(
        audits,
        source_paths,
        report_paths,
        missing_sources_without_reports,
        duplicate_b,
        duplicate_source_reports,
        exact_duplicate_reports,
        collisions,
        md_path,
        csv_path.name,
    )

    print(f"reports={len(report_paths)} sources={len(source_paths)}")
    print(f"p0={sum(1 for a in audits if a.severity == 'P0')} p1={sum(1 for a in audits if a.severity == 'P1')} p2={sum(1 for a in audits if a.severity == 'P2')} p3={sum(1 for a in audits if a.severity == 'P3')}")
    print(md_path)
    print(csv_path)


if __name__ == "__main__":
    main()
