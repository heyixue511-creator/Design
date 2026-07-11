# 02-Composition 深度报告：Composition

- **执行状态**：已完成 V2.0 批量重写；来源于 `P1` 重写队列
- **建议等级**：A 类核心章节材料
- **图像状态**：含 46 处图片链接，并检测到 36 条图注/图版说明；本报告只依据 Markdown 可读文字，不补写图像视觉细节
- **源文件完整路径**：`00-books/Designing Mobile Interfaces _ Patterns for Interaction -- Hoober, Steven; Berkma/02-Composition.md`
- **报告文件路径**：`00-books-result/Designing Mobile Interfaces _ Patterns for Interaction -- Hoober, Steven; Berkma/02-Composition.md`
- **文件类型**：学术专著或论文型章节
- **文本完整性**：109426 字符；存在断词或 OCR 连字痕迹；存在数字/字母混淆痕迹
- **相邻文件关系**：前序 `00-books/Designing Mobile Interfaces _ Patterns for Interaction -- Hoober, Steven; Berkma/01-Preface.md`；后续 `00-books/Designing Mobile Interfaces _ Patterns for Interaction -- Hoober, Steven; Berkma/03-Components.md`

## 1. 源文核验与内容概述

已重新读取对应 `00-books/` Markdown 源文。本报告不依据旧短报告扩写，而以源文件标题、段落、小标题、图注和可读注释为证据边界。

| 层级 | 标题 |
|---:|---|
| 1 | Composition |
| 2 | A Little Bit of History |
| 2 | A Revolution Has Begun |
| 2 | Composition Principles |
| 2 | The Concept of a Wrapper |
| 2 | Context Is Key |
| 2 | Patterns for Composition |
| 2 | Scroll |
| 2 | Annunciator Row |
| 2 | Notifications |
| 2 | Titles |
| 2 | Revealable Menu |
| 2 | Fixed Menu |
| 2 | Home & Idle Screens |
| 2 | Lock Screen |
| 2 | Interstitial Screen |
| 2 | Advertising |
| 2 | Scroll |
| ... | 另有 65 个标题未在此表展开 |

源文开端可读内容显示：To many people the year 1440 signifies a major shift in global communication. It was during this time in Mainz, Germany, that a goldsmith by the name of Johannes Gutenberg...

源文末段或末尾可读内容显示：This appendix provides additional information on appropriate use of message display characteristics, including typography, legibility, and readability guidelines, as well as...

从全文高频词和关键句看，本文主要围绕 “Composition”所指向的文献主题 展开。需要注意，这一判断是对源文词汇、标题和段落结构的归纳，不等同于外部知识补充。

源文中检测到的注释/书目信号：有；若用于正式论文引文，仍需回到原书页码和注释系统复核。

## 2. 文献性质、作者立场与史料等级

该文件在本仓库中应按“学术专著或论文型章节”处理。其史料等级建议为“A 类核心章节材料”：

该文件提供作者在当前切片中的历史叙述、概念判断与案例组织。报告区分作者论断、可核事实、图像线索和后续分析，不把章节观点自动视为中立事实。

本报告撰写者的判断只覆盖当前切片内已经出现的内容。人物身份、作品年代、机构归属和页码均应在进入论文、教材或数据库前再做版本核验。

## 3. 语义深度分析

### 3.1 核心命题

标题、小标题、段落重心与高频概念共同表明，当前切片集中处理 “Composition”所指向的文献主题。分析范围严格限定在“Composition”及本文件可读内容；相邻章节、外部常识和作者其他著作不补入当前结论。

### 3.2 关键论证句与证据线索

| 序号 | 源文关键句/段落抓手 | 可支持的分析方向 |
|---:|---|---|
| 1 | Advertising in mobile must be: • Clearly differentiated from the content • Clear, readable, legible, and able to be interacted with • In the same place, and used in the same way... | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 2 | Just some of the variety—and similarity—of Annunciator Rows, Notifications, Menus, and other device-wide features built into mobile device The invention of the letterpress not... | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 3 | A conventional order has arisen, from left to right: • Radios: – Mobile networks – WiFi – Bluetooth enabled, and active – NFC or contactless payment enabled – IrDA or other... | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 4 | Thumbnail List Icon Link Mobile devices must enter The Lock Screen is displayed a lock/sleep state to reduce immediately after a deliberate power consumption, to user-initiated... | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 5 | When determining which information belongs in the wrapper, you must decide on a multitude of things regarding context of use: • The technological, functional, and business... | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 6 | Presentation details Scroll indicators are not usually used in mobile devices to enable scrolling, but to: • Provide an affordance communicate the function that the area is... | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 7 | For indicators without scroll bars, the size of the indicator must often remain relatively small to avoid obscuring information; a relative size change may still be possible, but... | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 8 | When the user selects a key, selects a small on-screen element, or performs a gesture, an option menu is displayed with content relevant to the current state of the application. | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |

