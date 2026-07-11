# 18-System Design 深度报告：System Design

- **执行状态**：已完成 V2.0 批量重写；来源于 `P1` 重写队列
- **建议等级**：A 类核心章节材料
- **图像状态**：含 18 处图片链接，并检测到 14 条图注/图版说明；本报告只依据 Markdown 可读文字，不补写图像视觉细节
- **源文件完整路径**：`00-books/Contextual Design_ Defining Customer-Centered Systems -- Beyer, Hugh, Holtzblatt/18-System Design.md`
- **报告文件路径**：`00-books-result/Contextual Design_ Defining Customer-Centered Systems -- Beyer, Hugh, Holtzblatt/18-System Design.md`
- **文件类型**：学术专著或论文型章节
- **文本完整性**：87980 字符；存在断词或 OCR 连字痕迹；存在数字/字母混淆痕迹
- **相邻文件关系**：前序 `00-books/Contextual Design_ Defining Customer-Centered Systems -- Beyer, Hugh, Holtzblatt/17-Using Data toDrive Design.md`；后续 `00-books/Contextual Design_ Defining Customer-Centered Systems -- Beyer, Hugh, Holtzblatt/19-Project Planning and16Strategy.md`

## 1. 源文核验与内容概述

已重新读取对应 `00-books/` Markdown 源文。本报告不依据旧短报告扩写，而以源文件标题、段落、小标题、图注和可读注释为证据边界。

| 层级 | 标题 |
|---:|---|
| 1 | System Design |
| 2 | KEEPING THE USER'S WORK COHERENT |
| 2 | BREAKING UP THE PROBLEM BREAKS UP THE WORK |
| 2 | A SYSTEM HAS ITS OWN COHERENCE |
| 2 | THE STRUCTURE OF A SYSTEM |
| 2 | DESIGNING STRUCTURE PRECEDES UI DESIGN |
| 2 | THE USER ENVIRONMENT DESIGN |
| 2 | REPRESENTING THE SYSTEM WORK MODEL |
| 2 | THE USER ENVIRONMENT FORMALISM IN THE DESIGN PROCESS |
| 2 | TASK-ORIENTED OR OBJECT-ORIENTED? |
| 2 | USER ENVIRONMENT FORMALISM |
| 2 | Focus area |
| 2 | Purpose |
| 2 | Functions |
| 2 | Links |
| 2 | Work objects |
| 2 | Constraints |
| 2 | Issues |
| ... | 另有 12 个标题未在此表展开 |

源文开端可读内容显示：re've understood the user's model of work, we've captured it in work models, we've envisioned new ways for people to work— but so what? How does this help us with software design?...

源文末段或末尾可读内容显示：arnla s hc has ys niot ro pa at soe ss o o r roohte thed ho es e h e ke e s es ce Turess u w ee s es s sos oe nt eins aik n suocy or a u uoy ers ur urons sks s-ue e oue stuee so...

从全文高频词和关键句看，本文主要围绕 生态与环境、功能与使用 展开。需要注意，这一判断是对源文词汇、标题和段落结构的归纳，不等同于外部知识补充。

源文中检测到的注释/书目信号：有；若用于正式论文引文，仍需回到原书页码和注释系统复核。

## 2. 文献性质、作者立场与史料等级

该文件在本仓库中应按“学术专著或论文型章节”处理。其史料等级建议为“A 类核心章节材料”：

该文件提供作者在当前切片中的历史叙述、概念判断与案例组织。报告区分作者论断、可核事实、图像线索和后续分析，不把章节观点自动视为中立事实。

本报告撰写者的判断只覆盖当前切片内已经出现的内容。人物身份、作品年代、机构归属和页码均应在进入论文、教材或数据库前再做版本核验。

## 3. 语义深度分析

### 3.1 核心命题

标题、小标题、段落重心与高频概念共同表明，当前切片集中处理 生态与环境、功能与使用。分析范围严格限定在“System Design”及本文件可读内容；相邻章节、外部常识和作者其他著作不补入当前结论。

### 3.2 关键论证句与证据线索

| 序号 | 源文关键句/段落抓手 | 可支持的分析方向 |
|---:|---|---|
| 1 | If you can't write a single sentence that describes the purpose of the focus area because there are so many different functions doing different things, it's likely that the system... | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 2 | Conversely, QuickMail Pro's market message from their marketing literature is that it offers a base structure different from that of other mail products: "The 'All-in-One’Message... | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 3 | o t she Because focus areas are the most visible concept captured by a User Environment model, the model helps designers organize the sys- tem so it fits the work. | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 4 | The vision, User Environment Design, and object model are structural; they show all parts of the system and how they interrelate, though they focus on new work practice, the... | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 5 | Because the system is a mix of hardware and software, some focus areas in this User Environment represent physical hardware places as well as software screens. | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 6 | Later, when it comes time to build the object model, the functions will define the behavior these Objects in a focus area reveal the things the user works on objects must support... | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 7 | All this implies a new focus area, “See system's history," which is linked to "Work on user's request." Links are like other functions in that the user has to take an explicit... | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |
| 8 | When rolling storyboards into the User Environment Design, it's the work the storyboard represents that defines the focus areas in the User Environment. | 用于定位作者如何建立章节问题、概念关系或案例证据；正式引用需回源文核页。 |

