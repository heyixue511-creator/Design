from __future__ import annotations

import csv
import hashlib
from pathlib import Path

from repair_bilingual_knowledge_tables import long_path, path_exists, read_text_path


ROOT = Path(__file__).resolve().parents[1]
REPORT_ROOT = (ROOT / "00-books-result").resolve()
EXTRAS = ROOT / "outputs" / "00-books-result多余报告明细.csv"
MANIFEST = ROOT / "outputs" / "00-books-result已删除重复报告清单.csv"
SUMMARY = ROOT / "outputs" / "00-books-result删除重复报告报告.md"


def resolved_inside_report_root(path: Path) -> Path:
    resolved = path.resolve()
    try:
        resolved.relative_to(REPORT_ROOT)
    except ValueError as exc:
        raise RuntimeError(f"目标不在 00-books-result 内：{resolved}") from exc
    return resolved


def unlink_path(path: Path) -> None:
    try:
        path.unlink()
        return
    except OSError:
        long_path(path).unlink()


def main() -> None:
    rows = list(csv.DictReader(EXTRAS.open(encoding="utf-8-sig")))
    targets = [row for row in rows if row["category"] == "duplicate_noncanonical"]
    if len(targets) != 202:
        raise RuntimeError(f"预期 202 份重复非主报告，实际 {len(targets)}")

    target_paths: set[Path] = set()
    canonical_paths: set[Path] = set()
    prepared: list[dict[str, str]] = []
    for row in targets:
        target = resolved_inside_report_root(ROOT / row["extra_report"])
        canonical = resolved_inside_report_root(ROOT / row["canonical_report"])
        if target == canonical:
            raise RuntimeError(f"删除目标与主报告相同：{target}")
        if not path_exists(target):
            raise RuntimeError(f"删除目标不存在：{target}")
        if not path_exists(canonical):
            raise RuntimeError(f"主报告不存在：{canonical}")
        if target in target_paths:
            raise RuntimeError(f"重复删除目标：{target}")
        target_paths.add(target)
        canonical_paths.add(canonical)
        content = read_text_path(target)
        prepared.append({
            "deleted_report": row["extra_report"],
            "source": row["source"],
            "kept_report": row["canonical_report"],
            "bytes": str(len(content.encode("utf-8"))),
            "sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
        })

    overlap = target_paths & canonical_paths
    if overlap:
        raise RuntimeError(f"某些主报告同时出现在删除集合：{len(overlap)}")

    with MANIFEST.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["deleted_report", "source", "kept_report", "bytes", "sha256"],
        )
        writer.writeheader()
        writer.writerows(prepared)

    for target in sorted(target_paths, key=str):
        unlink_path(target)

    remaining_targets = [path for path in target_paths if path_exists(path)]
    missing_canonicals = [path for path in canonical_paths if not path_exists(path)]
    if remaining_targets or missing_canonicals:
        raise RuntimeError(
            f"删除后校验失败：仍存在目标 {len(remaining_targets)}，缺失主报告 {len(missing_canonicals)}"
        )

    SUMMARY.write_text(
        "# 00-books-result 删除重复报告报告\n\n"
        f"- 重复源文组：181\n"
        f"- 已删除非主报告：{len(targets)}\n"
        f"- 保留主报告：{len(canonical_paths)}\n"
        "- 新建 B9 报告被删除：0\n"
        "- 人工模型语义复审报告被删除：0\n"
        "- 删除清单：`outputs/00-books-result已删除重复报告清单.csv`\n\n"
        "每条清单包含删除路径、对应源文、保留主报告、字节数和 SHA-256。\n",
        encoding="utf-8",
    )
    print(f"deleted={len(targets)} kept={len(canonical_paths)} manifest={MANIFEST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
