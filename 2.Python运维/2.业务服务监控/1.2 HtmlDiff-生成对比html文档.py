import difflib

text1 = """
a
b
c
d
e
f
g
"""

text2 = """
A
B
C
D
E
F
g
"""

if __name__ == "__main__":
    d = difflib.HtmlDiff()
    print(d.make_file(text1, text2))
    # 终端执行命令，将输出结果重定向到 diff.html 文件
    # python 1._HtmlDiff - 生成对比html文档.py > diff.html