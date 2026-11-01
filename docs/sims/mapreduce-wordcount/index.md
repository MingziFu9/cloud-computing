---
title: MapReduce 词频统计
description: 一步一步演示 MapReduce 统计词频的分片、Map、Shuffle、Reduce 和输出过程，数据与实验 2-4 一致（第 2 章）
---

# MapReduce 词频统计

<iframe class="sim-frame" src="main.html" height="600" loading="lazy" title="MapReduce 词频统计"></iframe>

[全屏打开](main.html){ target=_blank } · 对应教材：[2.3.3.2 MapReduce 工作流程](../../chapters/02-core-technologies/2-3.md#2332) · [实验 2-4](../../chapters/02-core-technologies/labs.md#2-4)

## 教学说明

**学习目标**

1. 能说出 MapReduce 的四个阶段及各自做什么（记忆）；
2. 能解释为什么同一个键必须交给同一个 Reduce（理解）。

**画面与操作**

- 文本框中每一行是一个输入分片，可以改成自己的句子（词之间用空格隔开）。
- 点“下一步”依次显示：3 个分片、3 个 Map 的输出、2 个 Reduce 收到的分组、Reduce 的汇总、最终结果；“自动播放”每 2.2 秒前进一步。
- “云计算”一词始终用橙色标出，便于追踪。

**数据来源**：默认的三句话、分组规则（按词的 UTF-8 字节和对 2 取余）与实验 2-4 的程序完全一致。编者核对过：动画中 Reduce-0 收到 8 个词、Reduce-1 收到 13 个词，最终 21 个不同的词、27 个词次，与实验 2-4 的实测输出相同。

**课堂用法建议**

1. 先播放一遍，再让学生预测：如果把第一行改成“云计算 云计算 云计算”，最终“云计算”的计数是多少？
2. 配合实验 2-4，对照程序代码和动画的每一步。
