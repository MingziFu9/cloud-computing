"""实验 2-4：用 Python 模拟 MapReduce 词频统计。

不需要 Hadoop 集群：用多进程模拟多台机器，按“输入分片 → Map → Shuffle/Sort → Reduce”四步走一遍。
运行：python lab2_4_mapreduce.py
"""
from collections import defaultdict
from multiprocessing import Pool
import os

# 输入数据：3 个分片，每个分片交给一台“机器”（一个进程）处理。词与词之间已用空格分好。
SPLITS = [
    "云计算 让 计算 像 水电 一样 按需 使用",
    "虚拟化 是 云计算 的 基础 容器 让 部署 更 快",
    "分布式 存储 和 分布式 计算 支撑 云计算 的 弹性",
]


def map_task(args):
    """Map：把一行文字拆成 (词, 1) 键值对。"""
    split_id, text = args
    pairs = [(word, 1) for word in text.split()]
    log = f"[Map-{split_id}] 输出 {len(pairs)} 个键值对，前 3 个：{pairs[:3]}"
    return log, pairs, os.getpid()


def shuffle(all_pairs, n_reducers):
    """Shuffle/Sort：按词的哈希值把键值对分给不同的 Reduce，同一个词一定去同一个 Reduce。"""
    buckets = [defaultdict(list) for _ in range(n_reducers)]
    for pairs in all_pairs:
        for word, one in pairs:
            buckets[sum(word.encode("utf-8")) % n_reducers][word].append(one)
    return [dict(sorted(b.items())) for b in buckets]


def reduce_task(args):
    """Reduce：把同一个词的所有 1 加起来。"""
    reducer_id, groups = args
    result = {word: sum(ones) for word, ones in groups.items()}
    log = f"[Reduce-{reducer_id}] 收到 {len(groups)} 个词，例如 {list(groups.items())[:2]}"
    return log, result


if __name__ == "__main__":
    with Pool(3) as pool:
        mapped = pool.map(map_task, list(enumerate(SPLITS)))           # 3 个 Map 并行
        for log, _, _ in mapped:
            print(log)
        print("—— Shuffle：按词分组，交给 2 个 Reduce ——")
        groups = shuffle([pairs for _, pairs, _ in mapped], n_reducers=2)  # 分给 2 个 Reduce
        reduced = pool.map(reduce_task, list(enumerate(groups)))       # 2 个 Reduce 并行
    final = {}
    for log, part in reduced:
        print(log)
        final.update(part)
    print("\n词频最高的 5 个词：")
    for word, count in sorted(final.items(), key=lambda kv: (-kv[1], kv[0]))[:5]:
        print(f"{word}\t{count}")
    print(f"共 {len(final)} 个不同的词，{sum(final.values())} 个词次")
