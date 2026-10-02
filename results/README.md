# n=11 测试记录

**中文** · [English](README.en.md)

下表包含两次历史演示及一次独立审核判为错误的 DeepSeek 提交，不构成同口径正式榜单。历史全局证明未重跑；DeepSeek 的精确未覆盖反例已复算。模型名使用“名称/推理强度”。

| 模型 | 测试日期（UTC） | 记录的自然经过时间 | 分数（越高越好） |
|---|---|---|---:|
| [gpt-6 astra/max](https://pikaaa345.github.io/disk-covering-benchmark/record-n11-astra-20260930.zh.html) | 2026-09-30 | 主任务5小时34分29.011秒 + 独立最小多项式追加13分46.178秒，共5小时48分15.189秒 | 205 |
| [gpt-6.1 sol/max](https://pikaaa345.github.io/disk-covering-benchmark/record-n11-sol-20260930.zh.html) | 2026-09-30 | Goal 创建至完成6小时17分28秒 | 193 |
| [deepseek-v4-pro/max](https://pikaaa345.github.io/disk-covering-benchmark/record-n11-deepseek-v4-pro-max-20261002.zh.html) | 2026-10-02 | Goal 创建至最终提交10小时57分27.149秒；时限内提交错误证明 | 0 |

两条记录的计时端点不同。原主任务早于当前最小多项式题面：SOL 历史报告没有认证不可约性；Astra 历史报告另有独立追加阶段报告最小多项式。原60分钟限制均未满足，续作完成不改变超时判定。因此不能据本表宣称两模型通过同一正式合同，或证明它们之间存在稳定差距。

DeepSeek 本次原时限为12小时，提交在时限内，但所指定的精确圆心与半径存在严格未覆盖点，全局下界论证也未成立，因此计0分。报告详细说明错误章节、程序及不等式方向；原始对话和含答案的证据包留在本地。它的硬件记录来自本次报告整理时的查询。

n=11 参考哈希：**已发布于题目页**；历史测试尚未对照当前参考重跑。[公开测试报告](../docs/records.zh.html)现已展示原始输入、电脑配置、主要阶段与验收情况。原报告含数学答案，完整原文及证明包仍未公开。

机器可读记录位于 [n11.json](n11.json)，[详细时间线与输入出处](../docs/records.json)另行提供。CPU和内存采用SOL原报告整理时的配置查询；Astra使用同一台测试电脑的共享记录，未保存独立开题快照。费用仍未记录，填写 null。

测试日期用于标明测试发生时的公开资料环境。后续比较还应记录联网规则及实际使用的来源，避免将可获取资料的变化直接归为模型能力变化。

## n=12 模型测试记录

| 模型 | 测试日期（UTC） | 主任务自然经过时间 | 分数（越高越好） |
|---|---|---|---:|
| [gpt-6 astra/max](https://pikaaa345.github.io/disk-covering-benchmark/record-n12-astra-20261001.zh.html) | 2026-10-01 | 52分55.402秒（3175.402秒） | 477 |
| [gpt-6.1 sol/max](https://pikaaa345.github.io/disk-covering-benchmark/record-n12-sol-20261001.zh.html) | 2026-10-01 | 1小时30分57.272秒（5457.272秒） | 398 |

两条记录的参考答案指纹均匹配，原数学交付均在12小时时限内。发布者已明确：禁令仅针对测试开始前已经存在的本地资料；本任务中新下载、新生成的文件允许读取。既有审查未发现显式读取任务前已有研究材料、技能或其他聊天，据此保留上述成绩，删除“有条件”标记。

两模型均使用网上已有的构型、证明代码和证书，并补充代数数据或加强精确核验；不能表述为从零独立发现完整最优性证明。具体来源、新增工作、CPU、内存、原始输入及阶段记录见各自报告。单次事后记录不构成正式排名，原证明没有在本次网页修改中重新运行。

[两次测试的机器记录](n12.json)。公开版本不含数学答案，完整原始报告、审查和证明材料保留本地。

## n=13 测试记录

| 模型 | 测试日期（UTC） | 计分观测窗 | 分数（越高越好） |
|---|---|---|---:|
| [gpt-6 astra/max](https://pikaaa345.github.io/disk-covering-benchmark/record-n13-codex-20261001.zh.html) | 2026-10-01 | 12小时（43200秒）；未完成，非有效完成用时 | 0 |
| [gpt-6.1 sol/max](https://pikaaa345.github.io/disk-covering-benchmark/record-n13-sol-20261001.zh.html) | 2026-10-01 | 12小时（43200秒）；未完成，非有效完成用时 | 0 |

两条记录均未在期限内提交半径最小多项式及完整有效证明，计0分。两条模型均依据各自原Goal的运行元数据核实；Astra记录的14条配置均为gpt-6-astra、推理强度max，报告已按n=11 Astra格式修订。两次运行的工具、阶段时刻、系统计数分别保留，不混用。本次发布不重跑数学证明，不作正式排名。

[机器可读记录](n13.json) · [SOL实际计分输出](n13-sol-score-output.json) · [另一记录的计分输出](n13-score-output.json)。

## 算法系统运行记录

以下为人类与 AI 研发、优化的算法在本机的运行成绩。与上面的模型测试采用同一套计分公式，分数越高越好，可以在同一尺度上比较完成效率；具体运行条件见报告。最佳值取本次核对的三组归档共40条完整运行记录的最低用时；每条为单次观测。

| n | 算法 | 分数 | 报告 |
|---:|---|---:|---|
| 11 | DGC v62-F · MinPoly v9 | 994 | [运行报告](https://pikaaa345.github.io/disk-covering-benchmark/record-n11-algorithm-run-20261001.zh.html) |
| 12 | DGC v62-G · MinPoly v15 | 1117 | [运行报告](https://pikaaa345.github.io/disk-covering-benchmark/record-n12-algorithm-run-20261001.zh.html) |
| 14 | DGC v62-G · MinPoly v15 | 1138 | [运行报告](https://pikaaa345.github.io/disk-covering-benchmark/record-n14-algorithm-run-20261001.zh.html) |
| 16 | DGC v62-F · MinPoly v13 | 892 | [运行报告](https://pikaaa345.github.io/disk-covering-benchmark/record-n16-algorithm-run-20261001.zh.html) |
| 19 | DGC v62-G · MinPoly v15 | 1123 | [运行报告](https://pikaaa345.github.io/disk-covering-benchmark/record-n19-algorithm-run-20261001.zh.html) |
| 22 | DGC v62-G · MinPoly v15 | 1018 | [运行报告](https://pikaaa345.github.io/disk-covering-benchmark/record-n22-algorithm-run-20261001.zh.html) |
| 25 | DGC v62-G · MinPoly v15 | 883 | [运行报告](https://pikaaa345.github.io/disk-covering-benchmark/record-n25-algorithm-run-20261001.zh.html) |
| 26 | DGC v62-G · MinPoly v15 | 760 | [运行报告](https://pikaaa345.github.io/disk-covering-benchmark/record-n26-algorithm-run-20261001.zh.html) |

n=25仍为候选上界，n=26的全局证明来源复核未完成。分数不代表这两题已完成严格验收。报告列出CPU、内存、证明引擎、代数引擎、阶段计时和最新32核复测。
