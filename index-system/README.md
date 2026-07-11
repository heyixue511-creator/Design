# 《现当代设计史》教材型综合索引系统

本目录用于将 `00-books/` 与 `00-Paper/` 中的大量 Markdown 文献，转化为可直接服务教材写作、章节组织、课堂教学和引用管理的综合索引系统。

该系统不是简单的“文件目录”，而是围绕教材写作建立的资料组织框架：

```text
章节结构 → 核心概念 → 代表人物 → 重要文献 → 经典案例 → 核心观点 → 可引用材料 → 教学设计
```

## 一、索引系统文件

| 文件 | 功能 |
|---|---|
| [`01-total-bibliography-index.md`](01-total-bibliography-index.md) | 总文献索引：作者、题名、出版信息、ISBN/DOI、引用格式 |
| [`02-theme-index.md`](02-theme-index.md) | 主题分类索引：按教材知识主题组织文献 |
| [`03-content-summary-index.md`](03-content-summary-index.md) | 内容摘要索引：说明每本文献的内容、对象、观点和使用价值 |
| [`04-viewpoint-index.md`](04-viewpoint-index.md) | 核心观点索引：提炼可支撑教材论述的观点 |
| [`05-concept-index.md`](05-concept-index.md) | 概念术语索引：整理教材中的核心术语与解释 |
| [`06-person-index.md`](06-person-index.md) | 人物索引：学者、设计师、艺术家、教育家等 |
| [`07-case-index.md`](07-case-index.md) | 案例索引：作品、事件、机构、展览、产品等 |
| [`08-chapter-correspondence-index.md`](08-chapter-correspondence-index.md) | 章节对应索引：把文献、观点、案例与教材章节关联 |
| [`09-teaching-function-index.md`](09-teaching-function-index.md) | 教学功能索引：难度、用途、讨论题、作业设计 |
| [`10-version-translation-citation-index.md`](10-version-translation-citation-index.md) | 版本、译本、引文与页码索引 |
| [`11-image-method-controversy-timeline-index.md`](11-image-method-controversy-timeline-index.md) | 图像、研究方法、争议问题与时间线索引 |
| [`12-master-index-template.md`](12-master-index-template.md) | 综合总表模板：适合做成一个总表或数据库 |
| [`13-report-integration-rules.md`](13-report-integration-rules.md) | 深度报告入库规则：规定精读层与中央索引层的字段映射、编号、去重和复核流程 |

## 二、使用原则

1. **先建编号体系**：所有文献统一编号，如 B001、P001；观点用 V001；概念用 C001；人物用 N001；案例用 K001；引文用 Q001；图片用 Fig.001。
2. **先粗分，后精读**：先按题名和目录做主题归类，再逐步补充摘要、页码、观点和引文。
3. **教材优先**：每条索引都要回答“可用于教材哪一章、哪一节、哪一教学单元”。
4. **引用可核**：凡是用于正文论证的观点、引文、页码，都必须回到原文文件核对。
5. **动态维护**：D 类待核文献、版本差异、版权问题、翻译差异需持续更新。

## 三、建议编号规则

| 类型 | 编号规则 | 示例 |
|---|---|---|
| 书籍文献 | B001、B002 | B001 |
| 论文文献 | P001、P002 | P001 |
| 核心观点 | V001、V002 | V001 |
| 概念术语 | C001、C002 | C001 |
| 人物 | N001、N002 | N001 |
| 案例 | K001、K002 | K001 |
| 引文 | Q001、Q002 | Q001 |
| 图像 | Fig.001、Fig.002 | Fig.001 |
| 时间线事件 | T001、T002 | T001 |

## 四、重要性等级

| 等级 | 含义 | 使用方式 |
|---|---|---|
| A 类核心文献 | 教材必须参考，构成基本框架 | 重点阅读、重点引用 |
| B 类重要文献 | 对某些章节有重要支撑 | 局部使用 |
| C 类辅助文献 | 提供案例、背景、补充材料 | 选择性使用 |
| D 类待核文献 | 信息不完整或价值待确认 | 暂不作为核心依据 |

## 五、建议工作流

1. 用 `books-paths.txt`、`paper-paths.txt` 建立总文献索引。
2. 按教材目录进入主题分类索引。
3. 为 A 类、B 类文献补充内容摘要。
4. 从核心文献中提炼观点索引、概念索引、人物索引和案例索引。
5. 把所有材料对应到教材章节。
6. 整理可引用原文、页码、图像来源和教学设计。
7. 最后形成每章的“文献包”：核心文献 + 关键观点 + 重要概念 + 代表人物 + 经典案例 + 教学问题。
