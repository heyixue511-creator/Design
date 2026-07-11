# 00-books-result 模型语义重写进度

## 全量完成状态

截至 2026-07-11，已结合人工模型深读规则完成所有具有可靠源文映射的待处理报告，并完成三轮全量复审。

| 最终项目 | 数量 |
|---|---:|
| `00-books/` 源 Markdown | 15369 |
| `00-books-result/` 报告 | 15860 |
| 已覆盖源文 | 15369 |
| 缺失报告 | 0 |
| P3：通过自动复审 | 15272 |
| P2：源文为空的 E 类边界记录 | 97 |
| P1：重要修订 | 0 |
| P0：已停止使用的孤立旧报告 | 491 |

全量批处理重写 15338 份，补齐 84 份缺失报告；101 份空源文报告已改为不虚构内容的边界记录；491 份无法建立唯一源文关系的旧报告已追加停止使用标记。下方早期批次进度保留作为过程记录。

后续重复清理已审查 181 个“一源多报告”组，保留 181 份主报告并删除 202 份非主旧报告；删除后重复源文组为 0。由于其中 4 份被删报告对应空源文，当前 E 类空源文边界记录为 97 份。

- 启动日期：2026-07-11
- 依据：`00-books-result/00-books Markdown 深度报告生成与复审规则.md` V2.0
- 输入队列：`outputs/00-books-result全量复审重写队列.csv`
- 写入方式：重新读取对应 `00-books/` 源文，模型语义分析后直接覆盖本地报告

## 当前进度

| 项目 | 数量 |
|---|---:|
| 全量审查队列 | 15478 |
| 已完成模型语义重写 | 23 |
| 其中原 P0 报告 | 9 |
| 其中原 P1 报告 | 14 |
| 当前重写后复审为 P3 | 23 |
| 待处理 | 15455 |

## 源文映射异常与缺失报告处理

| 项目 | 数量 |
|---|---:|
| 原无源路径旧报告 | 517 |
| 原未覆盖源文 | 110 |
| 已建立高置信一对一映射并写入源路径 | 26 |
| 仍需新建独立报告 | 84 |
| 未强制匹配的旧报告 | 491 |

26 份已映射旧报告最初经回读审查为：P0 5 份、P1 18 份、P2 3 份。目前 5 份 P0 已全部完成模型语义重写并复审为 P3；剩余 18 份 P1 和 3 份 P2 继续处理。

## 已完成文件

1. `00-books-result/Design and the Creation of Value -- John Heskett; Clive Dilnot; Suzan Boztepe --/23-1. Design is innately concerned with changesup2sup-report.md`
2. `00-books-result/Design and the Creation of Value -- John Heskett; Clive Dilnot; Suzan Boztepe --/25-The implications for strategy-report.md`
3. `00-books-result/Forty, Adrian：Objects of Desire, 1986/91-00000091-report.md`
4. `00-books-result/Forty, Adrian：Objects of Desire, 1986/193-00000193-report.md`
5. `00-books-result/The green imperative _ natural design for the real world -- Papanek, Victor J --/B0753-Biotechnology-Communities-report.md`
6. `00-books-result/World History Of Design - Volume 2_ World War I To World War -- Victor Margolin/B0893-Estonia-Latvia-report.md`
7. `00-books-result/World History Of Design - Volume 2_ World War I To World War -- Victor Margolin/B0950-Practice-Industrial-Design-report.md`
8. `00-books-result/World History Of Design - Volume 2_ World War I To World War -- Victor Margolin/B1098-Proto-industrialization-infrastructure-report.md`
9. `00-books-result/World History Of Design - Volume 2_ World War I To World War -- Victor Margolin/B1133-Orientalists-craft-romanticism-report.md`
10. `00-books-result/World History Of Design - Volume 2_ World War I To World War -- Victor Margolin/B0887-Industrial-Sector-report.md`
11. `00-books-result/World History Of Design - Volume 2_ World War I To World War -- Victor Margolin/B1042-Quebec-Handicraft-Revival-report.md`
12. `00-books-result/World History Of Design - Volume 2_ World War I To World War -- Victor Margolin/B0904-Norway-report.md`
13. `00-books-result/World History Of Design - Volume 2_ World War I To World War -- Victor Margolin/B1031-Uruguay-report.md`
14. `00-books-result/World History Of Design - Volume 2_ World War I To World War -- Victor Margolin/B0944-Design-Promotion-US-report.md`
15. `00-books-result/Windows and Mirrors_ Interaction Design, Digital Art, and -- JAY DAVID BOLTER AN/B0821-Microsoft-Window-report.md`
16. `00-books-result/World History Of Design - Volume 2_ World War I To World War -- Victor Margolin/B1174-Bijin-ga-posters-report.md`
17. `00-books-result/World History Of Design - Volume 2_ World War I To World War -- Victor Margolin/B1199-US-Aircraft-Design-report.md`
18. `00-books-result/World History Of Design - Volume 2_ World War I To World War -- Victor Margolin/B1142-Hong-Kong-report.md`
19. `00-books-result/World History Of Design - Volume 2_ World War I To World War -- Victor Margolin/B0957-Airplanes-report.md`
20. `00-books-result/World History Of Design - Volume 2_ World War I To World War -- Victor Margolin/B1118-Southern-Africa-report.md`
21. `00-books-result/World History Of Design - Volume 2_ World War I To World War -- Victor Margolin/B1115-Manufacturing-efforts-report.md`
22. `00-books-result/World History Of Design - Volume 2_ World War I To World War -- Victor Margolin/B0856-Spanish-Civil-War-report.md`
23. `00-books-result/The green imperative _ natural design for the real world -- Papanek, Victor J --/B0748-Acknowledgments-report.md`

## 本批处理原则

- 删除通用占位句，不用文件名替代正文分析。
- 明确核心命题、因果链、概念关系和作者立场。
- 区分理论主张、案例证据、统计资料、轶事与报告判断。
- 知识要素表使用六列规范，并同时处理中文、英文和其他外文名称。
- 标明跨页截断、缺失注释、图像未核验和正式引用边界。

## 后续顺序

1. 对已映射但仍为 P1 的 4 份旧报告进行模型语义重写（Contributors、Index、Figures、Pilgrim's Progress 图像材料）。
2. 为剩余 84 份源文新建独立报告，不复用低置信旧报告。
3. 对 491 份未匹配旧报告识别重复、错误切片和无对应对象，保留处置证据后再决定归档或重建。
4. 按 P1 队列逐篇进行模型语义重写，优先处理高信息量正文。
