"""
Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数
str()将其转换为字符串格式。
"""
filename = "programming.txt"

with open(filename, "a") as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
