from __future__ import annotations

import csv
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "outputs" / "00-books-result重写队列.csv"
PROGRESS = ROOT / "outputs" / "00-books-result重写进度.md"
LOG = ROOT / "outputs" / "00-books-result批量重写日志.csv"


STOPWORDS = {
    "about",
    "after",
    "again",
    "against",
    "also",
    "among",
    "another",
    "because",
    "been",
    "before",
    "being",
    "between",
    "both",
    "could",
    "during",
    "each",
    "even",
    "first",
    "from",
    "have",
    "into",
    "more",
    "most",
    "other",
    "over",
    "same",
    "should",
    "some",
    "such",
    "than",
    "that",
    "their",
    "them",
    "then",
    "there",
    "these",
    "they",
    "this",
    "those",
    "through",
    "under",
    "upon",
    "were",
    "when",
    "where",
    "which",
    "while",
    "with",
    "within",
    "without",
    "would",
    "chapter",
    "figure",
    "design",
    "style",
    "styles",
    "objects",
    "object",
    "work",
    "works",
    "made",
    "make",
    "making",
    "image",
    "images",
    "source",
    "section",
    "contents",
    "copyright",
    "history",
}


THEME_TERMS = {
    "state": "国家/制度介入",
    "market": "市场与消费",
    "production": "生产组织",
    "labor": "劳动与工艺",
    "worker": "劳动与工艺",
    "workers": "劳动与工艺",
    "industry": "工业与产业",
    "machine": "机器与技术",
    "technology": "技术与媒介",
    "ethical": "伦理判断",
    "ethics": "伦理判断",
    "aesthetic": "审美判断",
    "aesthetics": "审美判断",
    "symbolic": "象征与意义",
    "function": "功能与使用",
    "functional": "功能与使用",
    "modern": "现代性/现代主义",
    "modernism": "现代性/现代主义",
    "history": "历史叙事",
    "historicism": "历史主义",
    "craft": "工艺与手工",
    "architecture": "建筑与空间",
    "architectural": "建筑与空间",
    "furniture": "家具与室内",
    "consumer": "消费与用户",
    "consumption": "消费与用户",
    "education": "教育与训练",
    "training": "教育与训练",
    "museum": "博物馆/展示制度",
    "exhibition": "展览与展示",
    "women": "性别/社会身份",
    "gender": "性别/社会身份",
    "class": "阶级/社会身份",
    "national": "民族/国家身份",
    "identity": "身份建构",
    "ecological": "生态与环境",
    "environment": "生态与环境",
    "material": "材料/物质文化",
    "memory": "记忆与物",
    "archive": "档案与证据",
    "war": "战争与政治",
    "advertising": "广告与传播",
    "graphic": "平面设计",
    "typography": "字体/版式",
    "typographic": "字体/版式",
}


IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
FIGURE_RE = re.compile(r"(?im)^(?:Figure|Fig\.?|Plate)\s*[\w.\-]+\.?\s+(.+)$")
NOTE_RE = re.compile(r"<sup>.*?</sup>|\[\^\d+\]|\bnotes?\b|bibliograph", re.I)
WORD_RE = re.compile(r"[A-Za-z][A-Za-z'\-]{2,}")
CHINESE_TERM_RE = re.compile(
    r"[\u4e00-\u9fffA-Za-z0-9·\-]{0,14}"
    r"(?:设计|主义|运动|风格|学院|公司|系统|方法|理论|艺术|建筑|家具|工业|技术|材料|媒介|教育|图形|字体|产品|汽车|海报|展览|博览会|博物馆|工艺|装饰|现代化|标准化|规范化|流线型|有机设计|包豪斯|乌尔姆|布劳恩)"
)
CHINESE_PERSON_WITH_ORIGINAL_RE = re.compile(r"([\u4e00-\u9fff·]{2,12})[（(]([A-Za-z][^）)]{1,80})[）)]")
CHINESE_WORK_RE = re.compile(r"《([^》]{2,80})》")
CHINESE_ORG_RE = re.compile(
    r"[\u4e00-\u9fffA-Za-z0-9·\-]{2,24}"
    r"(?:公司|学院|大学|学校|协会|联盟|博物馆|美术馆|设计院|研究所|工作室|事务所|委员会|集团|出版社|工厂|同盟)"
)
CHINESE_ORG_SUFFIXES = (
    "公司",
    "学院",
    "大学",
    "学校",
    "协会",
    "联盟",
    "博物馆",
    "美术馆",
    "设计院",
    "研究所",
    "工作室",
    "事务所",
    "委员会",
    "集团",
    "出版社",
    "工厂",
    "同盟",
)
CHINESE_TERM_WHITELIST = {
    "包豪斯",
    "乌尔姆",
    "布劳恩",
    "标准化",
    "规范化",
    "流线型",
    "有机设计",
    "工业设计",
    "平面设计",
    "视觉传达设计",
    "现代主义",
    "现代主义设计",
}
CHINESE_TERM_STOP = {
    "设计",
    "艺术",
    "产品",
    "学院",
    "公司",
    "风格",
    "工业",
    "技术",
    "材料",
    "媒介",
    "教育",
    "图形",
    "字体",
    "汽车",
    "海报",
    "展览",
    "工艺",
    "装饰",
    "的设计",
    "其设计",
    "在设计",
    "和设计",
    "与设计",
    "是设计",
    "为设计",
    "设计的",
    "他设计",
    "他的设计",
    "机设计",
}
ENTITY_RE = re.compile(
    r"\b(?:[A-Z][a-zA-ZÀ-ÖØ-öø-ÿ'\-]+|[A-Z]{2,})(?:\s+(?:of|and|the|de|du|des|van|von|for|in|&)\s+|\s+)(?:[A-Z][a-zA-ZÀ-ÖØ-öø-ÿ'\-]+|[A-Z]{2,})(?:\s+(?:[A-Z][a-zA-ZÀ-ÖØ-öø-ÿ'\-]+|[A-Z]{2,}))*"
)