### 3.3 章节结构中的论证层级

| 源文章节/段落 | 内容抓手 | 报告判断 |
|---|---|---|
| System Design | In Contextual Design, we introduce a new modeling technique to reveal the system work model and show how all the parts of the system relate to each other in... | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| KEEPING THE USER'S WORK COHERENT | The challenge is to keep the system work model coherent, so that it supports the users and fits with their expectations while extending and transforming their... | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| BREAKING UP THE PROBLEM BREAKS UP THE WORK | Designers find it hard not to treat their assigned part of the system as the most important—not only is their ego involved, but it is the most important part... | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| A SYSTEM HAS ITS OWN COHERENCE | The people making the paths are following their everyday life activities without thinking particularly Good design for individual work tasks is not enough... | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| THE STRUCTURE OF A SYSTEM | There's no way to keep users from expecting this approach throughout the system because the parts aren't isolated in the users' experience. | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| DESIGNING STRUCTURE PRECEDES UI DESIGN | This is what we are missing in software design—a single representation that shows how all the parts of the system relate in the users' experience and how they... | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| THE USER ENVIRONMENT DESIGN | o t she Because focus areas are the most visible concept captured by a User Environment model, the model helps designers organize the sys- tem so it fits the... | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| REPRESENTING THE SYSTEM WORK MODEL | Structure charts show the components of the system at a higher level of detail than code, but are focused on the structure of the implementation, which is not... | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| THE USER ENVIRONMENT FORMALISM IN THE DESIGN PROCESS | The User Environment Design occupies a place in the design process between storyboards on the one hand, and user interface design and object analysis on the... | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| TASK-ORIENTED OR OBJECT-ORIENTED? | If you can't write a single sentence that describes the purpose of the focus area because there are so many different functions doing different things, it's... | 该部分提供章节论证的直接证据；使用时应保留其所在小节语境。 |
| ... | 另有 17 个小节未在表中展开 | 后续精引时应回到源文逐节核验 |

从结构上看，报告应避免只写“本文讨论某主题”这种旧式短摘要。更可靠的读法是：先确认文本类型和切片边界，再把标题/小标题当作论证层级，把高频概念当作议题线索，把图注、注释和案例名当作可核验材料。这样才能区分源文事实、作者判断和后续研究者的再阐释。

## 4. 知识要素解构与术语标准化

### A. 知识要素表

| 要素类型 | 原文名称 | 标准英文／原文名 | 原文语境 | 可归入议题 | 证据状态 |
|---|---|---|---|---|---|
| 人物／机构／作品线索 | System Design | System Design | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | In Contextual Design | In Contextual Design | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | KEEPING THE USER'S WORK COHERENT The | KEEPING THE USER'S WORK COHERENT The | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Claris Emailer | Claris Emailer | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | BREAKING UP THE PROBLEM BREAKS UP THE WORK One | BREAKING UP THE PROBLEM BREAKS UP THE WORK One | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | SYSTEM HAS ITS OWN COHERENCE While | SYSTEM HAS ITS OWN COHERENCE While | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Apple's LaserWriter | Apple's LaserWriter | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | THE STRUCTURE OF | THE STRUCTURE OF | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Suppose Joe | Suppose Joe | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | DESIGNING STRUCTURE PRECEDES UI DESIGN Designing | DESIGNING STRUCTURE PRECEDES UI DESIGN Designing | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | THE USER ENVIRONMENT DESIGN Contextual Design | THE USER ENVIRONMENT DESIGN Contextual Design | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | User Environment Design UED | User Environment Design UED | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | The User Environ- | The User Environ- | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 人物／机构／作品线索 | Contextual Design | Contextual Design | 源文英文或外文专名 | 人物、设计师、作者或责任者 | 已在源文中出现，正式引用仍需页码核验 |
| 概念／议题 | user | user | 全文高频或关键议题词，出现约 227 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | system | system | 全文高频或关键议题词，出现约 213 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | focus | focus | 全文高频或关键议题词，出现约 164 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | environment | environment | 全文高频或关键议题词，出现约 129 次 | 生态与环境 | 已在源文中出现 |
| 概念／议题 | structure | structure | 全文高频或关键议题词，出现约 94 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | area | area | 全文高频或关键议题词，出现约 88 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | model | model | 全文高频或关键议题词，出现约 81 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | areas | areas | 全文高频或关键议题词，出现约 67 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | what | what | 全文高频或关键议题词，出现约 65 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 概念／议题 | different | different | 全文高频或关键议题词，出现约 62 次 | 章节核心议题或索引线索 | 已在源文中出现 |
| 议题簇 | 生态与环境、功能与使用 | 原文名同左 | 由高频词和关键句综合归纳 | 章节主题归纳 | 归纳性判断 |

### B. 术语与关键词

