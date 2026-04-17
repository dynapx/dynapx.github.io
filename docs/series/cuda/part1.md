---
date: 2026-04-18
categories:
  - CUDA系列教程
tags:
  - CUDA
  - 高性能计算
---

# CUDA 编程指南 (一)：引言与环境搭建

这是全新连载系列**《CUDA 编程指南》**的第一篇。

在这篇文章中，我们将了解什么是 CUDA，以及如何在本地配置你的第一个 GPU 并且跑通 "Hello World"。

## 为什么学习 CUDA？

随着并行计算和深度学习的爆发，GPU 算力变得越来越重要。掌握 CUDA 编程能让你压榨出显卡的极致性能。

```cpp title="hello_cuda.cu"
#include <stdio.h>

__global__ void helloFromGPU() {
    printf("Hello World from GPU!\n");
}

int main() {
    helloFromGPU<<<1, 10>>>();
    cudaDeviceSynchronize();
    return 0;
}
```

> **系列提示**：通过给文章设定相同的 category，可以把它们归为一类来浏览！

[下一篇：CUDA 编程指南 (二) 👉](part2.md)