from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT_ROOT = ROOT / "00-books-result"
SOURCE_ROOT = ROOT / "00-books"
OUTPUT_DIR = ROOT / "outputs"
LOG = OUTPUT_DIR / "00-books-result修复双语知识要素表日志.csv"
SUMMARY = OUTPUT_DIR / "00-books-result修复双语知识要素表报告.md"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rewrite_00_books_reports import make_entity_table, themes_from_terms, top_entities, top_terms  # noqa: E402


SOURCE_PATTERNS = [
    re.compile(r"\*\*源文件完整路径\*\*：`([^`]+)`"),
    re.compile(r"\*\*源文文件路径\*\*：`([^`]+)`"),
    re.compile(r"\*\*源文路径\*\*：`([^`]+)`"),
    re.compile(r"源文件完整路径：`([^`]+)`"),
    re.compile(r"源文文件路径：`([^`]+)`"),
    re.compile(r"源文路径：`([^`]+)`"),
    re.compile(r"`([^`]*00-books[\\/][^`]+?\.md)`"),
    re.compile(r"`(00-books/[^`]+?\.md)`"),
    re.compile(r"(00-books[\\/][^\n\r`]+?\.md)"),
    re.compile(r"(00-books/[^\n\r`]+?\.md)"),
]
SECTION_RE = re.compile(
    r"(?ms)^##\s*(?:4\.|四[、.．])\s*"
    r"(?:知识要素解构与术语标准化|核心概念、观点、人物与案例|核心概念.*?|知识要素.*?).*?"
    r"(?=^##\s*(?:5\.|五[、.．])|\Z)"
)
OLD_FOUR_COL_HEADER = "| 要素类型 | 原文名称 | 原文语境/可归入议题 | 证据状态 |"
NEW_SIX_COL_HEADER = "| 要素类型 | 原文名称 | 标准英文／原文名 | 原文语境 | 可归入议题 | 证据状态 |"


def long_path(path: Path) -> Path:
    resolved = path.resolve()
    if str(resolved).startswith("\\\\?\\"):
        return resolved
    return Path("\\\\?\\" + str(resolved))


def read_text_path(path: Path) -> str:
    for candidate in (path, long_path(path)):
        try:
            return candidate.read_text(encoding="utf-8-sig", errors="replace")
        except OSError:
            continue
    return ""


def path_exists(path: Path) -> bool:
    for candidate in (path, long_path(path)):
        try:
            if candidate.exists():
                return True
        except OSError:
            continue
    return False


