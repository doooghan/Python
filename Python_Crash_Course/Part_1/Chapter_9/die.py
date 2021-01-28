"""
1. 类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线。实例名
    和模块名都采用小写格式，并在单词之间加上下划线。
2. 需要同时导入标准库中的模块和你编写的模块时，先编写导入标准库模块的import语句，再
    添加一个空行，然后编写导入你自己编写的模块的import语句。在包含多条import语句的程序中，
    这种做法让人更容易明白程序使用的各个模块都来自何方。
"""
from random import randint


class Die():
    """骰子"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """摇骰子"""
        print(randint(1, self.sides))


my_die_6 = Die(6)
my_die_6.roll_die()

my_die_10 = Die(10)
for _ in range(10):
    my_die_10.roll_die()
