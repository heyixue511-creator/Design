from __future__ import annotations

import csv
import re
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path

import numpy as np
from scipy.optimize import linear_sum_assignment
from sklearn.feature_extraction.text import TfidfVectorizer

from full_audit_00_books_result_v2 import OUTPUT_ROOT, REPORT_ROOT, ROOT, SOURCE_ROOT, read_text


DETAIL = OUTPUT_ROOT / "00-books-result全量复审明细.csv"
LOG = OUTPUT_ROOT / "00-books-result源文映射重建日志.csv"
SUMMARY = OUTPUT_ROOT / "00-books-result源文映射重建报告.md"


def parent_key(path: str) -> str:
    value = str(Path(path).parent).replace("\\", "/")
    return value.replace("00-books-result", "00-books", 1)


def normalized_stem(path: str) -> str:
    value = Path(path).stem.lower()
    value = re.sub(r"^(?:b\d+|\d+)[-_ ]*", "", value)
    value = re.sub(r"[-_ ]*report$", "", value)
    return re.sub(r"[^a-z0-9\u3400-\u9fff]+", "", value)


def title_score(report: str, source: str) -> float:
    left, right = normalized_stem(report), normalized_stem(source)
    if not left or not right:
        return 0.0
    score = SequenceMatcher(None, left, right).ratio()
    if left in right or right in left:
        score = max(score, min(len(left), len(right)) / max(len(left), len(right)))
    return score


def semantic_matrix(reports: list[str], sources: list[str]) -> np.ndarray:
    report_texts = [read_text(ROOT / path)[:16000] for path in reports]
    source_texts = [read_text(ROOT / path)[:24000] for path in sources]
    docs = report_texts + source_texts
    try:
        vectors = TfidfVectorizer(
            analyzer="char_wb", ngram_range=(3, 5), min_df=1, max_features=24000, sublinear_tf=True
        ).fit_transform(docs)
        return (vectors[: len(reports)] @ vectors[len(reports) :].T).toarray()
    except ValueError:
        return np.zeros((len(reports), len(sources)))


def insert_source_path(report_path: Path, source: str) -> None:
    text = read_text(report_path)
    if "源文件完整路径" in text or "源文文件路径" in text or "源文路径" in text:
        return
    line = f"- **源文件完整路径**：`{source}`\n"
    match = re.search(r"(?m)^# .+$", text)
    if match:
        pos = match.end()
        updated = text[:pos] + "\n\n" + line + text[pos:].lstrip("\n")
    else:
        updated = line + "\n" + text
    report_path.write_text(updated, encoding="utf-8")


def main() -> None:
    rows = list(csv.DictReader(DETAIL.open(encoding="utf-8-sig")))
    unmapped = [row["report"] for row in rows if row["severity"] == "P0" and not row["sources"]]
    covered = {source for row in rows for source in row["sources"].split(" | ") if source}
    all_sources = [path.relative_to(ROOT).as_posix() for path in SOURCE_ROOT.rglob("*.md")]
    missing = [source for source in all_sources if source not in covered]

    reports_by_dir: defaultdict[str, list[str]] = defaultdict(list)
    sources_by_dir: defaultdict[str, list[str]] = defaultdict(list)
    for report in unmapped:
        reports_by_dir[parent_key(report)].append(report)
    for source in missing:
        sources_by_dir[parent_key(source)].append(source)

    output: list[dict[str, str]] = []
    accepted: list[tuple[str, str]] = []
    for directory, sources in sources_by_dir.items():
        reports = reports_by_dir.get(directory, [])
        if not reports:
            for source in sources:
                output.append({"status": "unmatched_source", "report": "", "source": source, "score": "0", "margin": "0"})
            continue

        semantic = semantic_matrix(reports, sources)
        title = np.array([[title_score(report, source) for source in sources] for report in reports])
        combined = 0.58 * title + 0.42 * semantic
        report_idx, source_idx = linear_sum_assignment(-combined)
        assigned_sources = set()
        for ri, si in zip(report_idx, source_idx):
            score = float(combined[ri, si])
            alternatives = sorted(combined[:, si], reverse=True)
            margin = score - float(alternatives[1] if len(alternatives) > 1 else 0)
            tscore = float(title[ri, si])
            sscore = float(semantic[ri, si])
            safe = (
                (score >= 0.66 and margin >= 0.06)
                or (tscore >= 0.88 and margin >= 0.04)
                or (tscore >= 0.72 and sscore >= 0.48 and margin >= 0.08)
            )
            status = "mapped" if safe else "needs_new_report"
            output.append({
                "status": status,
                "report": reports[ri] if safe else "",
                "source": sources[si],
                "score": f"{score:.4f}",
                "margin": f"{margin:.4f}",
            })
            assigned_sources.add(si)
            if safe:
                accepted.append((reports[ri], sources[si]))
        for si, source in enumerate(sources):
            if si not in assigned_sources:
                output.append({"status": "needs_new_report", "report": "", "source": source, "score": "0", "margin": "0"})

    for report, source in accepted:
        insert_source_path(ROOT / report, source)

    with LOG.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["status", "report", "source", "score", "margin"])
        writer.writeheader()
        writer.writerows(output)

    new_needed = sum(row["status"] != "mapped" for row in output)
    SUMMARY.write_text(
        "# 00-books-result 源文映射重建报告\n\n"
        f"- 原无源路径报告：{len(unmapped)}\n"
        f"- 原缺失报告源文：{len(missing)}\n"
        f"- 已建立高置信一对一映射：{len(accepted)}\n"
        f"- 仍需新建报告：{new_needed}\n"
        f"- 未强制匹配的旧报告：{len(unmapped) - len(accepted)}\n\n"
        "匹配综合同目录标题相似度、旧报告正文与源文的字符 TF-IDF 语义相似度，并执行一对一分配。"
        "低分、低区分度或通用标题对象不写入源路径。\n",
        encoding="utf-8",
    )
    print(f"unmapped={len(unmapped)} missing={len(missing)} mapped={len(accepted)} new_needed={new_needed}")


if __name__ == "__main__":
    main()