def write_text_path(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    for candidate in (path, long_path(path)):
        try:
            candidate.write_text(text, encoding="utf-8")
            return
        except OSError:
            continue
    raise OSError(f"Cannot write {path}")


def normalize_source(src: str) -> str:
    src = src.strip().strip("。；;，, )）]'\"")
    src = src.replace("\\", "/")
    if ".md" in src:
        src = src[: src.find(".md") + 3]
    if "00-books/" in src:
        src = src[src.find("00-books/") :]
    return src


def extract_source(report_text: str) -> str:
    for pattern in SOURCE_PATTERNS:
        for match in pattern.findall(report_text):
            src = normalize_source(match)
            if src.startswith("00-books/") and src.endswith(".md"):
                return src
    return ""


def normalize_slug(text: str) -> str:
    text = text.lower()
    text = re.sub(r"^b\d+[-_]+", "", text)
    text = re.sub(r"[-_]+report$", "", text)
    text = re.sub(r"^\d+[-_]+", "", text)
    text = re.sub(r"[^0-9a-z\u4e00-\u9fff]+", "", text)
    return text


def fallback_source_for_report(report_path: Path, source_rel: str = "") -> str:
    try:
        rel_parent = report_path.relative_to(REPORT_ROOT).parent
    except ValueError:
        return ""
    source_dir = SOURCE_ROOT / rel_parent
    if not path_exists(source_dir):
        return ""

    report_base = re.sub(r"-report$", "", report_path.stem)
    report_base_without_id = re.sub(r"^B\d+[-_]+", "", report_base)
    candidates = [
        source_dir / f"{report_base}.md",
        source_dir / f"{report_base_without_id}.md",
    ]
    for candidate in candidates:
        if path_exists(candidate):
            return relative_path(candidate)

    source_files = list(source_dir.glob("*.md"))
    if not source_files:
        return ""

    report_slug = normalize_slug(report_base)
    if source_rel:
        old_slug = normalize_slug(Path(source_rel).stem)
        if old_slug:
            scored = [
                (score_slug_match(old_slug, normalize_slug(src.stem)), src)
                for src in source_files
            ]
            scored.sort(reverse=True, key=lambda item: item[0])
            if scored and scored[0][0] >= 0.58:
                return relative_path(scored[0][1])

    scored = [(score_slug_match(report_slug, normalize_slug(src.stem)), src) for src in source_files]
    scored.sort(reverse=True, key=lambda item: item[0])
    if scored and scored[0][0] >= 0.46:
        return relative_path(scored[0][1])
    return ""


def score_slug_match(left: str, right: str) -> float:
    if not left or not right:
        return 0.0
    if left == right:
        return 1.0
    if left in right or right in left:
        return min(len(left), len(right)) / max(len(left), len(right))
    left_tokens = set(re.findall(r"[a-z0-9]{3,}|[\u4e00-\u9fff]{2,}", left))
    right_tokens = set(re.findall(r"[a-z0-9]{3,}|[\u4e00-\u9fff]{2,}", right))
    if not left_tokens or not right_tokens:
        return 0.0
    return len(left_tokens & right_tokens) / len(left_tokens | right_tokens)


def relative_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def make_keyword_line(terms: list[tuple[str, int]]) -> str:
    if not terms:
        return "源文未形成稳定高频关键词；知识要素表只保留已能从源文定位的名称或术语。"
    return "源文高频词包括：" + "、".join(f"{term}（约 {count} 次）" for term, count in terms[:14]) + "。"


def build_section(source_text: str) -> str:
    terms = top_terms(source_text, 22)
    entities = top_entities(source_text, 28)
    table = make_entity_table(entities, terms).rstrip()
    themes = themes_from_terms(terms)
    theme_line = "、".join(themes) if themes else "需按源文上下文继续人工归类"
    return (
        "## 4. 知识要素解构与术语标准化\n\n"
        "本节已重新读取对应 `00-books/` 源文后生成；抽取同时覆盖中文、英文和其他外文，不以英文大写专名作为唯一依据。中文源文中的术语、人名、机构名、书名号作品和括号内外文原名均按源文证据处理；源文未给出外文原名时，不反推英文。\n\n"
        "### A. 知识要素表\n\n"
        f"{table}\n\n"
        "### B. 术语与关键词\n\n"
        f"{make_keyword_line(terms)}\n\n"
        f"可归入的主要议题簇：{theme_line}。\n\n"
        "抽取说明：中文概念、中文人物、中文机构与英文／外文专名均来自当前源文；`英文原名待核` 表示源文未明示标准外文名，后续正式引用仍需回到原书页码、图注或索引系统复核。\n"
    )


def replace_or_insert_section(report_text: str, new_section: str) -> tuple[str, str]:
    match = SECTION_RE.search(report_text)
    if match:
        return report_text[: match.start()] + new_section + report_text[match.end() :], "updated"

    insert_match = re.search(r"(?m)^##\s*(?:四[、.．]|4\.|五[、.．]|5\.)", report_text)
    if insert_match:
        return report_text[: insert_match.start()] + new_section + "\n" + report_text[insert_match.start() :], "inserted"

    return report_text.rstrip() + "\n\n" + new_section, "inserted"


def repair_report(report_path: Path, dry_run: bool) -> dict[str, str]:
    report_text = read_text_path(report_path)
    report_rel = relative_path(report_path)
    if not report_text:
        return {"report": report_rel, "source": "", "status": "read_error", "chars": "0"}

    source_rel = extract_source(report_text)
    if not source_rel:
        source_rel = fallback_source_for_report(report_path)
        if not source_rel:
            return {"report": report_rel, "source": "", "status": "missing_source_reference", "chars": str(len(report_text))}

    source_path = ROOT / source_rel
    if not path_exists(source_path):
        fallback_rel = fallback_source_for_report(report_path, source_rel)
        if fallback_rel:
            source_rel = fallback_rel
            source_path = ROOT / source_rel
        if not path_exists(source_path):
            return {"report": report_rel, "source": source_rel, "status": "missing_source_file", "chars": str(len(report_text))}

    source_text = read_text_path(source_path)
    if not source_text.strip():
        return {"report": report_rel, "source": source_rel, "status": "empty_source", "chars": str(len(report_text))}

    new_section = build_section(source_text)
    new_text, action = replace_or_insert_section(report_text, new_section)
    if new_text == report_text:
        return {"report": report_rel, "source": source_rel, "status": "unchanged", "chars": str(len(report_text))}

    if not dry_run:
        write_text_path(report_path, new_text)
    if dry_run:
        status = "would_update" if action == "updated" else "would_insert"
    else:
        status = action
    return {"report": report_rel, "source": source_rel, "status": status, "chars": str(len(new_text))}


def scan_headers() -> tuple[int, int]:
    old_count = 0
    new_count = 0
    for report in REPORT_ROOT.rglob("*report.md"):
        text = read_text_path(report)
        if OLD_FOUR_COL_HEADER in text:
            old_count += 1
        if NEW_SIX_COL_HEADER in text:
            new_count += 1
    return old_count, new_count


def write_outputs(rows: list[dict[str, str]], dry_run: bool) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with LOG.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["report", "source", "status", "chars"])
        writer.writeheader()
        writer.writerows(rows)

    counts = Counter(row["status"] for row in rows)
    old_headers, new_headers = scan_headers()
    lines = [
        "# 00-books-result 双语知识要素表修复报告\n\n",
        "日期：2026-07-11\n\n",
        "依据：`00-books-result/00-books Markdown 深度报告生成与复审规则.md` 的知识要素表要求；重新读取 `00-books/` 对应源文后，只替换每篇报告的第 4 节。\n\n",
        "## 执行结果\n\n",
        f"- 模式：{'dry-run，仅统计不写入' if dry_run else '已直接写回 00-books-result/'}\n",
        f"- 扫描报告：{len(rows)}\n",
        f"- 已更新：{counts.get('updated', 0)}\n",
        f"- 已插入：{counts.get('inserted', 0)}\n",
        f"- 预计更新：{counts.get('would_update', 0)}\n",
        f"- 预计插入：{counts.get('would_insert', 0)}\n",
        f"- 无变化：{counts.get('unchanged', 0)}\n",
        f"- 缺少源文引用：{counts.get('missing_source_reference', 0)}\n",
        f"- 源文件缺失：{counts.get('missing_source_file', 0)}\n",
        f"- 源文为空：{counts.get('empty_source', 0)}\n",
        f"- 缺少第 4 节：{counts.get('missing_section_4', 0)}\n\n",
        "## 表头复核\n\n",
        f"- 旧四列表头残留：{old_headers}\n",
        f"- 新六列表头出现：{new_headers}\n\n",
        "日志：`outputs/00-books-result修复双语知识要素表日志.csv`\n",
    ]
    SUMMARY.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    reports = sorted(REPORT_ROOT.rglob("*report.md"))
    if args.limit:
        reports = reports[: args.limit]

    rows = [repair_report(report, args.dry_run) for report in reports]
    write_outputs(rows, args.dry_run)

    counts = Counter(row["status"] for row in rows)
    print(f"scanned={len(rows)} counts={dict(counts)}")
    print(f"log={LOG.relative_to(ROOT).as_posix()}")
    print(f"summary={SUMMARY.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
