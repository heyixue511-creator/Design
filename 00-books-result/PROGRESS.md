# `00-books-result/` 深度报告进度表

来源目录：`00-books/`  
来源清单：`books-paths.txt`  
计划数量：约 1344 个 `.md` 文档路径

## 一、处理状态说明

| 状态 | 含义 |
|---|---|
| ✅ 已完成 | 已生成深度报告 |
| 🟡 进行中 | 已读取原文，报告待完善 |
| ⬜ 未处理 | 尚未生成报告 |
| ⚠️ 待核 | 文献信息、页码、题名或来源需核对 |

## 二、目录结构规则

`00-books-result/` 与 `00-books/` 保持相同的相对目录结构：

```text
00-books/某书名/某章节.md
00-books-result/某书名/某章节-report.md
```

## 三、批次规则

`00-books/` 采用**书籍文件夹批次**推进：

```text
10 本书 = 10 个一级书籍文件夹 = 1 批
```

处理顺序以 `books-paths.txt` 中首次出现的一级文件夹为准。每一批先确定 10 个书籍文件夹，再处理这些文件夹内部的 md 深度报告。

### 第一批书籍文件夹：BATCH-BOOKS-001

| 批次序号 | 一级书籍文件夹 | 当前状态 | 说明 |
|---|---|---|---|
| 01 | `BUCHANAN, RICHARD. Branzi` | 🟡 已开始 | 已完成该文件夹内 4 个报告 |
| 02 | `Bringing design to software (Terry Winograd, (ed.))` | 🟡 已开始 | 已完成 B0008—B0033，剩余 Name Index、Subject Index、全书汇总与 OCR / bibliography 文件 |
| 03 | `CROSS, NIGEL. From a Design Science to a Design Discipline Understanding Designe` | ⬜ 未处理 | 下一步纳入本批处理 |
| 04 | `Contextual Design_ Defining Customer-Centered Systems -- Beyer, Hugh, Holtzblatt` | ⬜ 未处理 | 下一步纳入本批处理 |
| 05 | `DILLON, ANDREW. Beyond Usability Process, Outcome and Affect in Human Computer Interaction` | ⬜ 未处理 | 下一步纳入本批处理 |
| 06 | `Design Anthropology in Context _ An Introduction to Design -- Adam Drazin -- Lon` | ⬜ 未处理 | 下一步纳入本批处理 |
| 07 | `Design Fiction_ A Method Toolbox for Design Research in a -- Martin Wiedmer; Sim` | ⬜ 未处理 | 下一步纳入本批处理 |
| 08 | `Design Research Now __ The Uneasy Relationship between -- Susann Vihma; Ralf Mic` | ⬜ 未处理 | 下一步纳入本批处理 |
| 09 | `Design and Creativity Policy, Management and Practice (Guy Julier Liz Moor (edit` | ⬜ 未处理 | 下一步纳入本批处理 |
| 10 | `Design for Policy -- Christian Bason -- (OECD Publishing, 2014) -- 92642146` | ⬜ 未处理 | 下一步纳入本批处理，具体路径需继续向后读取确认完整文件夹名 |

## 四、已完成报告

已完成报告：B0001—B0033，共 33 个。

本轮新增：B0022—B0033，共 12 个，均位于 `Bringing design to software (Terry Winograd, (ed.))` 文件夹下。

完整已完成清单见 [`INDEX.md`](INDEX.md)。

## 五、下一步继续处理

继续补完 `BATCH-BOOKS-001` 中第 2 个文件夹 `Bringing design to software (Terry Winograd, (ed.))` 的剩余非正文 / 汇总文件：`29-Name Index.md`、`30-Subject Index.md`、`31-Bringing Design to Software.md` 以及 OCR / bibliography 文件。之后进入第 3 个文件夹 `CROSS, NIGEL. From a Design Science to a Design Discipline Understanding Designe`。

## 六、总体进度

```text
已完成：33 / 约 1344
未完成：约 1311 / 约 1344
当前批次规则：10 个一级书籍文件夹为 1 批
当前批次：BATCH-BOOKS-001
```
