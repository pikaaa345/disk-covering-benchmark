# 运行与交付条件

这是一份源码与说明材料包，不是 AI Skill 安装包，也不包含圆盘覆盖求解算法。无需安装、管理员权限、GUI或第三方Python依赖。下载材料需要网络；指纹生成、自检与计分可离线运行。

| 目标 | 运行需求 | 本次验证 |
|---|---|---|
| Windows x64 | Python 3.9+，PowerShell/CMD，标准库 | Windows x64 / Python 3.13.13 实际自检 |
| Linux | Python 3.9+，标准库 | 使用标准库和相对路径；未实际运行 |
| macOS | Python 3.9+，标准库 | 使用标准库和相对路径；未实际运行 |

先运行 python --version，再运行 python tools/check_tools.py。Python不存在或版本不足时，使用运行者选择的官方Python环境；项目不自动安装软件。读取错误时检查文件路径、UTF-8 JSON整数数组和命令参数，详细编码规则见 answer-protocol.txt。

人类入口 README.md，AI入口 AGENTS.md，机器索引 benchmark.json。下载ZIP后，在解压目录运行命令；文件名区分大小写，不需要设置工作机专用路径。无需卸载步骤，删除自己的下载副本即可。

本包只含公开题面、核对工具、协议、合成工具检查、报告Prompt、构型示意和历史摘要。未包含标准答案系数、半径小数、根隔离区间、求解代码、私人记录或原始证明包。完整数学解题能力与工具自检是不同事项。
