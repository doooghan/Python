name = "ada lovelace"

""" 修改 """
# 首字母大写
print(name.title())

name = "Ada Lovelace"

# 所有字母大写/小写
print(name.upper())
print(name.lower())

""" 拼接 """
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello," + full_name.title() + "!")

message = "Hello," + full_name.title() + "!"
print(message)

print("Languages:\n\tPython\n\tC\n\tJava")

""" 清除空白 """
favorite_language = " Python "
print(favorite_language.strip())
print(favorite_language.lstrip())
print(favorite_language.rstrip())
