# 13-Text and Character Input 深度报告：Text and Character Input

- **执行状态**：已完成 V2.0 批量重写；来源于 `P1` 重写队列
- **建议等级**：A 类核心章节材料
- **图像状态**：含 28 处图片链接，并检测到 23 条图注/图版说明；本报告只依据 Markdown 可读文字，不补写图像视觉细节
- **源文件完整路径**：`00-books/Designing Mobile Interfaces _ Patterns for Interaction -- Hoober, Steven; Berkma/13-Text and Character Input.md`
- **报告文件路径**：`00-books-result/Designing Mobile Interfaces _ Patterns for Interaction -- Hoober, Steven; Berkma/13-Text and Character Input.md`
- **文件类型**：学术专著或论文型章节
- **文本完整性**：66848 字符；存在断词或 OCR 连字痕迹；存在数字/字母混淆痕迹
- **相邻文件关系**：前序 `00-books/Designing Mobile Interfaces _ Patterns for Interaction -- Hoober, Steven; Berkma/12-Input and Output.md`；后续 `00-books/Designing Mobile Interfaces _ Patterns for Interaction -- Hoober, Steven; Berkma/14-General Interactive Controls.md`

## 1. 源文核验与内容概述

已重新读取对应 `00-books/` Markdown 源文。本报告不依据旧短报告扩写，而以源文件标题、段落、小标题、图注和可读注释为证据边界。

| 层级 | 标题 |
|---:|---|
| 1 | Text and Character Input |
| 2 | Slow Down, You’re Too Fast! |
| 2 | An Improved Design? |
| 2 | Failed Impact |
| 2 | The Status Quo |
| 2 | Use What’s Best for You |
| 2 | Text and Character Input on Mobile Devices |
| 2 | Patterns for Text and Character Input Controls |
| 2 | Keyboards & Keypads |
| 2 | Pen Input |
| 2 | Mode Switches |
| 2 | Input Method Indicator |
| 2 | Autocomplete & Prediction |
| 2 | Keyboards & Keypads |
| 2 | Problem |
| 2 | Solution |
| 2 | Variations |
| 2 | Hardware/virtual |
| ... | 另有 41 个标题未在此表展开 |

源文开端可读内容显示：Some say he was doing it to annoy the writers. He may argue that it was because the adjacent alphabetized keys kept jamming up due to interference when people were typing too...

源文末段或末尾可读内容显示：Do not violate the principles of Cancel Protection and allow destructive automatic behaviors without a method to revert or correct the change. For example, whenever automatic...

从全文高频词和关键句看，本文主要围绕 “Text and Character Input”所指向的文献主题 展开。需要注意，这一判断是对源文词汇、标题和段落结构的归纳，不等同于外部知识补充。

源文中检测到的注释/书目信号：有；若用于正式论文引文，仍需回到原书页码和注释系统复核。

## 2. 文献性质、作者立场与史料等级

该文件在本仓库中应按“学术专著或论文型章节”处理。其史料等级建议为“A 类核心章节材料”：

该文件提供作者在当前切片中的历史叙述、概念判断与案例组织。报告区分作者论断、可核事实、图像线索和后续分析，不把章节观点自动视为中立事实。

本报告撰写者的判断只覆盖当前切片内已经出现的内容。人物身份、作品年代、机构归属和页码均应在进入论文、教材或数据库前再做版本核验。

## 3. 语义深度分析

### 3.1 核心命题

标题、小标题、段落重心与高频概念共同表明，当前切片集中处理 “Text and Character Input”所指向的文献主题。分析范围严格限定在“Text and Character Input”及本文件可读内容；相邻章节、外部常识和作者其他著作不补入当前结论。

### 3.2 关键论证句与证据线索

| 序号 | 源文关键句/段落抓手 | 可支持的分析方向 |
|---:|---|---|
| 1 | In this chapter, we will discuss the following patterns: Keyboards & Keypads Provides guidelines for text and numeric entry on mobile devices that use physical and virtual... | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 2 | However, these will require learning, and so should be used as a secondary method in most cases; continue to provide keys for these functions as well. | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 3 | These can impede text entry enough that text-related functions are underutilized or alternative entry methods are used, and they can be so obscure that users cannot access certain... | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 4 | When the mode switch key is pressed, it remains active for a single character entry keystroke, after which it deactivates and the entire entry panel returns to the default state. | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 5 | Input Method Indicator Problem You must make the user aware of the current mode of the selected input method, and of any limits on selecting modes for a particular entry field. | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 6 | Labels must not only clearly explain the current mode, but also should be designed to associate with one another so that changes do not confuse the user. | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 7 | A variety of keyboard layouts, including two tablet methods, a 10-foot UI using remote gestures and prediction, a virtual keypad with entry mode indicator, and a press-and-hold... | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 8 | Patterns for Text and Character Input Controls Using text and character input functions appropriately will increase efficiency, performance, and user satisfaction. | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |

