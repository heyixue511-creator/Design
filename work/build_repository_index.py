from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK_ROOT = ROOT / "00-books"
BOOK_REPORT_ROOT = ROOT / "00-books-result"
PAPER_ROOT = ROOT / "00-Paper"
PAPER_REPORT_ROOT = ROOT / "00-Paper-result"
INDEX_ROOT = ROOT / "index-system"
GENERATED_ROOT = INDEX_ROOT / "generated"

RULES_FILE = "00-books-result/00-books Markdown 深度报告生成与复审规则.md"
RESULT_DOC_NAMES = {"INDEX.md", "README.md", "PROGRESS.md"}


THEMES = [
    (
        "TH001",
        "学科史",
        [
            "design history",
            "historiography",
            "设计史",
            "设计研究史",
            "history of design",
            "margolin",
            "doordan",
        ],
        "第一章 设计史的对象、边界与方法",
    ),
    (
        "TH002",
        "理论基础",
        [
            "theory",
            "理论",
            "modernity",
            "modernism",
            "visual culture",
            "material culture",
            "物质文化",
            "现代性",
            "现代主义",
        ],
        "第一章 设计史的对象、边界与方法",
    ),
    (
        "TH003",
        "方法论",
        [
            "method",
            "methodology",
            "research",
            "方法",
            "研究方法",
            "ethnography",
            "probe",
            "probes",
        ],
        "第七章 设计研究与设计思维",
    ),
    (
        "TH004",
        "重要人物",
        [
            "biography",
            "life",
            "letters",
            "memoir",
            "传记",
            "生平",
            "人物",
            "architect",
            "designer",
        ],
        "按人物所属议题进入相应章节",
    ),
    (
        "TH005",
        "重要作品与案例",
        [
            "case",
            "work",
            "works",
            "exhibition",
            "museum",
            "poster",
            "product",
            "案例",
            "作品",
            "展览",
            "博物馆",
            "海报",
        ],
        "按案例所属议题进入相应章节",
    ),
    (
        "TH006",
        "历史分期",
        [
            "industrial",
            "industrialization",
            "nineteenth",
            "twentieth",
            "war",
            "postwar",
            "工业化",
            "近代",
            "现代",
            "战后",
            "十九世纪",
            "二十世纪",
        ],
        "第二章 工业化、现代性与设计制度",
    ),
    (
        "TH007",
        "地域研究",
        [
            "china",
            "chinese",
            "japan",
            "japanese",
            "global",
            "europe",
            "american",
            "中国",
            "日本",
            "全球",
            "欧洲",
            "美国",
            "后殖民",
        ],
        "第十章 全球设计史与中国现代设计",
    ),
    (
        "TH008",
        "专题研究",
        [
            "graphic",
            "typography",
            "fashion",
            "architecture",
            "hci",
            "interaction",
            "sustainability",
            "transition",
            "平面",
            "字体",
            "服装",
            "建筑",
            "交互",
            "可持续",
            "转型设计",
        ],
        "按专题进入第五、六、九、十一章",
    ),
    (
        "TH009",
        "教材适配",
        [
            "teaching",
            "education",
            "pedagogy",
            "curriculum",
            "school",
            "教材",
            "教学",
            "教育",
            "课程",
            "学院",
            "包豪斯",
            "bauhaus",
            "ulm",
        ],
        "第四章 现代主义设计与包豪斯",
    ),
]

CHAPTERS = [
    ("第一章", "设计史的对象、边界与方法", ["design history", "historiography", "设计史", "methodology", "方法论"]),
    ("第二章", "工业化、现代性与设计制度", ["industrial", "industry", "industrialization", "工业", "工业化", "modernity", "现代性", "department store"]),
    ("第三章", "工艺美术运动与现代设计前史", ["arts and crafts", "ruskin", "morris", "工艺美术", "装饰", "ornament", "craft"]),
    ("第四章", "现代主义设计与包豪斯", ["bauhaus", "ulm", "modernism", "gropius", "moholy", "包豪斯", "乌尔姆", "现代主义"]),
    ("第五章", "平面设计、印刷与视觉传播", ["graphic", "typography", "poster", "printing", "isotype", "平面", "印刷", "字体", "海报"]),
    ("第六章", "产品、消费与日常生活", ["product", "consumer", "consumption", "fashion", "domestic", "产品", "消费", "日常", "服装"]),
    ("第七章", "设计研究与设计思维", ["design research", "design thinking", "wicked", "cross", "buchanan", "设计研究", "设计思维"]),
    ("第八章", "技术、人工物与社会关系", ["artifact", "technology", "latour", "winner", "bijker", "技术", "人工物", "政治"]),
    ("第九章", "数字设计、HCI 与交互设计", ["hci", "interaction", "interface", "software", "digital", "交互", "界面", "数字"]),
    ("第十章", "全球设计史与中国现代设计", ["global", "china", "chinese", "postcolonial", "全球", "中国", "后殖民"]),
    ("第十一章", "可持续设计、转型设计与当代议题", ["sustainability", "transition design", "future", "可持续", "转型设计", "未来"]),
    ("第十二章", "总结：从作品史到人工世界史", ["artificial world", "world history", "综合", "人工世界", "world history of design"]),
]

