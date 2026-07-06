# `00-books-result/` 书籍文档深度报告目录

本目录用于存放 `00-books/` 中每一个 Markdown 文档的深度报告，并且目录结构应与 `00-books/` 保持一致。

## 一、报告目标

`00-books/` 中包含大量书籍整本、章节、导论、目录、bibliography 和拆分页文档。本目录将把每个原始 md 文档转化为可服务《现当代设计史》教材写作的深度报告。

## 二、目录结构原则

`00-books-result/` 采用与 `00-books/` 相同的相对目录结构。

例如：

```text
00-books/某书名/某章节.md
```

对应报告应保存为：

```text
00-books-result/某书名/某章节-report.md
```

也就是说，报告文件不再集中放在 `00-books-result/` 根目录，而是放入与原始文档一致的书籍 / 章节目录中。

## 三、报告命名规则

```text
原文件名-report.md
```

示例：

```text
00-books/BUCHANAN, RICHARD. Branzi/01-Branzi's DilemmaDesign in Contemporary CultureRich.md
00-books-result/BUCHANAN, RICHARD. Branzi/01-Branzi's DilemmaDesign in Contemporary CultureRich-report.md
```

报告内部仍保留编号，如 `B0001`、`B0002`，编号原则上与 `books-paths.txt` 的路径顺序对应。

## 四、单篇报告结构

每篇报告建议包括：

1. 基础书目信息；
2. 原始文件路径；
3. 镜像报告路径；
4. 所属书籍 / 章节；
5. 文献类型与重要性等级；
6. 核心内容摘要；
7. 研究对象；
8. 主要观点；
9. 论证路径；
10. 核心概念；
11. 关键人物 / 案例；
12. 可用于教材章节；
13. 可引用页码或段落线索；
14. 教学转化建议；
15. 待核问题。

## 五、当前进度

进度见 [`PROGRESS.md`](PROGRESS.md)。

## 六、说明

由于 `00-books/` 约有 1344 个 `.md` 路径，建议分批处理：先处理 A 类核心书籍和与《现当代设计史》章节高度相关的文件，再处理辅助性目录、索引和 bibliography。
