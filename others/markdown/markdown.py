import markdown

md_text = """
# This is a heading

This is some **bold** and *italic* text.

Here's a list:
- Item 1
- Item 2
- Item 3
"""

html = markdown.markdown(md_text)
print(html)
