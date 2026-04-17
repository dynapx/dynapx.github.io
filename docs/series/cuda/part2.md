---
date: 2026-04-19
categories:
  - CUDA系列教程
tags:
  - CUDA
  - 高效计算
---

# CUDA 编程指南 (二)：线程结构与核心概念

在[上一篇文章(引言与环境搭建)](part1.md)中，我们成功跑通了 "Hello World"。今天这篇连载，我们将深入了解 CUDA 的线程层级结构。

## Grid 与 Block

CUDA 的线程是高度结构化的，由于 GPU 的架构特性，我们通常将任务切分为：
* **Grid (网格)**: 包含多个 Block，代表一次 Kernel 的启动任务。
* **Block (线程块)**: 包含数百到数千个 Thread（线程）。同一个 Block 内的线程可以共享一块名为 Shared Memory 的极速内存。
* **Thread (线程)**: 最基本的执行单元。

```cpp title="thread_index.cu"
__global__ void printThreadIndex() {
    int tid = threadIdx.x;
    int bid = blockIdx.x;
    printf("Block: %d, Thread: %d\n", bid, tid);
}
```

通过这样的多级左侧目录组织以及文章内的跳转，你可以把多篇博客内容如同**连载电子书**那般组合成一个完美的阅读体系！

[👈 上一篇：CUDA 编程指南 (一)](part1.md)