### 3.3 章节结构中的论证层级

| 源文章节/段落 | 内容抓手 | 报告判断 |
|---|---|---|
| Slow Down, You’re Too Fast! | He may argue that it was because the adjacent alphabetized keys kept jamming up due to interference when people were typing too fast. | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| An Improved Design? | In the 1930s, August Dvorak and his colleagues at the University of Washington were determined to create a new and improved keyboard layout. | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| Failed Impact | Many critics have discounted Dvorak’s findings that his keyboard improved performance. | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| The Status Quo | A variety of keyboard layouts, including two tablet methods, a 10-foot UI using remote gestures and prediction, a virtual keypad with entry mode indicator, and... | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| Use What’s Best for You | As we just discussed, even though more efficient ways to input text may exist, it’s essential to understand that people will use what they are comfortable with. | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| Text and Character Input on Mobile Devices | Use assistive technology such as auto-complete and prediction during text entry. | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| Patterns for Text and Character Input Controls | Using text and character input functions appropriately will increase efficiency, performance, and user satisfaction. | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| Keyboards & Keypads | Provides guidelines for text and numeric entry on mobile devices that use physical and virtual keyboards and keypads | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| Pen Input | Provides an alternative input method for users who are less familiar with keyboards or are more comfortable writing in gestures | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| Mode Switches | Expands the capabilities of a keyboard or keypad without using up additional screen or hardware space | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| ... | 另有 43 个小节未在表中展开 | 后续精引时应回到源文逐节核验 |

从结构上看，报告应避免只写“本文讨论某主题”这种旧式短摘要。更可靠的读法是：先确认文本类型和切片边界，再把标题/小标题当作论证层级，把高频概念当作议题线索，把图注、注释和案例名当作可核验材料。这样才能区分源文事实、作者判断和后续研究者的再阐释。

## 4. 知识要素解构与术语标准化

### A. 知识要素表

| 要素类型 | 原文名称 | 标准英文／原文名 | 原文语境 | 可归入议题 | 证据状态 |
|---|---|---|---|---|---|
| 人物／机构／作品线索 | Text and Character Input Slow Down | Text and Character Input Slow Down | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Too Fast | Too Fast | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Christopher Latham Sholes | Christopher Latham Sholes | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | James Densmore | James Densmore | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Sholes & Glidden Type-Writer | Sholes & Glidden Type-Writer | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Remington and Sons | Remington and Sons | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | TYPE WRITER | TYPE WRITER | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Remington No | Remington No | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | An Improved Design | An Improved Design | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | August Dvorak | August Dvorak | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | University of Washington | University of Washington | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Dvorak Simplified Keyboard DSK | Dvorak Simplified Keyboard DSK | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Failed Impact Many | Failed Impact Many | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | US Navy Department | US Navy Department | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 概念／议题 | input | input | 全文高频或关键议题词，出现约 144 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | mode | mode | 全文高频或关键议题词，出现约 102 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | entry | entry | 全文高频或关键议题词，出现约 93 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | will | will | 全文高频或关键议题词，出现约 79 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | user | user | 全文高频或关键议题词，出现约 66 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | keyboard | keyboard | 全文高频或关键议题词，出现约 57 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | keys | keys | 全文高频或关键议题词，出现约 49 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | text | text | 全文高频或关键议题词，出现约 48 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | method | method | 全文高频或关键议题词，出现约 48 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | used | used | 全文高频或关键议题词，出现约 41 次 | 章节核心议题或索引线索 | 已在源文中出现 |

### B. 术语与关键词

源文高频词包括：input(144)、mode(102)、entry(93)、will(79)、user(66)、keyboard(57)、keys(49)、text(48)、method(48)、used(41)、must(40)、character(38)。

这些词不应被机械翻译为固定理论标签。更稳妥的处理方式是保留英文原词或源文用语，并在报告、索引或教学条目中说明它在当前章节中的具体语境。例如，同一个 `style` 可能指风格制度、商品外观、历史复兴样式或作者批判对象；同一个 `design` 也可能指职业实践、人工物规划、形式判断或社会技术过程。

## 5. 实证材料、案例与图像线索

