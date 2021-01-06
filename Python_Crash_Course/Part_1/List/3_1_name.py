"""
3-1 姓名：将一些朋友的姓名存储在一个列表中，并将其命名为 names。依次访问
该列表中的每个元素，从而将每个朋友的姓名都打印出来。
"""
names = ['hd', 'aa', 'bob', 'cc']
print(names[0])
print(names[1])
print(names[2])

"""
继续使用练习 3-1 中的列表，但不打印每个朋友的姓名，而为每人打
印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
"""
for name in names:
    print(name + ", How are you?")
