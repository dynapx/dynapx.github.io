---
date: 2026-04-16
categories:
  - 技术分享
tags:
  - Python
  - 编程技巧
  - 进阶指南
---
# 🚀 Python 进阶：如何写出更优雅的代码

在日常进行 Python 开发时，我们总会遇到一些可以优化的地方。今天分享几个让代码变得更“Pythonic”的技巧，同时也是为了测试一下我博客的全新代码高亮和选项卡功能！

<!-- more -->

## 1. 使用列表推导式 (List Comprehension)

与其使用多行的 `for` 循环追加列表，不如尝试列表推导式，代码更紧凑也更具可读性。

=== "传统写法"
``python title="old_way.py" squares = [] for i in range(10): if i % 2 == 0: squares.append(i * i) print(squares) ``

=== "优雅写法"
``python title="new_way.py" # 结合了循环和条件判断，只需一行代码！ squares = [i * i for i in range(10) if i % 2 == 0] print(squares) ``

## 2. 善用数据类对象 (Data Classes)

在 Python 3.7+ 中，引入了 `dataclasses` 模块，极大简化了类的定义，省去了手写 `__init__` 和 `__repr__` 的烦恼。

!!! tip "悬浮动效测试"

把你的鼠标放在这个提示框上，看看是不是有一个轻微上浮的阴影反馈？这是我们在 CSS 里专门添加的微交互哦！



```python
from dataclasses import dataclass

@dataclass
class User:
    username: str
    email: str
    age: int = 18
  
    def display(self):
        print(f"[{self.username}] - {self.email}")

# 创建实例非常简单，自带好看的打印格式
user = User("dynapx", "dynapx@github.io")
print(user)
```

## 3. 待办事项检查

这也顺便测试一下我们的 Markdown 任务列表功能：

- [X] 配置 MkDocs 基础环境
- [X] 安装 Material 主题
- [X] 注入动态 CSS 和打字机 JS 特效
- [ ] 接入评论系统 (Giscus / Gitalk)
- [ ] 部署到 GitHub Pages 主分支

希望这些小技巧对你有帮助！记得使用代码块右上角的**一键复制**功能把代码带走试试。
