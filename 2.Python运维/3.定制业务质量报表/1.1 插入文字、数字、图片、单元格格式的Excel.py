import xlsxwriter

# 创建1个Excel文件
workbook = xlsxwriter.Workbook("demo1.xlsx")

# 创建1个工作表对象
worksheet = workbook.add_worksheet()

# 设定第1列(A列) 宽度为20像素
worksheet.set_column("A:A", 20)

# 定义1个加粗的格式对象
bold = workbook.add_format({"bold": True})

# A1单元格 写入 Hello
worksheet.write("A1", "Hello")

# A2单元格 写入 Word，并加粗使用bold
worksheet.write("A2", "World", bold)

# B2单元格写入中文并，并加粗使用bold
worksheet.write("B2", "中文测试", bold)

# 行列表示法的单元格下标以0作为起始值，'3，0'等价于 A3
# 用行列表示法 写入 32
worksheet.write(2, 0, 32)

# 用行列表示法 写入 35.5
worksheet.write(3, 0, 35.5)

# 求A3:A4 的和，并将结果写入'4，0'，即 A5
worksheet.write(4, 0, "=SUM(A3:A4)")

# B5单元格插入图片
worksheet.insert_image("B5", "../../assets/cat1.jpeg")

workbook.close()
