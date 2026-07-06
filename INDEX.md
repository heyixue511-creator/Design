# 《现当代设计史》资料仓库索引

本仓库用于支持《现当代设计史》课程、论文或资料卡写作，主要收录设计史、设计研究、设计理论、设计文化、技术与人工物研究、全球设计史等相关 Markdown 文档。

## 一、资料规模

| 目录 | 内容类型 | 当前索引规模 | 主要用途 |
|---|---|---:|---|
| [`00-books/`](00-books/) | 书籍、章节、书籍拆分页、bibliography | 约 1344 个 `.md` 路径 | 建立章节知识框架、提取历史叙述、补充参考文献 |
| [`00-Paper/`](00-Paper/) | 论文、文章、书评、专题材料 | 72 个 `.md` 路径 | 提炼理论概念、研究方法、专题案例与学术争议 |
| [`books-paths.txt`](books-paths.txt) | 书籍文档完整路径清单 | 1 个清单文件 | 底层路径检索 |
| [`paper-paths.txt`](paper-paths.txt) | 论文文档完整路径清单 | 1 个清单文件 | 底层路径检索 |

## 二、索引文件

| 索引文件 | 功能 |
|---|---|
| [`INDEX.md`](INDEX.md) | 仓库总索引：说明资料结构、写作流程、章节主题映射 |
| [`00-books/INDEX.md`](00-books/INDEX.md) | 书籍资料索引：按书籍与专题方向组织 |
| [`00-Paper/INDEX.md`](00-Paper/INDEX.md) | 论文资料索引：按理论问题、方法和专题组织 |

## 三、《现当代设计史》写作使用流程

建议采用以下工作流：

1. **确定章节主题**：先从论文或课程目录出发，明确章节问题，例如“现代设计的生成”“包豪斯与现代主义”“设计研究的兴起”“全球设计史写作”等。
2. **进入主题索引**：根据下方“章节—资料映射表”，优先进入 `00-books/INDEX.md` 或 `00-Paper/INDEX.md`。
3. **读取核心文献**：先读书籍导论、目录、章节小结和 bibliography，再读相关论文。
4. **建立资料卡**：每条资料卡建议记录：文献题名、作者、年份、核心概念、可用于哪一章节、可引用页码或段落。
5. **形成章节文献组**：每章至少形成“核心书籍 + 关键论文 + 案例材料 + 参考文献”四类材料。

## 四、章节—资料映射表

| 写作章节或问题 | 优先资料目录 | 推荐检索关键词 |
|---|---|---|
| 设计史学科对象、边界与方法 | `00-books/`、`00-Paper/` | design history, design studies, historiography, Margolin, Doordan |
| 工业化、现代性与设计制度形成 | `00-books/` | industrialization, modernity, World History of Design, production, consumption |
| 工艺美术运动、装饰、图案与早期现代设计 | `00-books/`、`00-Paper/` | Arts and Crafts, ornament, decoration, Ruskin, Morris, Grammar of Ornament |
| 包豪斯、乌尔姆、先锋派与现代主义教育 | `00-books/`、`00-Paper/` | Bauhaus, Vkhutemas, Ulm, Gropius, modernity, pedagogy |
| 平面设计、印刷、信息图形与视觉传播 | `00-books/`、`00-Paper/` | graphic design, printing, Isotype, Saul Bass, Rodchenko, visual interface |
| 设计研究、设计思维与问题框架 | `00-Paper/`、`00-books/` | Buchanan, Cross, Dorst, design thinking, wicked problems, design research |
| 技术、人工物与社会关系 | `00-Paper/` | artifacts, politics, Latour, Bijker, Kopytoff, publics, material culture |
| 数字设计、HCI 与交互设计研究 | `00-books/`、`00-Paper/` | HCI, interaction design, software design, probes, contextual design, interface |
| 可持续设计、转型设计与未来研究 | `00-Paper/`、`00-books/` | sustainability, transition design, Tonkinwise, Terry Irwin, Thackara |
| 全球设计史、后殖民与跨文化设计史 | `00-books/`、`00-Paper/` | World History of Design, China, postcolonial, border thinking, regionalism |

## 五、资料卡建议格式

```md
### 文献题名

- 作者：
- 年份：
- 类型：书籍 / 章节 / 论文 / 书评 / 案例材料
- 所属主题：
- 可用于章节：
- 核心观点：
- 关键词：
- 可引用段落或页码：
- 与《现当代设计史》的关系：
```

## 六、下一步建议

1. 为每个章节建立 `chapter-index` 或资料卡文件。
2. 将 `books-paths.txt` 中的书籍路径进一步按“书名文件夹”去重，形成书目级索引。
3. 将 `00-Paper/` 中 72 篇论文按“设计史理论 / 设计研究 / 技术与人工物 / 可持续与转型 / 全球与后殖民”继续精分。
4. 为 Victor Margolin、Richard Buchanan、Nigel Cross、Terry Irwin、Cameron Tonkinwise 等核心作者建立人物索引。