### 3.3 章节结构中的论证层级

| 源文章节/段落 | 内容抓手 | 报告判断 |
|---|---|---|
| A Little Bit of History | It was during this time in Mainz, Germany, that a goldsmith by the name of Johannes Gutenberg invented one of the most important industrial machines of the... | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| A Revolution Has Begun | This, the invention of modern typography, marked the birth of mass printing. | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| Composition Principles | Just some of the variety—and similarity—of Annunciator Rows, Notifications, Menus, and other device-wide features built into mobile device The invention of the... | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| The Concept of a Wrapper | The templates that are used across a product, on most every page of a website or application, we call a wrapper because they enclose wrap around all the other... | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| Context Is Key | When determining which information belongs in the wrapper, you must decide on a multitude of things regarding context of use: • The technological, functional... | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| Patterns for Composition | Figure 1-1 shows a selection of key components. | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| Scroll | When information on a page exceeds the viewport, a scroll bar control may be required to access the additional information. | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| Annunciator Row | This displays the status of hardware features on the top of each page. | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| Notifications | These notification displays must allow for user interaction. | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| Titles | Pages, content, and elements that require labels should use titles. | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| ... | 另有 61 个小节未在表中展开 | 后续精引时应回到源文逐节核验 |

从结构上看，报告应避免只写“本文讨论某主题”这种旧式短摘要。更可靠的读法是：先确认文本类型和切片边界，再把标题/小标题当作论证层级，把高频概念当作议题线索，把图注、注释和案例名当作可核验材料。这样才能区分源文事实、作者判断和后续研究者的再阐释。

## 4. 知识要素解构与术语标准化

### A. 知识要素表

| 要素类型 | 原文名称 | 标准英文／原文名 | 原文语境 | 可归入议题 | 证据状态 |
|---|---|---|---|---|---|
| 人物／机构／作品线索 | Little Bit | Little Bit | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | History To | History To | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Johannes Gutenberg | Johannes Gutenberg | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | China and Japan | China and Japan | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Bi Sheng | Bi Sheng | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Revolution Has Begun Gutenberg | Revolution Has Begun Gutenberg | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Composition Principles Figure | Composition Principles | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Annunciator Rows | Annunciator Rows | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | The Concept | The Concept | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Wrapper Throughout | Wrapper Throughout | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Context Is Key Figure | Context Is Key | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Patterns for Composition Using | Patterns for Composition Using | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Scroll When | Scroll When | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Annunciator Row This | Annunciator Row This | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 概念／议题 | screen | screen | 全文高频或关键议题词，出现约 149 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | menu | menu | 全文高频或关键议题词，出现约 120 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | will | will | 全文高频或关键议题词，出现约 90 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | display | display | 全文高频或关键议题词，出现约 88 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | user | user | 全文高频或关键议题词，出现约 86 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | must | must | 全文高频或关键议题词，出现约 78 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | devices | devices | 全文高频或关键议题词，出现约 76 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | content | content | 全文高频或关键议题词，出现约 67 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | information | information | 全文高频或关键议题词，出现约 66 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | scroll | scroll | 全文高频或关键议题词，出现约 66 次 | 章节核心议题或索引线索 | 已在源文中出现 |

### B. 术语与关键词

源文高频词包括：screen(149)、menu(120)、will(90)、display(88)、user(86)、must(78)、devices(76)、content(67)、information(66)、scroll(66)、device(65)、page(63)。

这些词不应被机械翻译为固定理论标签。更稳妥的处理方式是保留英文原词或源文用语，并在报告、索引或教学条目中说明它在当前章节中的具体语境。例如，同一个 `style` 可能指风格制度、商品外观、历史复兴样式或作者批判对象；同一个 `design` 也可能指职业实践、人工物规划、形式判断或社会技术过程。

## 5. 实证材料、案例与图像线索

