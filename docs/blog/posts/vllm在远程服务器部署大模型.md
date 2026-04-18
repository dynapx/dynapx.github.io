---
date: 2026-04-19
categories:
  - 技术分享
tags:
  - vLLM
  - 大模型部署
  - Linux
---
# 使用 vLLM 在远程服务器上部署大模型

**什么是 vLLM？**
[vLLM](https://github.com/vllm-project/vllm) 是一个开源的高效大语言模型（LLM）推理和服务引擎。它的核心突破是首创了 **PagedAttention** 技术，通过对注意力机制中的 Key 和 Value 缓存（KV Cache）进行类似操作系统的分页内存管理，极大地缓解了由于序列长度变化造成的显存碎片化与浪费。得益于这种高效的显存利用率，vLLM 能提供远超传统方案（如 HuggingFace Transformers 原生管道）的吞吐量（Throughput）及并发处理能力，可以说是当前业界低成本部署大语言模型的首选利器！

在真正实战远程部署模型时，除了享受 vLLM 极致的推理速度，我们还要兼顾一个非常现实的问题：如果 SSH 终端意外掉线了怎么办？通常连接断开会导致服务器正在运行的程序统统被“杀”掉。针对这种情况，我们需要引入 Linux 上的长连接利器——`tmux`，让 vLLM 部署更稳固。

<!-- more -->

## 1. 使用 tmux 保持远程会话

**什么是 tmux？**
`tmux` (Terminal Multiplexer) 是一款强大的终端复用神器。在远程服务器上部署大模型或者进行模型训练（炼丹）时，最担心的就是网络波动导致 SSH 意外断开，从而强制终止了正在运行的进程。而 `tmux` 可以将终端会话接管并挂载在后台，无论你是因为网络断开还是主动关闭电脑睡觉，只要服务器不关机，跑在 `tmux` 里的任务就会持续稳定运行。下次连接时，只需一条命令即可完美恢复之前的工作现场。

首先，我们需要启动一个全新的后台会话，以防网络中断导致随后启动的 vLLM 任务终止。这里用到的是 `tmux new` 命令：

- `new`：创建一个新的 tmux 会话。
- `-s`：(session name) 为这个会话指定一个名字，这样方便我们之后如果有大批量的任务，能准确找到它。

比如我们将这个会话命名为 `my_vllm_task`：

```bash
tmux new -s my_vllm_task
```

进入模型所在目录并激活对应的虚拟环境：

```bash
cd /home/njupt/PythonC/models/qwen32b
conda activate CPython
```

## 2. 启动 vLLM 服务

当我们准备好环境后，就可以启动 vLLM 推理服务了。vLLM 提供了与 OpenAI API 兼容的 API Server `vllm serve` 命令。在执行该命令前，我们需要了解一些常用的核心参数配置：

- `serve [模型路径或名称]`：指定你要加载的开源大模型，可以是 HuggingFace 上的在线库名，也可以是下载到本地的对应目录路径。
- `--host 0.0.0.0`：绑定服务器上的所有内网/外网 IP 地址，如果使用默认的 `127.0.0.1` 只能在服务器自己所在的机器上内部访问，所以要想实现远程接口调用，这一项必不可少。
- `--port 8000`：指定对外的监听端口号（默认就是 8000）。
- `--tensor-parallel-size 1`：张量并行（Tensor Parallelism，简称 TP）的数量。这里指使用几张 GPU 去切分跑这个大模型，如果是单卡用户直接设为 1 即可。
- `--gpu-memory-utilization 0.9`：指定 vLLM 能够占用的该 GPU 最大显存比例（这里设置占用 90% 的显存），剩余的 10% 留给系统或者其它基础进程。
- `--max-model-len 4096`：设置模型单次处理的最大上下文 token 长度。如果显存小报错，可以调小这个值，相反显存充裕可以调大！
- `--trust-remote-code`：部分模型（例如 Qwen）需要执行其 Hugging Face 仓库中自带的特定 Python 脚本，加上此项标志表示信任并允许执行远程代码。

理解了这些参数，我们来实际通过以下命令启动 vLLM 模型服务。这里我们需要特别说明一下：我们使用的是部署前从 HuggingFace 上下载的 **Qwen2.5-Coder-32B-Instruct** 的 GPTQ Int4 量化版本，它已经被下载并存在了当前目录的 `Qwen2.5-Coder-32B-Instruct-GPTQ-Int4/` 文件夹下。使用量化版能大幅度降低显存占用。我们将其服务挂载在 `8000` 端口：

```bash
vllm serve Qwen2.5-Coder-32B-Instruct-GPTQ-Int4/ \
  --host 0.0.0.0 \
  --port 8000 \
  --tensor-parallel-size 1 \
  --gpu-memory-utilization 0.9 \
  --max-model-len 4096 \
  --trust-remote-code 
```

## 3. 会话分离与恢复

### 安全地断开连接 (分离会话)

- **主动分离**：按下 `Ctrl+B` 组合键，松开后立刻再按一下 `D` 键。你会看到 `[detached]` 的提示，并返回到普通的 SSH 终端。此时，你可以安全地关闭 SSH 窗口或断开网络连接。
- **被动分离**：如果你的 SSH 连接因为网络波动直接断开，`tmux` 会话也会自动在后台保持运行，进程不会被杀掉。

### 重新连接并恢复会话

当你再次通过 SSH 登录到这台服务器后，可以随时重新连接到之前的 `tmux` 会话，恢复工作现场。

- **查看所有会话**：你可以列出当前所有正在运行的 tmux 会话：

  ```bash
  tmux ls
  ```
- **恢复到指定会话**：使用刚才设定的会话名重新连接：

  ```bash
  tmux attach -t my_vllm_task
  ```

---
