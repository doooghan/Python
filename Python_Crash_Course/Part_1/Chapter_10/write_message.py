"""
Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数
str()将其转换为字符串格式。
"""
filename = "programming.txt"

with open(filename, "w") as file_object:
    file_object.write("I love programming!\n")
    file_object.write("I love creating new games.\n")
