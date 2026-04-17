import os
import glob
import yaml

def define_env(env):
    """
    这是 mkdocs-macros-plugin 的入口。
    我们可以在这里定义 Python 方法，并在 Markdown 中直接调用来进行统计等操作。
    """
    @env.macro
    def get_blog_stats():
        docs_dir = os.path.join(env.project_dir, 'docs')

        # 统计博客数量
        blog_dir = os.path.join(docs_dir, 'blog', 'posts')
        blog_count = len(glob.glob(os.path.join(blog_dir, '*.md'))) if os.path.exists(blog_dir) else 0

        # 统计日常随笔数量
        essay_dir = os.path.join(docs_dir, 'essays')
        # 排除 index.md 目录页
        essay_count = len([f for f in glob.glob(os.path.join(essay_dir, '*.md')) if not f.endswith('index.md')]) if os.path.exists(essay_dir) else 0

        return blog_count, essay_count

    @env.macro
    def build_essay_directory():
        docs_dir = os.path.join(env.project_dir, 'docs')
        essay_dir = os.path.join(docs_dir, 'essays')
        if not os.path.exists(essay_dir):
            return ""

        md_files = [f for f in os.listdir(essay_dir) if f.endswith('.md') and f != 'index.md']
        lines = []

        for md_file in md_files:
            file_path = os.path.join(essay_dir, md_file)
            title = md_file.replace('.md', '')
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # 提取 YAML title
                if content.startswith('---'):
                    parts = content.split('---')
                    if len(parts) >= 3:
                        try:
                            fm = yaml.safe_load(parts[1])
                            if fm and 'title' in fm:
                                title = fm['title']
                        except:
                            pass
                
                # 如果依然没找到 title 尝试 #
                if title == md_file.replace('.md', ''):
                    for line in content.split('\n'):
                        if line.startswith('# '):
                            title = line[2:].strip()
                            break
                            
            # MkDocs 会将指向 .md 文件的链接自动转换为实际网页链接
            lines.append(f"- [{title}]({md_file})")
            
        return "\n".join(lines) if lines else "- 暂无随笔"
