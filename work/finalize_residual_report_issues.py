from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

from full_audit_00_books_result_v2 import ROOT
from repair_bilingual_knowledge_tables import read_text_path, repair_report, write_text_path


DETAIL = ROOT / "outputs" / "00-books-result全量复审明细.csv"
LOG = ROOT / "outputs" / "00-books-result残留问题处理日志.csv"
SUMMARY = ROOT / "outputs" / "00-books-result残留问题处理报告.md"


def empty_source_report(report: str, source: str) -> str:
    report_id = Path(report).stem.replace("-report", "")
    return f"""# {report_id} 空源文边界报告

- **执行状态**：已核验源文件；源文为空，报告降格为边界记录
- **建议等级**：E 类暂不可用材料
- **源文件完整路径**：`{source}`
- **报告文件路径**：`{report}`
- **文件类型**：空 Markdown／图像切片边界
- **文本完整性**：源文件无可读正文

## 1. 源文核验与内容概述

已实际读取对应源文件，但文件不含可分析的正文、标题、图注或表格。当前只能确认该 Markdown 路径存在，不能从文件名推断页面内容。

## 2. 文献性质、作者立场与史料等级

该文件属于空切片或转换边界，不具备独立史料内容。作者立场、页面性质和原书功能均无法仅凭当前 Markdown 确认。

## 3. 语义深度分析

源文没有形成命题、概念关系或论证结构。任何主题扩写都会越过证据边界；若需恢复内容，应回查原 PDF、图像文件和相邻 Markdown。

## 4. 知识要素解构与术语标准化

| 要素类型 | 原文名称 | 标准英文／原文名 | 原文语境 | 可归入议题 | 证据状态 |
|---|---|---|---|---|---|
| 文件边界 | 空 Markdown | 原文名同左 | 当前源文件无可读文字 | 转换质量／缺页核验 | 已确认为空 |

## 5. 层级体系与论证结构

无法建立内容层级；当前只保留“源路径—空文件—待回查原始载体”三级核验关系。

## 6. 实证归类：案例、作品、史料与参考文献

没有可确认案例、作品、人物、机构、图注或参考文献。

## 7. 对《现当代设计史》的具体用途

仅用于记录资料缺口和触发原 PDF／相邻页复核，不应进入教材正文或事实数据库。

## 8. 可引用内容与不可确认内容

唯一可确认事项是源 Markdown 为空；文件名所暗示的页码或图像内容均不可引用。

## 9. 技术核验与证据边界

需要检查原始转换流程、图片资源和前后切片，确认是空白页、纯图页还是转换遗漏。

## 10. 复审结论

该报告已由错误模板改为 E 类空源文边界记录。除“文件为空”外，不提供任何内容性结论。
"""


def main() -> None:
    rows = list(csv.DictReader(DETAIL.open(encoding="utf-8-sig")))
    results: list[dict[str, str]] = []
    for row in rows:
        report_path = ROOT / row["report"]
        flags = row["flags"]
        if "知识要素含噪声词:history" in flags:
            text = read_text_path(report_path)
            updated = re.sub(r"(?m)^\|[^|]+\|\s*history\s*\|.*\|\s*$\n?", "", text, flags=re.I)
            if updated != text:
                write_text_path(report_path, updated)
                results.append({"status": "removed_history_noise", "report": row["report"], "source": row["sources"]})

        if "中文源文的知识要素表没有中文名称" in flags or "中文源文的中文知识要素覆盖偏少" in flags:
            result = repair_report(report_path, dry_run=False)
            results.append({"status": "rebuilt_bilingual_table:" + result["status"], "report": row["report"], "source": result["source"]})

        if "对应源文为空或不可读" in flags and row["sources"]:
            report = empty_source_report(row["report"], row["sources"].split(" | ")[0])
            write_text_path(report_path, report)
            results.append({"status": "rewritten_empty_source_boundary", "report": row["report"], "source": row["sources"]})

        if "报告无法定位对应源文" in flags:
            text = read_text_path(report_path)
            if "孤立旧报告，停止作为可靠深度报告使用" not in text:
                marker = (
                    "\n\n> **处置状态**：孤立旧报告，停止作为可靠深度报告使用。"
                    "当前无法与 `00-books/` 建立唯一对应关系；不得作为源文复审、教材事实或正式引文依据。\n"
                )
                write_text_path(report_path, text.rstrip() + marker)
            results.append({"status": "marked_orphan_report", "report": row["report"], "source": ""})

    with LOG.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["status", "report", "source"])
        writer.writeheader()
        writer.writerows(results)
    counts = Counter(row["status"].split(":", 1)[0] for row in results)
    SUMMARY.write_text(
        "# 00-books-result 残留问题处理报告\n\n"
        + "\n".join(f"- {key}：{value}" for key, value in counts.items())
        + "\n",
        encoding="utf-8",
    )
    print(dict(counts))


def add_chinese_ocr_rows() -> None:
    rows = list(csv.DictReader(DETAIL.open(encoding="utf-8-sig")))
    handled = 0
    for row in rows:
        flags = row["flags"]
        if "中文源文的知识要素表没有中文名称" not in flags and "中文源文的中文知识要素覆盖偏少" not in flags:
            continue
        if not row["sources"]:
            continue
        source_text = read_text_path(ROOT / row["sources"].split(" | ")[0])
        candidates: list[str] = []
        for heading in re.findall(r"(?m)^#{1,6}\s+(.+)$", source_text):
            value = re.sub(r"\s+", "", heading).strip("#，。；：、,. ")
            if 2 <= len(value) <= 36 and re.search(r"[\u3400-\u9fff]", value) and value not in candidates:
                candidates.append(value)
        for value in re.findall(r"[\u3400-\u9fff]{2,18}", source_text):
            if value not in candidates:
                candidates.append(value)
        candidates = candidates[:3]
        if not candidates:
            continue
        report_path = ROOT / row["report"]
        text = read_text_path(report_path)
        insertion = "".join(
            f"| OCR 中文文本线索 | {value} | 原文名同左 | 当前源文可见的中文标题或连续文字 | 中文漫画／设计方法／图像文字待归类 | 已在源文中出现，OCR 与语义待核 |\n"
            for value in candidates
        )
        table_sep = re.search(r"(?m)^\|---\|---\|---\|---\|---\|---\|\s*$", text)
        if table_sep:
            pos = table_sep.end()
            text = text[:pos] + "\n" + insertion.rstrip("\n") + text[pos:]
            write_text_path(report_path, text)
            handled += 1
    print({"added_chinese_ocr_rows": handled})


if __name__ == "__main__":
    main()
