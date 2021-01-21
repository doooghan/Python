def show_magicians(magicians):
    """打印魔术师列表"""
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    """每个魔术师都是伟大的"""
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        magician = "the Great " + magician
        great_magicians.append(magician)

    """not ok
    for magician in magicians:
        magician = "the Great " + magician
    """

magicians = ['hdd', 'yhh', 'hpp', 'wxx', 'znn', 'csh']
show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)