源文高频词包括：user(227)、system(213)、focus(164)、environment(129)、structure(94)、area(88)、model(81)、areas(67)、what(65)、different(62)、it's(61)、function(60)。

这些词不应被机械翻译为固定理论标签。更稳妥的处理方式是保留英文原词或源文用语，并在报告、索引或教学条目中说明它在当前章节中的具体语境。例如，同一个 `style` 可能指风格制度、商品外观、历史复兴样式或作者批判对象；同一个 `design` 也可能指职业实践、人工物规划、形式判断或社会技术过程。

## 5. 实证材料、案例与图像线索

| 图注/案例线索 | 使用边界 |
|---|---|
| Claris Emailer: Two ways of finding: one with a query dialog box, one with a filter. | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| A floor plan. Notice how the important distinctions are immediately apparent—the relative size of the spaces and the access between them. Details that are unimportant for understanding the structure of the house—rugs... | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| The progression from design to development. This diagram shows the process of going from work models through systems design to implementation design. It shows the alternation between sequential, story-based thinking and... | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| 5.1 The main screen of Microsoft PowerPoint and the focus area that represents it. This window creates a place in the system in which to focus on creating, viewing, and changing the content of individual slides. This... | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| shows the main window of PowerPoint, a tool for making slide presentations. This window provides a place for creating and editing the content of slides. In the User Environment Design we represent places as focus areas... | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| Links between focus areas. These three focus areas support distinct but related activities. They declare that when a user is worrying about the detailed content of one slide, she is not concerned with the overall... | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| A double link between focus areas. The double link indicates that the work done in the second focus area, spell checking, needs the context of the main focus area and that the user will switch back and forth between the... | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| Storyboard for getting help from system management. | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| A focus area representing new functions on the user's phone. | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| Function added to an existing focus area. | 可作为作品、图版或案例索引线索；图像内容需另行视觉核验。 |
| ... | 另有 4 条图注未展开。 |

可进入后续数据库或教学索引的材料包括：章节标题、可读小标题、反复出现的关键词、人物/机构/作品名、图注文字和注释线索。不能直接进入可靠事实库的内容包括：未核页码的引文、OCR 可能误读的人名、只由图片文件名推断出的作品信息，以及源文没有明确说明的年代和因果关系。

## 6. 可用边界与不可用边界

| 类型 | 可用结论 | 不可越界 |
|---|---|---|
| 源文核验 | 当前报告已读取 `00-books/Contextual Design_ Defining Customer-Centered Systems -- Beyer, Hugh, Holtzblatt/18-System Design.md`，可确认其大致结构、标题、关键词和可读段落 | 不代表已核对原 PDF 页码、扫描图像和印刷版版式 |
| 语义分析 | 可把本文纳入 生态与环境、功能与使用 的议题网络 | 不应把同书其他章节或作者其他著作的观点补入当前切片 |
| 知识要素 | 可抽取人物、机构、作品、技术、媒介和概念线索 | 不应把自动抽取实体直接当作权威规范名 |
| 图像材料 | 可记录 Markdown 图注和图片链接存在 | 不应描述未实际查看的图像视觉细节 |

## 7. 教材、研究与索引用途

本文件适合用于：生态与环境、功能与使用 的章节导读、关键词索引、案例线索整理和设计史/设计理论课程的材料入口。若用于课堂讲授，可先以源文标题和小标题建立问题框架，再选取关键句回读，让学生区分作者论证、案例证据和后续解释。

若用于研究写作，建议把本报告当作“复审入口”而非最终引文依据：进入写作前应回到源 Markdown 和原 PDF，补齐页码、注释、图版编号、译名和版本信息。

## 8. 可引用内容与不可确认内容

可引用范围限于源文明确出现的标题、人物、机构、作品、案例、图注、数据和作者判断；直接引语必须回原书补页码。不可确认的内容包括仅由文件名推断的主题、未查看图片的视觉细节、OCR 可疑专名，以及当前切片没有展开的因果关系。

## 9. 技术核验与证据边界

源文件共约 87980 个字符；存在断词或 OCR 连字痕迹；存在数字/字母混淆痕迹。含 18 处图片链接，并检测到 14 条图注/图版说明；本报告只依据 Markdown 可读文字，不补写图像视觉细节。相邻文件为前序 `00-books/Contextual Design_ Defining Customer-Centered Systems -- Beyer, Hugh, Holtzblatt/17-Using Data toDrive Design.md`、后续 `00-books/Contextual Design_ Defining Customer-Centered Systems -- Beyer, Hugh, Holtzblatt/19-Project Planning and16Strategy.md`。正式使用前需核对原 PDF 页码、注释、图版和版本信息。

## 10. 复审结论

本报告已重新读取 `00-books/Contextual Design_ Defining Customer-Centered Systems -- Beyer, Hugh, Holtzblatt/18-System Design.md`，并按“学术专著或论文型章节”的实际信息结构完成 V2.0 重写。当前可作为 生态与环境、功能与使用 的研究入口；自动抽取的专名、术语和证据关系已保留复核标记，不替代原书精读与正式引文核验。
