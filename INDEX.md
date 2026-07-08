# 《现当代设计史》资料仓库索引

本仓库用于支持《现当代设计史》课程、论文或资料卡写作，主要收录设计史、设计研究、设计理论、设计文化、技术与人工物研究、全球设计史等相关 Markdown 文档。

## 一、资料规模

| 目录 | 内容类型 | 当前索引规模 | 主要用途 |
|---|---|---:|---|
| [`00-books/`](00-books/) | 书籍、章节、书籍拆分页、bibliography | 15369 个 `.md` 路径 | 建立章节知识框架、提取历史叙述、补充参考文献 |
| [`00-Paper/`](00-Paper/) | 论文、文章、书评、专题材料 | 72 个 `.md` 路径 | 提炼理论概念、研究方法、专题案例与学术争议 |
| [`books-paths.txt`](books-paths.txt) | 书籍文档完整路径清单 | 1 个清单文件 | 底层路径检索 |
| [`paper-paths.txt`](paper-paths.txt) | 论文文档完整路径清单 | 1 个清单文件 | 底层路径检索 |
| [`index-system/`](index-system/) | 教材型综合索引系统 | 12 个索引模板文件 | 支持文献信息、主题、观点、概念、人物、案例、章节、教学和引用管理 |
| [`00-Paper-result/`](00-Paper-result/) | 论文深度报告结果 | 当前已完成 9 篇，待核 1 篇 | 将论文转化为教材写作报告 |
| [`00-books-result/`](00-books-result/) | 书籍文档深度报告结果 | 详见缺失审计与进度表 | 将书籍 / 章节文档转化为教材写作报告 |

## 二、索引文件

| 索引文件 | 功能 |
|---|---|
| [`INDEX.md`](INDEX.md) | 仓库总索引：说明资料结构、写作流程、章节主题映射 |
| [`00-books/INDEX.md`](00-books/INDEX.md) | 书籍资料索引：按书籍与专题方向组织 |
| [`00-Paper/INDEX.md`](00-Paper/INDEX.md) | 论文资料索引：按理论问题、方法和专题组织 |
| [`index-system/README.md`](index-system/README.md) | 教材型综合索引系统总说明 |
| [`00-Paper-result/INDEX.md`](00-Paper-result/INDEX.md) | 论文深度报告索引 |
| [`00-books-result/INDEX.md`](00-books-result/INDEX.md) | 书籍文档深度报告索引 |

## 三、教材型综合索引系统

| 文件 | 功能 |
|---|---|
| [`01-total-bibliography-index.md`](index-system/01-total-bibliography-index.md) | 基础书目信息索引：作者、译者、题名、出版信息、ISBN/DOI、引用格式 |
| [`02-theme-index.md`](index-system/02-theme-index.md) | 主题分类索引：按教材知识主题组织文献 |
| [`03-content-summary-index.md`](index-system/03-content-summary-index.md) | 内容摘要索引：记录核心内容、研究对象、主要观点和使用价值 |
| [`04-viewpoint-index.md`](index-system/04-viewpoint-index.md) | 观点索引：提炼可用于教材论证的核心判断 |
| [`05-concept-index.md`](index-system/05-concept-index.md) | 概念索引：整理核心术语、英文原文、定义、来源和易混概念 |
| [`06-person-index.md`](index-system/06-person-index.md) | 人物索引：整理学者、设计师、艺术家、教育家等 |
| [`07-case-index.md`](index-system/07-case-index.md) | 案例索引：整理作品、事件、机构、展览、产品等 |
| [`08-chapter-correspondence-index.md`](index-system/08-chapter-correspondence-index.md) | 章节对应索引：把文献、观点、概念、人物、案例、图片对应到教材章节 |
| [`09-teaching-function-index.md`](index-system/09-teaching-function-index.md) | 教学功能索引：难度、适用对象、课堂问题、作业设计 |
| [`10-version-translation-citation-index.md`](index-system/10-version-translation-citation-index.md) | 版本、译本、引文与页码索引 |
| [`11-image-method-controversy-timeline-index.md`](index-system/11-image-method-controversy-timeline-index.md) | 图像、研究方法、争议问题与时间线索引 |
| [`12-master-index-template.md`](index-system/12-master-index-template.md) | 综合总表模板：适合转为表格或数据库 |