| 图注/案例线索 | 使用边界 |
|---|---|
| A variety of keyboard layouts, including two tablet methods, a 10-foot UI using remote gestures and prediction, a virtual keypad with entry mode indicator, and a press-and-hold method to get to optional characters. | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| Writing methods can be useful for inconvenient environments, users not accustomed to typing, annotations or nonlinear editing, or ergonomic reasons. Writing with the finger is available on some devices, and may become a... | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| A variety of slide or fold-out keyboards found on mobile phones. These include conventional individual keys with backlight, transparent keys with ePaper labels, and membrane panels. The arrangements of each are... | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| A typical mobile device numeric keypad is coordinated with direction keys and other functions such as Talk and End, soft keys, and so on. This keypad is for use in North America, as the letter labels comply with the... | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| Numerous keyboard layouts can be devised to fit the space available, and still provide a meaningful experience for the user. This virtual keyboard is fairly full-size, with number keys, and symbols assigned to each of... | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| For more compressed spaces, keyboards often lose the dedicated number row. You can make up for this by switching modes to a number entry or function key mode. This is a virtual keyboard, so alternative labels are not... | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| An example of how the multitap or “triple-tap” text entry method works | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| This keyboard has a “Back” button immediately adjacent to other keys, where it can be accidentally hit. Without an Exit Guard this can cause catastrophic failures, discarding large amounts of user-entered data. | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| Word entry with pens will appear in an input panel, occupying part of the screen. Options such as the mode switches and special characters appear as buttons within this panel. Translation candidates appear beneath the... | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| Letter input divides the input panel into discrete entry areas. Each character displays a translated candidate. One way to handle correction is for optional translations to be offered in a list. If the best guess is... | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| ... | 另有 13 条图注未展开。 |

可进入后续数据库或教学索引的材料包括：章节标题、可读小标题、反复出现的关键词、人物/机构/作品名、图注文字和注释线索。不能直接进入可靠事实库的内容包括：未核页码的引文、OCR 可能误读的人名、只由图片文件名推断出的作品信息，以及源文没有明确说明的年代和因果关系。

## 6. 可用边界与不可用边界

| 类型 | 可用结论 | 不可越界 |
|---|---|---|
| 源文核验 | 当前报告已读取 `00-books/Designing Mobile Interfaces _ Patterns for Interaction -- Hoober, Steven; Berkma/13-Text and Character Input.md`，可确认其大致结构、标题、关键词和可读段落 | 不代表已核对原 PDF 页码、扫描图像和印刷版版式 |
| 语义分析 | 可把本文纳入 “Text and Character Input”所指向的文献主题 的议题网络 | 不应把同书其他章节或作者其他著作的观点补入当前切片 |
| 知识要素 | 可抽取人物、机构、作品、技术、媒介和概念线索 | 不应把自动抽取实体直接当作权威规范名 |
| 图像材料 | 可记录 Markdown 图注和图片链接存在 | 不应描述未实际查看的图像视觉细节 |

## 7. 教材、研究与索引用途

本文件适合用于：“Text and Character Input”所指向的文献主题 的章节导读、关键词索引、案例线索整理和设计史/设计理论课程的材料入口。若用于课堂讲授，可先以源文标题和小标题建立问题框架，再选取关键句回读，让学生区分作者论证、案例证据和后续解释。

若用于研究写作，建议把本报告当作“复审入口”而非最终引文依据：进入写作前应回到源 Markdown 和原 PDF，补齐页码、注释、图版编号、译名和版本信息。

## 8. 可引用内容与不可确认内容

可引用范围限于源文明确出现的标题、人物、机构、作品、案例、图注、数据和作者判断；直接引语必须回原书补页码。不可确认的内容包括仅由文件名推断的主题、未查看图片的视觉细节、OCR 可疑专名，以及当前切片没有展开的因果关系。

## 9. 技术核验与证据边界

源文件共约 66848 个字符；存在断词或 OCR 连字痕迹；存在数字/字母混淆痕迹。含 28 处图片链接，并检测到 23 条图注/图版说明；本报告只依据 Markdown 可读文字，不补写图像视觉细节。相邻文件为前序 `00-books/Designing Mobile Interfaces _ Patterns for Interaction -- Hoober, Steven; Berkma/12-Input and Output.md`、后续 `00-books/Designing Mobile Interfaces _ Patterns for Interaction -- Hoober, Steven; Berkma/14-General Interactive Controls.md`。正式使用前需核对原 PDF 页码、注释、图版和版本信息。

## 10. 复审结论

本报告已重新读取 `00-books/Designing Mobile Interfaces _ Patterns for Interaction -- Hoober, Steven; Berkma/13-Text and Character Input.md`，并按“学术专著或论文型章节”的实际信息结构完成 V2.0 重写。当前可作为 “Text and Character Input”所指向的文献主题 的研究入口；自动抽取的专名、术语和证据关系已保留复核标记，不替代原书精读与正式引文核验。
