def count_words(filename):
    """计算一个文件大概包含多少单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file %s does not exist." % filename
        print(msg)
    else:
        # 计算文件包含多少单词
        words = contents.split()
        number = len(words)
        print("The file %s has about %s words." % (filename, str(number)))


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'programming.txt']
for filename in filenames:
    count_words(filename)