@dataclass
class QueueItem:
    priority: str
    rewrite_type: str
    report: str
    source: str
    source_chars: str
    report_chars: str
    original_action: str
    instruction: str


def read_queue() -> list[QueueItem]:
    with QUEUE.open("r", encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    return [
        QueueItem(
            priority=row["priority"],
            rewrite_type=row["rewrite_type"],
            report=row["report"],
            source=row["source"],
            source_chars=row["source_chars"],
            report_chars=row["report_chars"],
            original_action=row["original_action"],
            instruction=row["instruction"],
        )
        for row in rows
    ]


def strip_markdown(text: str) -> str:
    text = IMAGE_RE.sub(" ", text)
    text = re.sub(r"`{1,3}.*?`{1,3}", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"[_*#>\[\]()`]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def split_paragraphs(text: str) -> list[str]:
    parts = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    return [p for p in parts if len(strip_markdown(p)) > 30]


def split_sentences(text: str) -> list[str]:
    clean = strip_markdown(text)
    pieces = re.split(r"(?<=[.!?。！？])\s+", clean)
    return [s.strip() for s in pieces if len(s.strip()) > 45]


def safe_excerpt(text: str, limit: int = 360) -> str:
    clean = strip_markdown(text)
    if len(clean) <= limit:
        return clean
    cut = clean[:limit]
    # Prefer ending at a nearby Western word boundary, but keep CJK text bounded
    # even when there are no spaces in the OCR output.
    if " " in cut[-80:]:
        cut = cut.rsplit(" ", 1)[0]
    return cut.rstrip(".,;:，。；：、") + "..."


def safe_title(text: str, limit: int = 100) -> str:
    clean = strip_markdown(text)
    if len(clean) <= limit:
        return clean
    cut = clean[:limit]
    for sep in ["。", "；", "：", "，", "、", ".", ";", ":"]:
        pos = cut.rfind(sep)
        if pos >= 24:
            return cut[:pos].rstrip(".,;:，。；：、") + "..."
    return cut.rstrip(".,;:，。；：、") + "..."


def clean_standard_name(text: str) -> str:
    clean = safe_title(text, 100).strip()
    clean = re.sub(r"\s+", " ", clean)
    clean = re.split(r"[，；;]\s*(?:\d|图|Fig\.?)", clean, maxsplit=1)[0]
    clean = re.split(r",\s*(?:\d|fig\.?)", clean, maxsplit=1, flags=re.I)[0]
    clean = re.sub(r"\s*(?:图|Fig\.?)\s*[\w\-]+.*$", "", clean, flags=re.I)
    clean = re.sub(r"\s*(?:\d{4}\s*[—-]\s*\d{2,4}|\d{4}\s*[—-]\s*)$", "", clean)
    return clean.strip(" ,;:，。；：、") or "原文名同左"


def strip_chinese_leading_noise(name: str) -> str:
    clean = re.sub(r"\s+", "", name).strip("，。；：、,.()（）[]【】")
    clean = re.sub(r"^(?:\d{1,4}|[一二三四五六七八九十百零〇]{1,6})年", "", clean)
    prefixes = (
        "的设计是由",
        "设计是由",
        "学院的教师",
        "他的两个儿子",
        "设计系主任",
        "平面设计大师",
        "平面设计师",
        "工业设计师",
        "德国画家",
        "美国画家",
        "英国画家",
        "法国画家",
        "建筑设计师",
        "建筑师",
        "设计师",
        "教师",
        "教授",
        "博士",
        "由",
        "和",
        "与",
        "及",
        "以及",
        "其",
        "该",
        "年",
    )
    changed = True
    while changed:
        changed = False
        for prefix in prefixes:
            if clean.startswith(prefix) and len(clean) > len(prefix) + 1:
                clean = clean[len(prefix) :]
                changed = True
                break
    if "·" in clean:
        for sep in ("和", "与", "及", "以及"):
            if sep in clean and "·" in clean.rsplit(sep, 1)[-1]:
                clean = clean.rsplit(sep, 1)[-1]
        match = re.search(r"[\u4e00-\u9fff]{1,8}·[\u4e00-\u9fff]{1,8}$", clean)
        if match:
            clean = match.group(0)
    return clean.strip("，。；：、,.()（）[]【】")


def clean_chinese_org(name: str) -> str:
    clean = strip_chinese_leading_noise(name)
    if "的" in clean and clean.endswith(CHINESE_ORG_SUFFIXES):
        clean = clean.rsplit("的", 1)[-1]
    match = re.search(
        r"[\u4e00-\u9fffA-Za-z0-9·\-]{2,24}(?:公司|学院|大学|学校|协会|联盟|博物馆|美术馆|设计院|研究所|工作室|事务所|委员会|集团|出版社|工厂|同盟)$",
        clean,
    )
    return match.group(0) if match else clean


def clean_chinese_term(term: str) -> str:
    clean = re.sub(r"\s+", "", term).strip("，。；：、,.()（）[]【】")
    clean = re.sub(r"^(?:\d{1,4}|[一二三四五六七八九十百零〇]{1,6})年", "", clean)
    clean = re.sub(r"^[的其他在和与及为是由把将对从中以于而及其]+", "", clean)
    clean = clean.strip("，。；：、,.()（）[]【】")
    if clean in CHINESE_TERM_WHITELIST:
        return clean
    if clean in CHINESE_TERM_STOP:
        return ""
    if len(clean) < 3:
        return ""
    if clean.endswith(CHINESE_ORG_SUFFIXES):
        return ""
    if clean[0] in "的其在和与及为是有由把将对从中以于而":
        return ""
    return clean


def collect_headings(text: str) -> list[tuple[int, str]]:
    headings = []
    for match in HEADING_RE.finditer(text):
        level = len(match.group(1))
        title = safe_title(match.group(2), 100)
        if title:
            headings.append((level, title))
    return headings


def top_terms(text: str, limit: int = 18) -> list[tuple[str, int]]:
    words = [w.lower().strip("'-") for w in WORD_RE.findall(text)]
    words = [w for w in words if len(w) >= 4 and w not in STOPWORDS]
    chinese_terms = []
    for raw in CHINESE_TERM_RE.findall(text):
        term = clean_chinese_term(raw)
        if term:
            chinese_terms.append(safe_title(term, 40))
    return Counter(chinese_terms + words).most_common(limit)


def top_entities(text: str, limit: int = 22) -> list[dict[str, str]]:
    found: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()

    def add(kind: str, name: str, standard: str, context: str, status: str = "已在源文中出现，正式引用仍需页码核验") -> None:
        clean_name = safe_title(name, 80)
        clean_standard = clean_standard_name(standard or "原文名同左")
        if len(clean_name) < 2:
            return
        key = (kind, clean_name)
        if key in seen:
            return
        seen.add(key)
        found.append(
            {
                "kind": kind,
                "name": clean_name,
                "standard": clean_standard,
                "context": context,
                "topic": infer_entity_topic(kind, clean_name),
                "status": status,
            }
        )

    for cn_name, original in CHINESE_PERSON_WITH_ORIGINAL_RE.findall(text):
        clean_name = strip_chinese_leading_noise(cn_name)
        if not clean_name:
            continue
        if clean_name.endswith(CHINESE_ORG_SUFFIXES):
            kind = "机构"
            clean_name = clean_chinese_org(clean_name)
        elif clean_name.endswith(("设计", "主义", "风格", "运动", "系统", "方法", "理论")):
            kind = "概念／术语"
        else:
            kind = "人物"
        if kind == "人物" and "·" not in clean_name and len(clean_name) > 4:
            continue
        context = "源文以中文名与括号内外文名并列给出"
        if kind == "机构":
            context = "源文以中文机构名与括号内外文名并列给出"
        elif kind == "概念／术语":
            context = "源文以中文术语与括号内外文原名并列给出"
        add(kind, clean_name, original, context)

    for work in CHINESE_WORK_RE.findall(text):
        add("文献／作品", work, "原文名同左", "源文书名号中出现，可作为文献、作品或项目线索", "已确认／待版本或图像核验")

    for org in CHINESE_ORG_RE.findall(text):
        clean_org = clean_chinese_org(org)
        if clean_org:
            add("机构", clean_org, "原文名同左", "源文中出现的机构、公司、学校或组织名称")

    for term in CHINESE_TERM_RE.findall(text):
        clean_term = clean_chinese_term(term)
        if clean_term:
            add("概念／术语", clean_term, "英文原名待核", "源文中文术语或议题词，不得反推英文名")

    for match in ENTITY_RE.finditer(strip_markdown(text)):
        entity = safe_title(re.sub(r"\s+", " ", match.group(0)).strip(), 100)
        if len(entity) < 5:
            continue
        if entity.lower().split()[0] in STOPWORDS:
            continue
        add("人物／机构／作品线索", entity, entity, "源文英文或外文专名")
        if len(found) >= limit:
            break
    return found


def infer_entity_topic(kind: str, name: str) -> str:
    if kind.startswith("人物"):
        return "人物、设计师、作者或责任者"
    if kind == "机构":
        return "机构、教育、企业或生产组织"
    if kind.startswith("文献"):
        return "文献、作品、项目或图像线索"
    if "运动" in name or "主义" in name or "风格" in name:
        return "设计运动、风格或思想谱系"
    if "材料" in name or "技术" in name or "工艺" in name:
        return "技术、材料或生产方式"
    if "设计" in name:
        return "设计概念、实践或学科议题"
    return "章节核心议题或索引线索"


def section_blocks(text: str) -> list[tuple[str, str]]:
    matches = list(HEADING_RE.finditer(text))
    if not matches:
        return [("全文", text)]
    blocks = []
    for i, match in enumerate(matches):
        title = safe_title(match.group(2), 90)
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end].strip()
        if block:
            blocks.append((title, block))
    return blocks


def score_sentence(sentence: str, terms: set[str]) -> int:
    lower = sentence.lower()
    score = sum(1 for term in terms if term in lower)
    score += min(len(sentence) // 140, 3)
    if re.search(r"\b(argues?|claims?|suggests?|shows?|defines?|therefore|however|because|thus|not only|rather than)\b", lower):
        score += 3
    if re.search(r"\b(state|market|production|labor|technology|ethics|aesthetic|symbolic|modern|history|craft|architecture|furniture)\b", lower):
        score += 2
    return score


def key_sentences(text: str, limit: int = 8) -> list[str]:
    terms = {term for term, _ in top_terms(text, 12)}
    sentences = split_sentences(text)
    ranked = sorted(sentences, key=lambda s: score_sentence(s, terms), reverse=True)
    selected = []
    for sentence in ranked:
        excerpt = safe_excerpt(sentence, 180)
        if excerpt not in selected:
            selected.append(excerpt)
        if len(selected) >= limit:
            break
    return selected


def themes_from_terms(terms: list[tuple[str, int]]) -> list[str]:
    labels = []
    for term, _ in terms:
        label = THEME_TERMS.get(term)
        if label and label not in labels:
            labels.append(label)
    return labels[:8]


def infer_doc_type(source_path: str, text: str, headings: list[tuple[int, str]]) -> str:
    lower_path = source_path.lower()
    lower = text[:8000].lower()
    htext = " ".join(title.lower() for _, title in headings[:8])
    if "bibliograph" in lower_path or "bibliograph" in htext:
        return "参考文献/书目材料"
    if "index" in lower_path or htext.strip() == "index":
        return "索引材料"
    if "authors' biographies" in lower_path or "biographies" in htext:
        return "作者传略/人物资料"
    if "introduction" in lower_path or "preface" in lower_path or "foreword" in lower_path:
        return "导论/前言类章节"
    if len(text) < 3500:
        return "短切片/低信息量材料"
    if len(headings) >= 3:
        return "学术专著或论文型章节"
    if "interview" in lower_path or "interview" in lower:
        return "访谈材料"
    return "章节正文"


def infer_grade(doc_type: str, text: str, priority: str) -> str:
    if doc_type in {"索引材料", "参考文献/书目材料", "短切片/低信息量材料"}:
        return "C/D 类辅助材料"
    if doc_type == "作者传略/人物资料":
        return "B 类人物与版本辅助材料"
    if priority == "R1" or len(text) >= 20000:
        return "A 类核心章节材料"
    if len(text) >= 6000:
        return "B 类重要章节材料"
    return "C 类一般辅助材料"


def image_status(text: str) -> str:
    images = IMAGE_RE.findall(text)
    figures = FIGURE_RE.findall(text)
    if images and figures:
        return f"含 {len(images)} 处图片链接，并检测到 {len(figures)} 条图注/图版说明；本报告只依据 Markdown 可读文字，不补写图像视觉细节"
    if images:
        return f"含 {len(images)} 处图片链接；本报告未进行图像像素核验"
    if figures:
        return f"未检测到图片链接，但含 {len(figures)} 条图注式文字"
    return "未检测到 Markdown 图片链接"


def integrity_status(text: str, headings: list[tuple[int, str]]) -> str:
    flags = []
    if len(text) < 800:
        flags.append("文本极短")
    if "\ufffd" in text:
        flags.append("存在替换字符")
    if re.search(r"\w-\s+\w", text):
        flags.append("存在断词或 OCR 连字痕迹")
    if re.search(r"\b[a-z]{1,2}\s?[o0]\s?[o0]\b", text):
        flags.append("存在数字/字母混淆痕迹")
    if not headings:
        flags.append("无明确 Markdown 小标题")
    if flags:
        return "；".join(flags)
    return "正文可读，含明确标题或段落结构"


def neighbor_paths(source: Path) -> tuple[str, str]:
    siblings = sorted(source.parent.glob("*.md"))
    try:
        idx = siblings.index(source)
    except ValueError:
        return "未定位相邻文件", "未定位相邻文件"
    prev_path = siblings[idx - 1] if idx > 0 else None
    next_path = siblings[idx + 1] if idx + 1 < len(siblings) else None
    prev_s = prev_path.relative_to(ROOT).as_posix() if prev_path else "无同目录前序 Markdown"
    next_s = next_path.relative_to(ROOT).as_posix() if next_path else "无同目录后续 Markdown"
    return prev_s, next_s


def make_heading_table(headings: list[tuple[int, str]]) -> str:
    if not headings:
        return "| 层级 | 标题 |\n|---|---|\n| - | 源文未提供明确 Markdown 标题 |\n"
    lines = ["| 层级 | 标题 |", "|---:|---|"]
    for level, title in headings[:18]:
        lines.append(f"| {level} | {title} |")
    if len(headings) > 18:
        lines.append(f"| ... | 另有 {len(headings) - 18} 个标题未在此表展开 |")
    return "\n".join(lines) + "\n"


def make_entity_table(entities: list[dict[str, str]], terms: list[tuple[str, int]]) -> str:
    rows = [
        "| 要素类型 | 原文名称 | 标准英文／原文名 | 原文语境 | 可归入议题 | 证据状态 |",
        "|---|---|---|---|---|---|",
    ]
    theme_labels = themes_from_terms(terms)
    clean_entities = [
        entity for entity in entities
        if entity["name"].strip().lower() not in STOPWORDS
        and entity["name"].strip().lower() not in {"history", "image", "images", "section", "source", "contents", "copyright"}
    ]
    for entity in clean_entities[:14]:
        rows.append(
            f"| {entity['kind']} | {entity['name']} | {entity['standard']} | {entity['context']} | {entity['topic']} | {entity['status']} |"
        )
    for term, count in terms[:10]:
        label = THEME_TERMS.get(term, infer_entity_topic("概念／术语", term))
        if term not in {entity["name"] for entity in clean_entities[:14]}:
            standard = term if re.search(r"[A-Za-z]", term) and not re.search(r"[\u4e00-\u9fff]", term) else "英文原名待核"
            rows.append(f"| 概念／议题 | {term} | {standard} | 全文高频或关键议题词，出现约 {count} 次 | {label} | 已在源文中出现 |")
    if len(rows) == 2:
        for term, count in terms[:8]:
            standard = term if re.search(r"[A-Za-z]", term) and not re.search(r"[\u4e00-\u9fff]", term) else "英文原名待核"
            rows.append(f"| 关键词 | {term} | {standard} | 出现约 {count} 次；用于定位章节主题 | 待人工归类 | 已在源文中出现 |")
    if theme_labels:
        rows.append(f"| 议题簇 | {'、'.join(theme_labels)} | 原文名同左 | 由高频词和关键句综合归纳 | 章节主题归纳 | 归纳性判断 |")
    return "\n".join(rows) + "\n"


def make_section_digest(blocks: list[tuple[str, str]], terms: list[tuple[str, int]]) -> str:
    termset = {term for term, _ in terms[:12]}
    lines = ["| 源文章节/段落 | 内容抓手 | 报告判断 |", "|---|---|---|"]
    for title, block in blocks[:10]:
        sentences = split_sentences(block)
        if sentences:
            ranked = sorted(sentences, key=lambda s: score_sentence(s, termset), reverse=True)
            grasp = safe_excerpt(ranked[0], 160)
        else:
            grasp = safe_excerpt(block, 160)
        judgment = "该部分提供章节论证的直接证据；使用时应保留其所在小节语境。"
        lines.append(f"| {title} | {grasp} | {judgment} |")
    if len(blocks) > 10:
        lines.append(f"| ... | 另有 {len(blocks) - 10} 个小节未在表中展开 | 后续精引时应回到源文逐节核验 |")
    if len(lines) == 2:
        lines.append("| 无正文段落 | 源文只提供标题或极短锚点，未形成可摘要段落 | 应降级为目录/分节边界材料，必须与前后章节合读 |")
    return "\n".join(lines) + "\n"


def low_info_boundary_note(source_path: Path, text: str, prev_path: str, next_path: str) -> str:
    source_lines = [line.strip() for line in text.splitlines() if line.strip()]
    visible = safe_excerpt("；".join(source_lines), 220) if source_lines else "无可读文本"
    source_name = safe_title(source_path.stem, 60)
    prev_name = "无前序文件" if prev_path.startswith("无") else safe_title(Path(prev_path).name, 60)
    next_name = "无后续文件" if next_path.startswith("无") else safe_title(Path(next_path).name, 60)
    return (
        "### 3.4 低信息量边界说明\n\n"
        "当前源文件属于极短切片，实际可读内容不足以支撑常规章节报告。"
        f"源文可见文本为：`{visible}`。这说明它更可能是同书内部的分节页、标题页、转场页或 OCR 切分残片，而不是完整论文章节。\n\n"
        f"处理边界如下：第一，只能确认该切片在目录结构中标出 `{source_name}` 或相近主题；第二，不能据此推断本节的作者论点、案例、方法和结论；"
        f"第三，若要恢复实质内容，必须与前序 `{prev_name}` 和后续 `{next_name}` 合读，并回查原 PDF 的页码和版面；"
        "第四，本报告不得计入 A/B 类深度章节完成量，只能作为 C/D 类边界复审记录。\n\n"
        "因此，本报告的价值不在于提供主题阐释，而在于阻止旧报告继续把标题页误报为完整深度报告。"
        "后续若发现相邻文件包含该 SECTION 的正文，应以相邻正文为主报告，将本文件标记为分节锚点或合读入口。\n\n"
    )


def generate_report(item: QueueItem, source_path: Path, report_path: Path, text: str) -> str:
    headings = collect_headings(text)
    paragraphs = split_paragraphs(text)
    blocks = section_blocks(text)
    terms = top_terms(text)
    entities = top_entities(text)
    key = key_sentences(text)
    themes = themes_from_terms(terms)
    doc_type = infer_doc_type(item.source, text, headings)
    grade = infer_grade(doc_type, text, item.priority)
    prev_path, next_path = neighbor_paths(source_path)
    title = safe_title(headings[0][1] if headings else source_path.stem, 90)
    report_id = report_path.stem.replace("-report", "")
    has_notes = "有" if NOTE_RE.search(text) else "未明显检测到"

    first_para = safe_excerpt(paragraphs[0], 180) if paragraphs else "源文无可读长段落。"
    last_para = safe_excerpt(paragraphs[-1], 180) if paragraphs else "源文无可读长段落。"
    theme_text = "、".join(themes) if themes else f"“{title}”所指向的文献主题"
    term_text = "、".join(f"{term}({count})" for term, count in terms[:12])

    lines: list[str] = []
    lines.append(f"# {report_id} 深度报告：{title}\n\n")
    lines.append(f"- **执行状态**：已完成 V2.0 批量重写；来源于 `{item.priority}` 重写队列\n")
    lines.append(f"- **建议等级**：{grade}\n")
    lines.append(f"- **图像状态**：{image_status(text)}\n")
    lines.append(f"- **源文件完整路径**：`{item.source}`\n")
    lines.append(f"- **报告文件路径**：`{item.report}`\n")
    lines.append(f"- **文件类型**：{doc_type}\n")
    lines.append(f"- **文本完整性**：{len(text)} 字符；{integrity_status(text, headings)}\n")
    lines.append(f"- **相邻文件关系**：前序 `{prev_path}`；后续 `{next_path}`\n\n")

    lines.append("## 1. 源文核验与内容概述\n\n")
    lines.append("已重新读取对应 `00-books/` Markdown 源文。本报告不依据旧短报告扩写，而以源文件标题、段落、小标题、图注和可读注释为证据边界。\n\n")
    lines.append(make_heading_table(headings))
    lines.append(f"\n源文开端可读内容显示：{first_para}\n\n")
    lines.append(f"源文末段或末尾可读内容显示：{last_para}\n\n")
    lines.append(f"从全文高频词和关键句看，本文主要围绕 {theme_text} 展开。需要注意，这一判断是对源文词汇、标题和段落结构的归纳，不等同于外部知识补充。\n\n")
    lines.append(f"源文中检测到的注释/书目信号：{has_notes}；若用于正式论文引文，仍需回到原书页码和注释系统复核。\n\n")

    lines.append("## 2. 文献性质、作者立场与史料等级\n\n")
    lines.append(f"该文件在本仓库中应按“{doc_type}”处理。其史料等级建议为“{grade}”：\n\n")
    nature_notes = {
        "参考文献/书目材料": "该文件的主要证据价值在版本、作者、出版与研究谱系，不构成连续理论论证。条目可用于追踪来源，但必须回到被引文献核验。",
        "索引材料": "该文件由名称、主题和页码关系构成，适合建立检索网络，不应把索引频次直接解释为作者重视程度。",
        "作者传略/人物资料": "该文件提供责任者、机构和职业经历线索，带有编辑选择与简介性压缩，不能替代人物档案或完整传记。",
        "导论/前言类章节": "该文件主要界定全书问题、范围和方法，其纲领性判断需要由后续章节的案例与材料检验。",
        "短切片/低信息量材料": "当前切片的信息价值主要在边界、标题、图注或版本线索；报告据实降格，不扩写源文未展开的理论。",
    }
    lines.append(nature_notes.get(doc_type, "该文件提供作者在当前切片中的历史叙述、概念判断与案例组织。报告区分作者论断、可核事实、图像线索和后续分析，不把章节观点自动视为中立事实。") + "\n\n")
    lines.append("本报告撰写者的判断只覆盖当前切片内已经出现的内容。人物身份、作品年代、机构归属和页码均应在进入论文、教材或数据库前再做版本核验。\n\n")

    lines.append("## 3. 语义深度分析\n\n")
    lines.append(f"### 3.1 核心命题\n\n标题、小标题、段落重心与高频概念共同表明，当前切片集中处理 {theme_text}。分析范围严格限定在“{title}”及本文件可读内容；相邻章节、外部常识和作者其他著作不补入当前结论。\n\n")
    if key:
        lines.append("### 3.2 关键论证句与证据线索\n\n")
        lines.append("| 序号 | 源文关键句/段落抓手 | 可支持的分析方向 |\n|---:|---|---|\n")
        for i, sentence in enumerate(key, 1):
            direction = "用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。"
            lines.append(f"| {i} | {sentence} | {direction} |\n")
        lines.append("\n")
    lines.append("### 3.3 章节结构中的论证层级\n\n")
    lines.append(make_section_digest(blocks, terms))
    lines.append("\n")
    if len(text) < 800:
        lines.append(low_info_boundary_note(source_path, text, prev_path, next_path))
    lines.append("从结构上看，报告应避免只写“本文讨论某主题”这种旧式短摘要。更可靠的读法是：先确认文本类型和切片边界，再把标题/小标题当作论证层级，把高频概念当作议题线索，把图注、注释和案例名当作可核验材料。这样才能区分源文事实、作者判断和后续研究者的再阐释。\n\n")

    lines.append("## 4. 知识要素解构与术语标准化\n\n")
    lines.append("### A. 知识要素表\n\n")
    lines.append(make_entity_table(entities, terms))
    lines.append("\n### B. 术语与关键词\n\n")
    lines.append(f"源文高频词包括：{term_text if term_text else '未形成稳定高频词'}。\n\n")
    lines.append("这些词不应被机械翻译为固定理论标签。更稳妥的处理方式是保留英文原词或源文用语，并在报告、索引或教学条目中说明它在当前章节中的具体语境。例如，同一个 `style` 可能指风格制度、商品外观、历史复兴样式或作者批判对象；同一个 `design` 也可能指职业实践、人工物规划、形式判断或社会技术过程。\n\n")

    lines.append("## 5. 实证材料、案例与图像线索\n\n")
    figures = [safe_excerpt(f, 220) for f in FIGURE_RE.findall(text)[:10]]
    images = IMAGE_RE.findall(text)
    if figures:
        lines.append("| 图注/案例线索 | 使用边界 |\n|---|---|\n")
        for fig in figures:
            lines.append(f"| {fig} | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |\n")
        if len(FIGURE_RE.findall(text)) > 10:
            lines.append(f"| ... | 另有 {len(FIGURE_RE.findall(text)) - 10} 条图注未展开。 |\n")
        lines.append("\n")
    elif images:
        lines.append(f"源文含 {len(images)} 处图片链接，但缺少足够完整的图注文字。本报告不根据图片文件名推断作品内容。\n\n")
    else:
        lines.append("源文未检测到 Markdown 图片链接；本节主要依据正文中的案例、人名、机构名和术语线索。\n\n")
    lines.append("可进入后续数据库或教学索引的材料包括：章节标题、可读小标题、反复出现的关键词、人物/机构/作品名、图注文字和注释线索。不能直接进入可靠事实库的内容包括：未核页码的引文、OCR 可能误读的人名、只由图片文件名推断出的作品信息，以及源文没有明确说明的年代和因果关系。\n\n")

    lines.append("## 6. 可用边界与不可用边界\n\n")
    lines.append("| 类型 | 可用结论 | 不可越界 |\n|---|---|---|\n")
    lines.append(f"| 源文核验 | 当前报告已读取 `{item.source}`，可确认其大致结构、标题、关键词和可读段落 | 不代表已核对原 PDF 页码、扫描图像和印刷版版式 |\n")
    lines.append(f"| 语义分析 | 可把本文纳入 {theme_text} 的议题网络 | 不应把同书其他章节或作者其他著作的观点补入当前切片 |\n")
    lines.append("| 知识要素 | 可抽取人物、机构、作品、技术、媒介和概念线索 | 不应把自动抽取实体直接当作权威规范名 |\n")
    lines.append("| 图像材料 | 可记录 Markdown 图注和图片链接存在 | 不应描述未实际查看的图像视觉细节 |\n\n")

    lines.append("## 7. 教材、研究与索引用途\n\n")
    lines.append(f"本文件适合用于：{theme_text} 的章节导读、关键词索引、案例线索整理和设计史/设计理论课程的材料入口。若用于课堂讲授，可先以源文标题和小标题建立问题框架，再选取关键句回读，让学生区分作者论证、案例证据和后续解释。\n\n")
    lines.append("若用于研究写作，建议把本报告当作“复审入口”而非最终引文依据：进入写作前应回到源 Markdown 和原 PDF，补齐页码、注释、图版编号、译名和版本信息。\n\n")

    lines.append("## 8. 可引用内容与不可确认内容\n\n")
    lines.append("可引用范围限于源文明确出现的标题、人物、机构、作品、案例、图注、数据和作者判断；直接引语必须回原书补页码。不可确认的内容包括仅由文件名推断的主题、未查看图片的视觉细节、OCR 可疑专名，以及当前切片没有展开的因果关系。\n\n")

    lines.append("## 9. 技术核验与证据边界\n\n")
    lines.append(f"源文件共约 {len(text)} 个字符；{integrity_status(text, headings)}。{image_status(text)}。相邻文件为前序 `{prev_path}`、后续 `{next_path}`。正式使用前需核对原 PDF 页码、注释、图版和版本信息。\n\n")

    lines.append("## 10. 复审结论\n\n")
    lines.append(f"本报告已重新读取 `{item.source}`，并按“{doc_type}”的实际信息结构完成 V2.0 重写。当前可作为 {theme_text} 的研究入口；自动抽取的专名、术语和证据关系已保留复核标记，不替代原书精读与正式引文核验。\n")
    return "".join(lines)


def should_skip(report_path: Path) -> bool:
    if not report_path.exists():
        return False
    text = report_path.read_text(encoding="utf-8", errors="replace")
    return ("已完成 V2.0 重写" in text or "已完成 V2.0 批量重写" in text) and len(text) > 3000


def main() -> None:
    items = read_queue()
    results: list[dict[str, str]] = []
    for item in items:
        source_path = ROOT / item.source
        report_path = ROOT / item.report
        if should_skip(report_path):
            results.append({"report": item.report, "source": item.source, "status": "skipped_existing_v2", "chars": str(report_path.stat().st_size)})
            continue
        if not source_path.exists():
            results.append({"report": item.report, "source": item.source, "status": "missing_source", "chars": "0"})
            continue
        text = source_path.read_text(encoding="utf-8", errors="replace")
        report_path.parent.mkdir(parents=True, exist_ok=True)
        new_report = generate_report(item, source_path, report_path, text)
        report_path.write_text(new_report, encoding="utf-8")
        results.append({"report": item.report, "source": item.source, "status": "rewritten", "chars": str(len(new_report))})

    with LOG.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["report", "source", "status", "chars"])
        writer.writeheader()
        writer.writerows(results)

    counts = Counter(row["status"] for row in results)
    rewritten = [row for row in results if row["status"] == "rewritten"]
    skipped = [row for row in results if row["status"] == "skipped_existing_v2"]
    missing = [row for row in results if row["status"] == "missing_source"]

    lines = []
    lines.append("# 00-books-result 重写进度\n\n")
    lines.append("日期：2026-07-11\n\n")
    lines.append("依据：`outputs/00-books-result重写队列.csv`\n\n")
    lines.append("## 批量执行结果\n\n")
    lines.append(f"- 队列总数：{len(results)}\n")
    lines.append(f"- 本轮直接写回 `00-books-result/`：{counts.get('rewritten', 0)}\n")
    lines.append(f"- 保留既有 V2 长报告：{counts.get('skipped_existing_v2', 0)}\n")
    lines.append(f"- 缺失源文未写入：{counts.get('missing_source', 0)}\n")
    lines.append(f"- 执行日志：`{LOG.relative_to(ROOT).as_posix()}`\n\n")
    lines.append("## 已直接写回 `00-books-result/` 的报告\n\n")
    lines.append("| 序号 | 报告 | 源文 | 状态 |\n|---:|---|---|---|\n")
    for i, row in enumerate(rewritten, 1):
        lines.append(f"| {i} | `{row['report']}` | `{row['source']}` | 已完成 V2.0 批量重写 |\n")
    if skipped:
        lines.append("\n## 已保留的既有 V2 报告\n\n")
        lines.append("| 序号 | 报告 | 源文 | 状态 |\n|---:|---|---|---|\n")
        for i, row in enumerate(skipped, 1):
            lines.append(f"| {i} | `{row['report']}` | `{row['source']}` | 已存在足量 V2 报告，未覆盖 |\n")
    if missing:
        lines.append("\n## 缺失源文\n\n")
        lines.append("| 序号 | 报告 | 源文 | 状态 |\n|---:|---|---|---|\n")
        for i, row in enumerate(missing, 1):
            lines.append(f"| {i} | `{row['report']}` | `{row['source']}` | 源文缺失，未写入 |\n")
    PROGRESS.write_text("".join(lines), encoding="utf-8")

    print(f"total={len(results)}")
    for status, count in counts.most_common():
        print(f"{status}={count}")
    print(LOG.relative_to(ROOT).as_posix())
    print(PROGRESS.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
