file_name = "pi_digits.txt"
with open(file_name) as file_object:
    # contents = file_object.read()
    # print(contents.rstrip())
# 3.1415926535
#   8979323846
#   2643383279


    for line in file_object:
        print(0)
        print(line.rstrip())
    lines = file_object.readlines()
print("x")
print(lines)
for line in lines:
    print(1)
    print(line.rstrip())
