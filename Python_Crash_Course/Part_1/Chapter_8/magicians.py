def show_magicians(magicians):
    """打印魔术师列表"""
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    """每个魔术师都是伟大的"""
    # 学到了什么,学到了可以对列表元素影响,但不能指向别的列表
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        magician = "the Great " + magician
        great_magicians.append(magician)
    return great_magicians
    # return magicians.extend(great_magicians)[:]  # not ok
    """ ok
    magicians.extend(great_magicians)
    return magicians
    """

    """not ok
    for magician in magicians:
        magician = "the Great " + magician
    """


magicians = ['hdd', 'yhh', 'hpp', 'wxx', 'znn', 'csh']
show_magicians(magicians)
print("-" * 20)
great_magicians = make_great(magicians[:])
show_magicians(magicians)
print("-" * 20)
show_magicians(great_magicians)
