import sys

import difflib

try:
    textFile1 = sys.argv[1]  # 第1个配置文件路径参数
    textFile2 = sys.argv[2]  # 第2个配置文件路径参数

except Exception as e:
    print("Error:" + str(e))
    print("Usage: simple3.py filename1 filename2")
    sys.exit()


def readfile(filename):
    """文件读取分隔函数"""
    try:
        fileHandler = open(filename, "r")
        text = fileHandler.read().splitlines()
        return text
    except IOError as error:
        print("READ file Error:" + str(error))
        sys.exit()


if textFile1 == "" and textFile2 == "":
    print("Usage: simple3.py filename1 filename2")
    sys.exit()

text1_lines = readfile(textFile1)
text2_lines = readfile(textFile2)

if __name__ == "__main__":
    d = difflib.HtmlDiff()
    print(d.make_file(text1_lines, text2_lines))
    # 终端执行命令，将结果输出到 diffFile.html文件
    # python 1.3 对比Nginx配置文件差异.py 1.1 Differ-比较2个字符串差异.py 1.2 HtmlDiff-生成对比html文档.py > diffFile.html
