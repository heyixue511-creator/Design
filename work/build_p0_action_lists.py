from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "outputs" / "00-books-result-audit-details.csv"
OUT_DIR = ROOT / "outputs"


def norm_rel(path: str) -> str:
    return path.replace("\\", "/").strip()


def tokenize(text: str) -> set[str]:
    text = text.lower()
    text = re.sub(r"\bB\d{3,8}\b", " ", text)
    text = re.sub(r"\breport\b", " ", text)
    text = re.sub(r"[_\-.,;:()\[\]{}《》：“”'\"/\\]+", " ", text)
    return {tok for tok in text.split() if len(tok) >= 3}


def git_files() -> list[str]:
    import subprocess

    proc = subprocess.run(
        ["git", "-c", "core.quotePath=false", "ls-files", "-z"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        check=True,
    )
    return [item for item in proc.stdout.decode("utf-8", errors="replace").split("\0") if item]


def read_csv() -> list[dict[str, str]]:
    with AUDIT.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def book_dir(path: str, root: str) -> str:
    parts = norm_rel(path).split("/")
    if len(parts) >= 2 and parts[0] == root:
        return parts[1]
    return ""


def suggest_source(report: str, sources_by_book: dict[str, list[str]]) -> tuple[str, float, str]:
    bdir = book_dir(report, "00-books-result")
    candidates = sources_by_book.get(bdir, [])
    if not candidates:
        return "", 0.0, "no matching 00-books directory"

    report_tokens = tokenize(Path(report).stem)
    best: tuple[str, float] = ("", 0.0)
    for src in candidates:
        src_tokens = tokenize(Path(src).stem)
        if not report_tokens or not src_tokens:
            score = 0.0
        else:
            score = len(report_tokens & src_tokens) / len(report_tokens | src_tokens)
        if score > best[1]:
            best = (src, score)

    confidence = "low"
    if best[1] >= 0.45:
        confidence = "high"
    elif best[1] >= 0.25:
        confidence = "medium"
    return best[0], best[1], confidence


def first_flag_action(flags: str) -> tuple[str, str]:
    if "source unreadable/empty but report generated" in flags:
        return "exclude_and_rebuild", "源文为空或不可读却生成报告，现有报告不能计入可靠完成量；需先恢复/确认源文，再按 V2 重写或降级为 E/D 类。"
    if "no source path declared" in flags:
        return "locate_source_then_reaudit", "报告未声明源文件路径；必须先补齐并核验源文，不能直接算可靠完成。"
    if "duplicate B number" in flags:
        return "deduplicate_b_number", "重复 B 编号；需确定唯一保留报告，其余改号、合并或废弃。"
    if "tracked report path not materialized" in flags:
        return "resolve_case_collision", "Git 跟踪路径与 Windows 工作区落盘冲突；需先解决大小写路径冲突。"
    return "manual_review", "P0 其他问题；需人工判断。"


def write_outputs(rows: list[dict[str, str]], source_paths: list[str]) -> None:
    sources_by_book: dict[str, list[str]] = defaultdict(list)
    for src in source_paths:
        bdir = book_dir(src, "00-books")
        if bdir:
            sources_by_book[bdir].append(src)

    action_rows = []
    for row in rows:
        if row.get("severity") != "P0":
            continue
        action, rationale = first_flag_action(row.get("flags", ""))
        suggestion = ""
        score = 0.0
        confidence = ""
        if action == "locate_source_then_reaudit":
            suggestion, score, confidence = suggest_source(row["report"], sources_by_book)
        action_rows.append(
            {
                "action": action,
                "report": row["report"],
                "b_number": row.get("b_number", ""),
                "declared_sources": row.get("source_paths", ""),
                "suggested_source": suggestion,
                "suggestion_score": f"{score:.3f}" if suggestion else "",
                "suggestion_confidence": confidence,
                "flags": row.get("flags", ""),
                "rationale": rationale,
            }
        )

    csv_path = OUT_DIR / "00-books-result-P0执行清单.csv"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "action",
                "report",
                "b_number",
                "declared_sources",
                "suggested_source",
                "suggestion_score",
                "suggestion_confidence",
                "flags",
                "rationale",
            ],
        )
        writer.writeheader()
        writer.writerows(action_rows)

    counts = defaultdict(int)
    confidence_counts = defaultdict(int)
    for row in action_rows:
        counts[row["action"]] += 1
        if row["suggestion_confidence"]:
            confidence_counts[row["suggestion_confidence"]] += 1

    md_path = OUT_DIR / "00-books-result-P0复审执行清单.md"
    lines: list[str] = []
    lines.append("# 00-books-result P0 复审执行清单\n\n")
    lines.append("本清单由全量审计明细生成，用于开始处理不可计入可靠完成量的 P0 报告。\n\n")
    lines.append("## 一、动作分组\n\n")
    for key in ["exclude_and_rebuild", "locate_source_then_reaudit", "deduplicate_b_number", "resolve_case_collision", "manual_review"]:
        lines.append(f"- `{key}`：{counts.get(key, 0)}\n")
    lines.append("\n")
    lines.append("## 二、未声明源路径报告的自动匹配情况\n\n")
    for key in ["high", "medium", "low", "no matching 00-books directory"]:
        if confidence_counts.get(key):
            lines.append(f"- `{key}`：{confidence_counts[key]}\n")
    lines.append("\n")
    lines.append("说明：自动匹配只作为定位辅助，不能替代源文复核。只有重新读取 `00-books/` 源 Markdown 并按 V2.0 补齐证据边界后，报告才可恢复为可靠完成量。\n\n")
    lines.append("## 三、第一批建议处理\n\n")
    lines.append("### A. 先排除并重建：源文为空/不可读/近空却被写成报告\n\n")
    for row in [r for r in action_rows if r["action"] == "exclude_and_rebuild"][:60]:
        lines.append(f"- `{row['report']}`\n")
        if row["declared_sources"]:
            lines.append(f"  - 源文：`{row['declared_sources'].splitlines()[0]}`\n")
        lines.append(f"  - 问题：{row['flags']}\n")
    lines.append("\n### B. 先补源路径再复审：可自动推测源文的报告\n\n")
    suggested = [r for r in action_rows if r["action"] == "locate_source_then_reaudit" and r["suggested_source"]]
    suggested.sort(key=lambda r: (-float(r["suggestion_score"]), r["report"]))
    for row in suggested[:80]:
        lines.append(f"- `{row['report']}`\n")
        lines.append(f"  - 建议源文：`{row['suggested_source']}`（{row['suggestion_confidence']}，score={row['suggestion_score']}）\n")
    lines.append("\n### C. 重复 B 编号/大小写冲突\n\n")
    for row in [r for r in action_rows if r["action"] in {"deduplicate_b_number", "resolve_case_collision"}][:80]:
        lines.append(f"- `{row['report']}`\n")
        lines.append(f"  - 问题：{row['flags']}\n")
    lines.append(f"\n完整明细见 `{csv_path.name}`。\n")
    md_path.write_text("".join(lines), encoding="utf-8")

    print(f"p0_rows={len(action_rows)}")
    print(md_path)
    print(csv_path)


def main() -> None:
    files = git_files()
    source_paths = [p for p in files if p.startswith("00-books/") and p.endswith(".md")]
    rows = read_csv()
    write_outputs(rows, source_paths)


if __name__ == "__main__":
    main()