STOP_MARKERS = ("停止使用", "无对应源文", "误映射", "orphan", "P0")


@dataclass
class ReportInfo:
    path: str
    source: str = ""
    doc_id: str = ""
    status: str = ""
    level: str = ""
    file_type: str = ""
    integrity: str = ""
    chars: int = 0
    headings: list[str] = field(default_factory=list)
    summary: str = ""


@dataclass
class SourceInfo:
    path: str
    collection: str
    doc_id: str
    author: str
    title: str
    work_title: str
    year: str
    doc_type: str
    size: int
    chars: int
    lines: int
    sha1: str
    first_heading: str
    report: ReportInfo | None
    themes: list[tuple[str, str, list[str]]] = field(default_factory=list)
    chapter: str = ""
    keywords: list[str] = field(default_factory=list)
    importance: str = "C"
    completeness: str = ""
    teaching_use: str = ""
    note: str = ""


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def long_path(path: Path) -> Path:
    resolved = path.resolve()
    text = str(resolved)
    return resolved if text.startswith("\\\\?\\") else Path("\\\\?\\" + text)


def read_bytes(path: Path) -> bytes:
    try:
        return path.read_bytes()
    except OSError:
        return long_path(path).read_bytes()


def read_text(path: Path) -> str:
    data = read_bytes(path)
    for encoding in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def ps_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def powershell_files(root: Path, filter_value: str = "*") -> list[Path]:
    if not root.exists():
        return []
    command = (
        "[Console]::OutputEncoding=[System.Text.UTF8Encoding]::new($false); "
        "$OutputEncoding=[Console]::OutputEncoding; "
        f"Get-ChildItem -LiteralPath {ps_quote(str(root))} -Recurse -File -Filter {ps_quote(filter_value)} "
        "| ForEach-Object { $_.FullName }"
    )
    result = subprocess.run(
        ["powershell", "-NoProfile", "-Command", command],
        cwd=str(ROOT),
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return [Path(line.strip()) for line in result.stdout.splitlines() if line.strip()]


def sha1_bytes(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()


def first_heading(text: str) -> str:
    match = re.search(r"(?m)^#{1,3}\s+(.+?)\s*$", text)
    return clean_cell(match.group(1)) if match else ""


def clean_cell(value: str, limit: int = 500) -> str:
    value = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", " ", value or "")
    value = re.sub(r"\s+", " ", value or "").strip()
    value = value.replace("|", "／")
    return value[:limit]


def normalize_path(value: str) -> str:
    value = value.strip().strip("`'\"。；;，, )）]").replace("\\", "/")
    for prefix in ("00-books/", "00-Paper/", "00-books-result/", "00-Paper-result/"):
        pos = value.find(prefix)
        if pos >= 0:
            value = value[pos:]
            break
    md_pos = value.lower().find(".md")
    if md_pos >= 0:
        value = value[: md_pos + 3]
    return value


def parse_work_metadata(path: Path, collection: str) -> tuple[str, str, str, str]:
    parts = path.relative_to(ROOT).parts
    parent = parts[1] if len(parts) > 2 else path.stem
    stem = path.stem
    author = ""
    work_title = parent
    year = ""

    match = re.match(r"^(?P<author>[^：:《]+)[：:]\s*《?(?P<title>.*?)(?:》)?(?:[，,]\s*(?P<year>\d{4}))?$", parent)
    if match:
        author = clean_cell(match.group("author"), 120)
        work_title = clean_cell(match.group("title"), 240).strip("《》")
        year = match.group("year") or ""
    else:
        year_match = re.search(r"(?:^|[，,\s_-])((?:1|2)\d{3})(?:$|[，,\s_-])", parent)
        if year_match:
            year = year_match.group(1)
        if "：" in parent:
            author, work_title = parent.split("：", 1)
        elif ":" in parent:
            author, work_title = parent.split(":", 1)

    if collection == "paper" and not author:
        match = re.match(r"^(P\d+)[-_](.+)$", stem, re.I)
        if match:
            work_title = match.group(2)

    title = stem if stem != path.parent.name else work_title
    return clean_cell(author, 120), clean_cell(title, 240), clean_cell(work_title, 240), year


def doc_type_from_path(path: Path, collection: str, text: str) -> str:
    stem = path.stem.lower()
    if collection == "paper":
        return "论文 / 文章 / 书评"
    if any(token in stem for token in ("bibliography", "references", "notes", "index")):
        return "书目 / 注释 / 索引切片"
    if any(token in stem for token in ("cover", "title", "toc", "contents", "preface", "acknowledg")):
        return "封面 / 目录 / 前言切片"
    if re.search(r"(?m)^#{1,3}\s+chapter\b", text[:5000], re.I):
        return "章节"
    return "书籍 / 章节 Markdown"


def extract_report_info(path: Path) -> ReportInfo:
    text = read_text(path)
    info = ReportInfo(path=rel(path), chars=len(text))
    info.headings = [clean_cell(m.group(1), 140) for m in re.finditer(r"(?m)^#{1,4}\s+(.+?)\s*$", text[:30000])]
    header = text[:5000]

    source_patterns = [
        r"(?:源文件完整路径|源文文件路径|源文路径|原始文件)\D{0,20}`([^`]+?\.md)`",
        r"`((?:00-books|00-Paper)/[^`]+?\.md)`",
    ]
    for pattern in source_patterns:
        match = re.search(pattern, header, re.I)
        if match:
            source = normalize_path(match.group(1))
            if source.startswith(("00-books/", "00-Paper/")):
                info.source = source
                break

    id_match = re.search(r"(?m)^#\s+((?:B|P)\d{2,8})[-\s]", text)
    if not id_match:
        id_match = re.search(r"(?:报告编号|文献编号)\s*\|?\s*((?:B|P)\d{2,8})", text)
    if id_match:
        info.doc_id = id_match.group(1)

    for label, attr in [
        ("执行状态", "status"),
        ("建议等级", "level"),
        ("重要性等级", "level"),
        ("文件类型", "file_type"),
        ("文本完整性", "integrity"),
        ("当前状态", "status"),
    ]:
        match = re.search(rf"(?:\*\*)?{label}(?:\*\*)?\s*[：:|]\s*([^\n|]+)", header)
        if match:
            setattr(info, attr, clean_cell(match.group(1), 240))

    info.summary = extract_summary(text)
    return info


def extract_summary(text: str) -> str:
    candidates = []
    for pattern in [
        r"从全文高频词和关键句看，(.+?)(?:\n\n|$)",
        r"##\s+1\..*?\n\n(.+?)(?:\n\n|$)",
        r"##\s+二、读取结果\s*\n\n(.+?)(?:\n\n|$)",
        r"##\s+三、暂定文献定位\s*\n\n(.+?)(?:\n\n|$)",
    ]:
        match = re.search(pattern, text, re.S)
        if match:
            candidates.append(match.group(1))
    for value in candidates:
        value = re.sub(r"\|.*?\|", " ", value)
        value = re.sub(r"`([^`]+)`", r"\1", value)
        value = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", value)
        value = clean_cell(value, 360)
        if len(value) >= 20:
            return value
    paragraphs = [
        clean_cell(p, 360)
        for p in re.split(r"\n\s*\n", text)
        if p.strip() and not p.lstrip().startswith(("#", "|", "-", "```"))
    ]
    return next((p for p in paragraphs if len(p) >= 20), "")


def classify_themes(text: str) -> list[tuple[str, str, list[str]]]:
    low = text.lower()
    scored: list[tuple[int, str, str, list[str]]] = []
    for theme_id, theme, keywords, _chapter in THEMES:
        matched = []
        score = 0
        for keyword in keywords:
            keyword_low = keyword.lower()
            count = low.count(keyword_low)
            if count:
                matched.append(keyword)
                score += min(count, 8)
        if score:
            scored.append((score, theme_id, theme, matched[:8]))
    scored.sort(key=lambda item: (-item[0], item[1]))
    if not scored:
        return [("TH008", "专题研究", [])]
    return [(theme_id, theme, matched) for _score, theme_id, theme, matched in scored[:3]]


def classify_chapter(text: str, themes: list[tuple[str, str, list[str]]]) -> str:
    low = text.lower()
    best = (0, "第十二章 总结：从作品史到人工世界史")
    for chapter_id, title, keywords in CHAPTERS:
        score = sum(min(low.count(keyword.lower()), 10) for keyword in keywords)
        if score > best[0]:
            best = (score, f"{chapter_id} {title}")
    if best[0] == 0 and themes:
        theme_map = {theme_id: chapter for theme_id, _theme, _keywords, chapter in THEMES}
        return theme_map.get(themes[0][0], best[1])
    return best[1]


def keywords_from_text(text: str, themes: list[tuple[str, str, list[str]]]) -> list[str]:
    words: list[str] = []
    for _theme_id, _theme, matched in themes:
        words.extend(matched)
    for pattern in [
        r"\b[A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+){0,2}\b",
        r"[\u4e00-\u9fff]{2,8}(?:设计|史|理论|方法|文化|建筑|教育|研究|运动|视觉|图像)",
    ]:
        for match in re.findall(pattern, text[:12000]):
            value = clean_cell(match, 60)
            if value.lower() not in {"markdown", "index", "report"} and value not in words:
                words.append(value)
            if len(words) >= 8:
                return words
    return words[:8]


def infer_importance(report: ReportInfo | None, doc_type: str, text: str) -> str:
    if report and "A" in report.level:
        return "A"
    if report and "B" in report.level:
        return "B"
    low = text.lower()
    if any(token in low for token in ("world history of design", "bauhaus", "design history", "设计史", "包豪斯")):
        return "B"
    if "待核" in (report.status if report else "") or "空" in (report.integrity if report else ""):
        return "D"
    if "书目" in doc_type or "封面" in doc_type:
        return "C"
    return "C"


def collect_reports(root: Path, exclude_rules: bool = False) -> tuple[dict[str, ReportInfo], list[ReportInfo]]:
    by_source: dict[str, ReportInfo] = {}
    orphan: list[ReportInfo] = []
    if not root.exists():
        return by_source, orphan
    for path in sorted(powershell_files(root, "*.md")):
        report_path = rel(path)
        if exclude_rules and report_path == RULES_FILE:
            continue
        if path.name in RESULT_DOC_NAMES:
            continue
        info = extract_report_info(path)
        if info.source:
            existing = by_source.get(info.source)
            if not existing or existing.path.endswith("/INDEX.md"):
                by_source[info.source] = info
        else:
            orphan.append(info)
    return by_source, orphan


def fallback_book_report(source_rel: str, reports_by_source: dict[str, ReportInfo]) -> ReportInfo | None:
    if source_rel in reports_by_source:
        return reports_by_source[source_rel]
    mirror = "00-books-result/" + source_rel.removeprefix("00-books/")
    path = ROOT / mirror
    if path.exists():
        info = extract_report_info(path)
        info.source = source_rel
        return info
    return None


def source_doc_id(collection: str, index: int, report: ReportInfo | None, source_path: str) -> str:
    if report and report.doc_id:
        return report.doc_id
    if collection == "paper":
        stem = Path(source_path).stem
        match = re.match(r"^(P\d{2,5})", stem, re.I)
        if match:
            return match.group(1).upper()
        return f"P{index:05d}"
    return f"B{index:05d}"


def build_source_infos() -> tuple[list[SourceInfo], list[ReportInfo], list[dict[str, str]]]:
    book_reports, book_orphans = collect_reports(BOOK_REPORT_ROOT, exclude_rules=True)
    paper_reports, paper_orphans = collect_reports(PAPER_REPORT_ROOT)
    report_orphans = book_orphans + paper_orphans
    docs: list[SourceInfo] = []
    file_rows: list[dict[str, str]] = []

    all_files = [
        p
        for p in sorted(powershell_files(ROOT))
        if ".git" not in p.parts and GENERATED_ROOT not in p.parents
    ]
    for path in all_files:
        data = read_bytes(path)
        text = ""
        heading = ""
        lines = ""
        if path.suffix.lower() in {".md", ".txt", ".csv", ".json", ".py"}:
            try:
                text = data.decode("utf-8-sig", errors="replace")
                heading = first_heading(text)
                lines = str(text.count("\n") + (1 if text else 0))
            except Exception:
                lines = ""
        file_rows.append(
            {
                "path": rel(path),
                "directory": Path(rel(path)).parent.as_posix(),
                "extension": path.suffix.lower(),
                "size_bytes": str(len(data)),
                "sha1": sha1_bytes(data),
                "line_count": lines,
                "first_heading": heading,
            }
        )

    source_paths = [(p, "book") for p in sorted(powershell_files(BOOK_ROOT, "*.md"))] + [
        (p, "paper") for p in sorted(powershell_files(PAPER_ROOT, "*.md")) if p.name != "INDEX.md"
    ]

    counters = Counter()
    for path, collection in source_paths:
        counters[collection] += 1
        data = read_bytes(path)
        text = data.decode("utf-8-sig", errors="replace")
        source_rel = rel(path)
        report = (
            fallback_book_report(source_rel, book_reports)
            if collection == "book"
            else paper_reports.get(source_rel)
        )
        doc_id = source_doc_id(collection, counters[collection], report, source_rel)
        author, title, work_title, year = parse_work_metadata(path, collection)
        doc_type = doc_type_from_path(path, collection, text)
        context = " ".join([source_rel, title, work_title, first_heading(text), text[:20000], report.summary if report else ""])
        themes = classify_themes(context)
        chapter = classify_chapter(context, themes)
        keywords = keywords_from_text(context, themes)
        importance = infer_importance(report, doc_type, context)
        completeness = report.integrity if report else ("未生成深度报告" if collection == "paper" else "报告映射待核")
        teaching_use = "必读 / 框架文献" if importance == "A" else ("重点精读 / 局部使用" if importance == "B" else "选读 / 备查")
        note = ""
        if not text.strip():
            note = "源 Markdown 为空，暂入待核"
            importance = "D"
        elif not report:
            note = "未找到有效深度报告映射"
        docs.append(
            SourceInfo(
                path=source_rel,
                collection=collection,
                doc_id=doc_id,
                author=author,
                title=title,
                work_title=work_title,
                year=year,
                doc_type=doc_type,
                size=len(data),
                chars=len(text),
                lines=text.count("\n") + (1 if text else 0),
                sha1=sha1_bytes(data),
                first_heading=first_heading(text),
                report=report,
                themes=themes,
                chapter=chapter,
                keywords=keywords,
                importance=importance,
                completeness=completeness,
                teaching_use=teaching_use,
                note=note,
            )
        )

    deduplicate_doc_ids(docs)
    return docs, report_orphans, file_rows


def deduplicate_doc_ids(docs: list[SourceInfo]) -> None:
    groups: dict[str, list[SourceInfo]] = defaultdict(list)
    for doc in docs:
        groups[doc.doc_id].append(doc)
    for doc_id, items in groups.items():
        if len(items) <= 1:
            continue
        for number, doc in enumerate(sorted(items, key=lambda item: item.path), 1):
            original_note = doc.note
            doc.doc_id = f"{doc_id}-{number:02d}"
            collision_note = f"原报告编号 {doc_id} 存在重复，中央索引已消歧"
            doc.note = f"{original_note}；{collision_note}" if original_note else collision_note


def build_outputs(docs: list[SourceInfo], report_orphans: list[ReportInfo], file_rows: list[dict[str, str]]) -> None:
    GENERATED_ROOT.mkdir(parents=True, exist_ok=True)

    master_rows = []
    theme_rows = []
    summary_rows = []
    chapter_rows = []
    teaching_rows = []
    report_map_rows = []
    version_rows = []

    for idx, doc in enumerate(docs, 1):
        theme_names = "；".join(f"{theme_id} {theme}" for theme_id, theme, _kw in doc.themes)
        keyword_text = "；".join(doc.keywords)
        report_path = doc.report.path if doc.report else ""
        summary = doc.report.summary if doc.report and doc.report.summary else f"{doc.work_title} / {doc.title}"
        master_rows.append(
            {
                "编号": doc.doc_id,
                "作者": doc.author,
                "译者": "",
                "题名": doc.title,
                "原书名 / 原文题名": doc.work_title,
                "文献类型": doc.doc_type,
                "出版信息": doc.year,
                "ISBN / DOI": "",
                "文件路径": doc.path,
                "报告路径": report_path,
                "主题分类": theme_names,
                "关键词": keyword_text,
                "核心观点": "见深度报告；中央观点索引需逐条复核后入库" if report_path else "待补深度报告",
                "主要内容摘要": summary,
                "适用章节": doc.chapter,
                "可用案例": "见 07 案例候选索引与深度报告",
                "可用概念": "见 05 概念候选索引与深度报告",
                "可引用页码": "Markdown 段落定位；正式页码需回版本核验",
                "教学用途": doc.teaching_use,
                "重要性等级": doc.importance,
                "版本与译本": "待由 10 号索引复核",
                "图片资料": "需由 11 号索引复核图像来源与版权",
                "版权备注": "未做出版授权判断",
                "待补 / 待核": doc.note,
                "备注": f"字符数 {doc.chars}；行数 {doc.lines}",
            }
        )
        for theme_id, theme, matched in doc.themes:
            theme_rows.append(
                {
                    "主题编号": theme_id,
                    "主题类别": theme,
                    "对应文献编号": doc.doc_id,
                    "代表文献路径": doc.path,
                    "报告路径": report_path,
                    "匹配关键词": "；".join(matched),
                    "教材适用章节": doc.chapter,
                    "备注": doc.note,
                }
            )
        summary_rows.append(
            {
                "摘要编号": f"S{idx:05d}",
                "文献编号": doc.doc_id,
                "文献题名": doc.title,
                "核心内容": summary,
                "研究对象": "；".join(theme for _theme_id, theme, _kw in doc.themes),
                "主要观点": "候选观点见报告，入正文前需回源文复核",
                "论证路径": "源 Markdown → 深度报告 → 中央索引候选",
                "重要章节": doc.first_heading,
                "关键词": keyword_text,
                "适用章节": doc.chapter,
                "适用程度": doc.teaching_use,
                "使用价值": "教材写作、备课检索、资料卡建设",
            }
        )
        chapter_rows.append(
            {
                "教材章节": doc.chapter.split(" ", 1)[0],
                "章节主题": doc.chapter.split(" ", 1)[1] if " " in doc.chapter else doc.chapter,
                "可用文献编号": doc.doc_id,
                "文献路径": doc.path,
                "可用观点编号": "待从 04 观点索引分配",
                "可用概念编号": "待从 05 概念索引分配",
                "可用人物编号": "待从 06 人物索引分配",
                "可用案例编号": "待从 07 案例索引分配",
                "图片资料编号": "待从 11 图像索引分配",
                "教学重点": doc.teaching_use,
                "备注": doc.note,
            }
        )
        teaching_rows.append(
            {
                "教学编号": f"TE{idx:05d}",
                "文献编号": doc.doc_id,
                "文献题名": doc.title,
                "教学难度": "高级" if doc.importance == "A" else ("中级" if doc.importance == "B" else "入门 / 备查"),
                "适合对象": "研究生 / 本科高年级" if doc.importance in {"A", "B"} else "本科课程备查",
                "适合用途": doc.teaching_use,
                "是否必读": "是" if doc.importance == "A" else "否",
                "是否推荐阅读": "是" if doc.importance in {"A", "B"} else "否",
                "可设计问题": f"该文献如何支持“{doc.chapter}”的教材论述？",
                "可设计作业": "制作资料卡，标注文献观点、概念、案例和可引用边界",
                "教学提示": "正式讲义引用需回源 Markdown 与版本页码复核",
                "适用章节": doc.chapter,
            }
        )
        report_map_rows.append(
            {
                "文献编号": doc.doc_id,
                "源文件路径": doc.path,
                "报告路径": report_path,
                "映射状态": "mapped" if report_path else "missing_report",
                "报告状态": doc.report.status if doc.report else "",
                "报告等级": doc.report.level if doc.report else "",
                "完整性": doc.completeness,
            }
        )
        version_rows.append(
            {
                "版本编号": f"ED{idx:05d}",
                "文献编号": doc.doc_id,
                "原版出版年份": doc.year,
                "所用版本年份": doc.year,
                "中文译本信息": "待核",
                "不同译本差异": "待核",
                "推荐使用版本": "仓库 Markdown 当前版本",
                "引用页码版本": "Markdown 段落定位；纸本页码待核",
                "备注": doc.path,
            }
        )

    write_csv(GENERATED_ROOT / "repository-file-index.csv", list(file_rows[0].keys()), file_rows)
    write_csv(
        GENERATED_ROOT / "01-total-bibliography-index.csv",
        list(master_rows[0].keys()),
        master_rows,
    )
    write_csv(
        GENERATED_ROOT / "02-theme-index.csv",
        ["主题编号", "主题类别", "对应文献编号", "代表文献路径", "报告路径", "匹配关键词", "教材适用章节", "备注"],
        theme_rows,
    )
    write_csv(
        GENERATED_ROOT / "03-content-summary-index.csv",
        [
            "摘要编号",
            "文献编号",
            "文献题名",
            "核心内容",
            "研究对象",
            "主要观点",
            "论证路径",
            "重要章节",
            "关键词",
            "适用章节",
            "适用程度",
            "使用价值",
        ],
        summary_rows,
    )
    write_csv(
        GENERATED_ROOT / "08-chapter-correspondence-index.csv",
        [
            "教材章节",
            "章节主题",
            "可用文献编号",
            "文献路径",
            "可用观点编号",
            "可用概念编号",
            "可用人物编号",
            "可用案例编号",
            "图片资料编号",
            "教学重点",
            "备注",
        ],
        chapter_rows,
    )
    write_csv(
        GENERATED_ROOT / "09-teaching-function-index.csv",
        [
            "教学编号",
            "文献编号",
            "文献题名",
            "教学难度",
            "适合对象",
            "适合用途",
            "是否必读",
            "是否推荐阅读",
            "可设计问题",
            "可设计作业",
            "教学提示",
            "适用章节",
        ],
        teaching_rows,
    )
    write_csv(
        GENERATED_ROOT / "10-version-translation-citation-index.csv",
        ["版本编号", "文献编号", "原版出版年份", "所用版本年份", "中文译本信息", "不同译本差异", "推荐使用版本", "引用页码版本", "备注"],
        version_rows,
    )
    write_csv(
        GENERATED_ROOT / "source-report-map.csv",
        ["文献编号", "源文件路径", "报告路径", "映射状态", "报告状态", "报告等级", "完整性"],
        report_map_rows,
    )
    orphan_rows = [
        {
            "报告路径": info.path,
            "报告状态": info.status,
            "报告等级": info.level,
            "推断源文件": info.source,
            "字符数": str(info.chars),
            "备注": "未进入中央索引；需先确认源文映射",
        }
        for info in report_orphans
    ]
    write_csv(
        GENERATED_ROOT / "orphan-report-index.csv",
        ["报告路径", "报告状态", "报告等级", "推断源文件", "字符数", "备注"],
        orphan_rows,
    )

    write_markdown_indexes(docs, report_orphans, file_rows)


def top_counter(rows: list[str], limit: int = 20) -> list[tuple[str, int]]:
    return Counter(rows).most_common(limit)


def md_link(path: str) -> str:
    return f"[`{path}`]({path})"


def write_markdown_indexes(docs: list[SourceInfo], report_orphans: list[ReportInfo], file_rows: list[dict[str, str]]) -> None:
    collection_counts = Counter(doc.collection for doc in docs)
    report_mapped = sum(1 for doc in docs if doc.report)
    missing_reports = len(docs) - report_mapped
    theme_counts = Counter(theme for doc in docs for _theme_id, theme, _kw in doc.themes)
    chapter_counts = Counter(doc.chapter for doc in docs)
    importance_counts = Counter(doc.importance for doc in docs)
    extension_counts = Counter(row["extension"] or "[no extension]" for row in file_rows)

    stats = {
        "generated_on": date.today().isoformat(),
        "repository_files": len(file_rows),
        "source_markdown_total": len(docs),
        "book_markdown": collection_counts["book"],
        "paper_markdown": collection_counts["paper"],
        "mapped_reports": report_mapped,
        "missing_reports": missing_reports,
        "orphan_reports": len(report_orphans),
        "importance_counts": dict(importance_counts),
        "theme_counts": dict(theme_counts),
        "chapter_counts": dict(chapter_counts),
    }
    write_text(GENERATED_ROOT / "index-stats.json", json.dumps(stats, ensure_ascii=False, indent=2))

    summary_lines = [
        "# 全仓库教材型索引构建报告",
        "",
        f"- 生成日期：{date.today().isoformat()}",
        f"- 仓库文件总数：{len(file_rows)}",
        f"- 源 Markdown：{len(docs)}（00-books：{collection_counts['book']}；00-Paper：{collection_counts['paper']}）",
        f"- 已映射深度报告：{report_mapped}",
        f"- 缺少深度报告映射：{missing_reports}",
        f"- 未入库孤立报告：{len(report_orphans)}",
        "",
        "## 生成文件",
        "",
        "| 文件 | 内容 |",
        "|---|---|",
        "| `repository-file-index.csv` | 全仓库文件级索引，含路径、扩展名、大小、SHA1、首标题 |",
        "| `01-total-bibliography-index.csv` | 按 12 号综合总表字段生成的全量文献主索引 |",
        "| `02-theme-index.csv` | 按 02 号主题框架生成的文献—主题映射 |",
        "| `03-content-summary-index.csv` | 按 03 号摘要框架生成的报告摘要与用途索引 |",
        "| `08-chapter-correspondence-index.csv` | 按 08 号框架生成的章节对应索引 |",
        "| `09-teaching-function-index.csv` | 按 09 号框架生成的教学功能索引 |",
        "| `10-version-translation-citation-index.csv` | 按 10 号框架生成的版本核验队列 |",
        "| `source-report-map.csv` | 源 Markdown 与深度报告的一一映射表 |",
        "| `orphan-report-index.csv` | 未进入中央索引的无源/孤立报告 |",
        "| `index-stats.json` | 本轮索引统计数据 |",
        "",
        "## 主题分布",
        "",
        "| 主题 | 文献数 |",
        "|---|---:|",
    ]
    summary_lines += [f"| {theme} | {count} |" for theme, count in theme_counts.most_common()]
    summary_lines += [
        "",
        "## 章节分布",
        "",
        "| 教材章节 | 文献数 |",
        "|---|---:|",
    ]
    summary_lines += [f"| {chapter} | {count} |" for chapter, count in chapter_counts.most_common()]
    summary_lines += [
        "",
        "## 重要性等级",
        "",
        "| 等级 | 文献数 |",
        "|---|---:|",
    ]
    summary_lines += [f"| {level} | {count} |" for level, count in sorted(importance_counts.items())]
    summary_lines += [
        "",
        "## 文件类型分布",
        "",
        "| 扩展名 | 文件数 |",
        "|---|---:|",
    ]
    summary_lines += [f"| {ext} | {count} |" for ext, count in extension_counts.most_common(20)]
    summary_lines += [
        "",
        "## 索引边界",
        "",
        "本轮索引已经读取仓库文件与 Markdown 内容，按 `index-system/` 的字段框架建立中央索引入口。观点、概念、人物、案例、图像和可引用页码仍按 `13-report-integration-rules.md` 保持候选状态；进入教材正文前必须回到源 Markdown 与版本页码复核。",
        "",
    ]
    write_text(GENERATED_ROOT / "00-index-build-report.md", "\n".join(summary_lines))

    readme = [
        "# generated",
        "",
        "本目录为自动生成的全仓库教材型索引区，依据 `index-system/01-13` 的字段规则建立。",
        "",
        "- `00-index-build-report.md`：本轮构建摘要。",
        "- `01-total-bibliography-index.csv`：全量文献主索引。",
        "- `repository-file-index.csv`：全仓库文件级索引。",
        "- `source-report-map.csv`：源文与报告映射。",
        "",
        "注意：本目录中的观点、概念、人物、案例、图像和页码均为索引候选入口；正式教材引用仍需回源文复核。",
        "",
    ]
    write_text(GENERATED_ROOT / "README.md", "\n".join(readme))

    directory_lines = [
        "# 全仓库目录级索引",
        "",
        "| 目录 | 文件数 | Markdown | 总大小 MB |",
        "|---|---:|---:|---:|",
    ]
    dir_stats: dict[str, dict[str, int]] = defaultdict(lambda: {"files": 0, "md": 0, "bytes": 0})
    for row in file_rows:
        directory = row["directory"] or "."
        top = directory.split("/", 1)[0]
        dir_stats[top]["files"] += 1
        dir_stats[top]["bytes"] += int(row["size_bytes"])
        if row["extension"] == ".md":
            dir_stats[top]["md"] += 1
    for directory, stat in sorted(dir_stats.items()):
        directory_lines.append(
            f"| `{directory}` | {stat['files']} | {stat['md']} | {stat['bytes'] / 1024 / 1024:.2f} |"
        )
    directory_lines.append("")
    write_text(GENERATED_ROOT / "repository-directory-index.md", "\n".join(directory_lines))


def refresh_readmes() -> None:
    root_index = ROOT / "INDEX.md"
    text = read_text(root_index)
    marker = "\n## 八、自动生成索引\n"
    generated_section = f"""
## 八、自动生成索引

最近一次全仓库索引已根据 `index-system/` 的字段框架生成，入口位于 [`index-system/generated/`](index-system/generated/)。

| 文件 | 用途 |
|---|---|
| [`00-index-build-report.md`](index-system/generated/00-index-build-report.md) | 本轮索引构建摘要、统计与边界说明 |
| [`01-total-bibliography-index.csv`](index-system/generated/01-total-bibliography-index.csv) | 全量文献主索引 |
| [`repository-file-index.csv`](index-system/generated/repository-file-index.csv) | 全仓库文件级索引 |
| [`source-report-map.csv`](index-system/generated/source-report-map.csv) | 源 Markdown 与深度报告映射 |

该索引层不替代原文核验；观点、概念、人物、案例、图像和页码进入正文前仍需按 `13-report-integration-rules.md` 复核。
"""
    if marker in text:
        text = text.split(marker, 1)[0] + generated_section
    else:
        text = text.rstrip() + "\n" + generated_section
    write_text(root_index, text)

    system_readme = INDEX_ROOT / "README.md"
    text = read_text(system_readme)
    marker = "\n## 六、自动生成索引区\n"
    generated_section = f"""
## 六、自动生成索引区

`generated/` 为本索引系统的自动生成结果区，用于承接全仓库扫描、源文—报告映射和教材型中央索引。

| 文件 | 内容 |
|---|---|
| [`generated/00-index-build-report.md`](generated/00-index-build-report.md) | 构建报告与统计 |
| [`generated/01-total-bibliography-index.csv`](generated/01-total-bibliography-index.csv) | 01 总文献索引的全量数据版 |
| [`generated/02-theme-index.csv`](generated/02-theme-index.csv) | 02 主题索引的全量数据版 |
| [`generated/03-content-summary-index.csv`](generated/03-content-summary-index.csv) | 03 内容摘要索引的全量数据版 |
| [`generated/08-chapter-correspondence-index.csv`](generated/08-chapter-correspondence-index.csv) | 08 章节对应索引的全量数据版 |
| [`generated/09-teaching-function-index.csv`](generated/09-teaching-function-index.csv) | 09 教学功能索引的全量数据版 |
| [`generated/10-version-translation-citation-index.csv`](generated/10-version-translation-citation-index.csv) | 10 版本与页码核验队列 |
| [`generated/repository-file-index.csv`](generated/repository-file-index.csv) | 全仓库文件级索引 |
| [`generated/source-report-map.csv`](generated/source-report-map.csv) | 源文与深度报告映射 |

自动生成表只负责建立检索入口和候选关系；全局观点、概念、人物、案例、图像和引文编号仍按 04—11 号索引逐步人工复核入库。
"""
    if marker in text:
        text = text.split(marker, 1)[0] + generated_section
    else:
        text = text.rstrip() + "\n" + generated_section
    write_text(system_readme, text)


def main() -> None:
    docs, report_orphans, file_rows = build_source_infos()
    build_outputs(docs, report_orphans, file_rows)
    refresh_readmes()
    print(
        json.dumps(
            {
                "source_docs": len(docs),
                "files": len(file_rows),
                "mapped_reports": sum(1 for doc in docs if doc.report),
                "missing_reports": sum(1 for doc in docs if not doc.report),
                "orphan_reports": len(report_orphans),
                "generated": rel(GENERATED_ROOT),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