## 四、深度报告系统

| 结果目录 | 说明 |
|---|---|
| [`00-Paper-result/`](00-Paper-result/) | 存放 `00-Paper/` 中 72 篇论文 / 文章 / 书评 / 专题材料的逐篇深度报告 |
| [`00-books-result/`](00-books-result/) | 存放 `00-books/` 中每一个书籍或章节 Markdown 文档的深度报告 |

当前已建立两批报告，详见：

- [`00-Paper-result/PROGRESS.md`](00-Paper-result/PROGRESS.md)
- [`00-books-result/PROGRESS.md`](00-books-result/PROGRESS.md)

## 五、《现当代设计史》写作使用流程

建议采用以下工作流：

1. **确定章节主题**：先从论文或课程目录出发，明确章节问题，例如“现代设计的生成”“包豪斯与现代主义”“设计研究的兴起”“全球设计史写作”等。
2. **进入主题索引**：根据下方“章节—资料映射表”，优先进入 `00-books/INDEX.md`、`00-Paper/INDEX.md` 或 `index-system/02-theme-index.md`。
3. **建立基础书目表**：先在 `index-system/01-total-bibliography-index.md` 中统一编号、作者、题名、出版信息和引用格式。
4. **读取核心文献**：先读书籍导论、目录、章节小结和 bibliography，再读相关论文。
5. **建立资料卡**：每条资料卡建议记录：文献题名、作者、年份、核心概念、可用于哪一章节、可引用页码或段落。
6. **提炼观点与概念**：将核心文献中的判断转入观点索引，将教材术语转入概念索引。
7. **形成章节文献组**：每章至少形成“核心书籍 + 关键论文 + 核心观点 + 重要概念 + 代表人物 + 经典案例 + 图片资料 + 教学问题”。
8. **生成深度报告**：将每个原始 md 文档的分析结果保存到 `00-Paper-result/` 或 `00-books-result/`。

## 六、章节—资料映射表

| 写作章节或问题 | 优先资料目录 | 推荐检索关键词 |
|---|---|---|
| 设计史学科对象、边界与方法 | `00-books/`、`00-Paper/`、`index-system/` | design history, design studies, historiography, Margolin, Doordan |
| 工业化、现代性与设计制度形成 | `00-books/` | industrialization, modernity, World History of Design, production, consumption |
| 工艺美术运动、装饰、图案与早期现代设计 | `00-books/`、`00-Paper/` | Arts and Crafts, ornament, decoration, Ruskin, Morris, Grammar of Ornament |
| 包豪斯、乌尔姆、先锋派与现代主义教育 | `00-books/`、`00-Paper/` | Bauhaus, Vkhutemas, Ulm, Gropius, modernity, pedagogy |
| 平面设计、印刷、信息图形与视觉传播 | `00-books/`、`00-Paper/` | graphic design, printing, Isotype, Saul Bass, Rodchenko, visual interface |
| 设计研究、设计思维与问题框架 | `00-Paper/`、`00-books/` | Buchanan, Cross, Dorst, design thinking, wicked problems, design research |
| 技术、人工物与社会关系 | `00-Paper/` | artifacts, politics, Latour, Bijker, Kopytoff, publics, material culture |
| 数字设计、HCI 与交互设计研究 | `00-books/`、`00-Paper/` | HCI, interaction design, software design, probes, contextual design, interface |
| 可持续设计、转型设计与未来研究 | `00-Paper/`、`00-books/` | sustainability, transition design, Tonkinwise, Terry Irwin, Thackara |
| 全球设计史、后殖民与跨文化设计史 | `00-books/`、`00-Paper/` | World History of Design, China, postcolonial, border thinking, regionalism |

## 七、下一步建议

1. 继续处理 `00-Paper/` 中 Doordan、Design history anthology、Capkova、Tonkinwise、Forlano、HCI / probes 等核心文献。
2. 继续处理 `00-books/` 中 Victor Margolin、Buchanan、Cross 等核心书籍章节。
3. 每完成一批报告，同步更新 `00-Paper-result/PROGRESS.md` 和 `00-books-result/PROGRESS.md`。