| 图注/案例线索 | 使用边界 |
|---|---|
| Just some of the variety—and similarity—of Annunciator Rows, Notifications, Menus, and other device-wide features built into mobile device | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| The lock screen on this device is as informative in presentation, and gestural in interaction, as the rest of the experience. Even notifying the user of an error on entering the code is organic to the design. Apply your... | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| Scroll indicators may be complete bars, or simple indicators floating over the content. | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| A thumbnail may be a better way to indicate location within a large area, and may also be used to jump to other regions. Here, a full desktop-view website is in the corner, while a zoomed-in view of a small portion... | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| Two types of two-axis scrolling. For items like images where both axes are equal, scroll bars must be equally easy to see and use. Make sure they are not obscured by options menus and other items, as shown to the left... | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| The Annunciator Row is a strip anchored across the top of the viewport. Note that the scroll bar stops at the Annunciator Row, as it does not scroll. | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| Common icons for the vast majority of conditions shown in the Annunciator Row. All items are enabled and at maximum graphical mode. This is an example; some are in conflict with one another, so this would never be seen... | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| A series of exemplary statuses for the battery, from full to empty, then charging. Using the exclamation point in the icon is clearer than blinking the icon, and is a second code for users or conditions where red is not... | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| These are just some of the many ways battery charge level is depicted on mobile devices. Many are quite unreadable. Try to pick simple, easy-to-understand symbols, and reuse common icon styles from existing products and... | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| Since mobiles generally have limited space, and notifications must usually be assumed to be secondary to the current process, even a dedicated notification area should be out of the way. When the notification area is... | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| ... | 另有 26 条图注未展开。 |

可进入后续数据库或教学索引的材料包括：章节标题、可读小标题、反复出现的关键词、人物/机构/作品名、图注文字和注释线索。不能直接进入可靠事实库的内容包括：未核页码的引文、OCR 可能误读的人名、只由图片文件名推断出的作品信息，以及源文没有明确说明的年代和因果关系。

## 6. 可用边界与不可用边界

| 类型 | 可用结论 | 不可越界 |
|---|---|---|
| 源文核验 | 当前报告已读取 `00-books/Designing Mobile Interfaces _ Patterns for Interaction -- Hoober, Steven; Berkma/02-Composition.md`，可确认其大致结构、标题、关键词和可读段落 | 不代表已核对原 PDF 页码、扫描图像和印刷版版式 |
| 语义分析 | 可把本文纳入 “Composition”所指向的文献主题 的议题网络 | 不应把同书其他章节或作者其他著作的观点补入当前切片 |
| 知识要素 | 可抽取人物、机构、作品、技术、媒介和概念线索 | 不应把自动抽取实体直接当作权威规范名 |
| 图像材料 | 可记录 Markdown 图注和图片链接存在 | 不应描述未实际查看的图像视觉细节 |

## 7. 教材、研究与索引用途

本文件适合用于：“Composition”所指向的文献主题 的章节导读、关键词索引、案例线索整理和设计史/设计理论课程的材料入口。若用于课堂讲授，可先以源文标题和小标题建立问题框架，再选取关键句回读，让学生区分作者论证、案例证据和后续解释。

若用于研究写作，建议把本报告当作“复审入口”而非最终引文依据：进入写作前应回到源 Markdown 和原 PDF，补齐页码、注释、图版编号、译名和版本信息。

## 8. 可引用内容与不可确认内容

可引用范围限于源文明确出现的标题、人物、机构、作品、案例、图注、数据和作者判断；直接引语必须回原书补页码。不可确认的内容包括仅由文件名推断的主题、未查看图片的视觉细节、OCR 可疑专名，以及当前切片没有展开的因果关系。

## 9. 技术核验与证据边界

源文件共约 109426 个字符；存在断词或 OCR 连字痕迹；存在数字/字母混淆痕迹。含 46 处图片链接，并检测到 36 条图注/图版说明；本报告只依据 Markdown 可读文字，不补写图像视觉细节。相邻文件为前序 `00-books/Designing Mobile Interfaces _ Patterns for Interaction -- Hoober, Steven; Berkma/01-Preface.md`、后续 `00-books/Designing Mobile Interfaces _ Patterns for Interaction -- Hoober, Steven; Berkma/03-Components.md`。正式使用前需核对原 PDF 页码、注释、图版和版本信息。

## 10. 复审结论

本报告已重新读取 `00-books/Designing Mobile Interfaces _ Patterns for Interaction -- Hoober, Steven; Berkma/02-Composition.md`，并按“学术专著或论文型章节”的实际信息结构完成 V2.0 重写。当前可作为 “Composition”所指向的文献主题 的研究入口；自动抽取的专名、术语和证据关系已保留复核标记，不替代原书精读与正式引文核验。
