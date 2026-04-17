# 欢迎来到我的博客 👋

<h2 style="font-weight: 300;">在这里，我喜欢 <span id="typing-text" class="typed-text"></span><span class="cursor">&nbsp;</span></h2>

这是一个基于 **MkDocs** 和 **Material** 主题构建的个人空间。经过了动态交互的优化，现在的浏览体验更加接近现代 Web App！

---

{% set blog_count, essay_count = get_blog_stats() %}
<div class="grid cards" markdown>
- 📝 **体系博文：{{ blog_count }} 篇**
    包含深度技术分析、系列教程以及长篇杂谈，注重排版与深度。
    [:octicons-arrow-right-24: 去阅读博客](blog/index.md)
- 🌿 **日常随笔：{{ essay_count }} 篇**
    记录生活瞬间、一闪而逝的灵感与代码片段，纯粹且松弛。
    [:octicons-arrow-right-24: 翻阅我的随笔](essays/index.md)
</div>

---

## ✨ 新增的动态交互体验

=== "🚀 单页应用 (SPA)"
    点击导航栏或文章链接，**页面不会出现白屏刷新**，而是丝滑地直接切换内容！并且在顶部会有加载进度条提示。

=== "📋 快捷复制代码"
    所有的代码块现在右上角都拥有了**一键复制**按钮，再也不用鼠标拖拽了。

=== "💡 沉浸式动效"
    试试把鼠标悬浮到下方的提示框上？它们现在有了微妙的**浮动反馈**，首页标题也增加了**动态打字机效果**和色彩渐变。

## 🎯 功能展示区

!!! tip "可以浮动的悬浮框"
    鼠标放上来看看！我可以用来写各种备注或高亮的提醒信息哦。

```python title="hello.py"
# 鼠标移到代码块右上角试试一键复制
def greet():
    print("Welcome to my awesome blog!") 
    
greet()
```

## 如何发布文章？

在工程的 `docs/blog/posts/` 目录下创建一个新的 Markdown 文件即可。你可以前往顶部的 **[博客]** 标签栏查看我的最新文章！
