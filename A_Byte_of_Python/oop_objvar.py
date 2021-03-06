# coding=UTF-8

class Robot:
    """表示一个带有名字的机器人"""
    # 一个类变量,用来计数机器人的数量
    population = 0

    def __init__(self, name):
        """初始化数据"""
        self.name = name
        print("(Initializing {})".format(self.name))

        # 初始化一次,机器人创建一个
        Robot.population += 1

    def die(self):
        """我 gg 了"""
        print("{} is being destoryed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There are still {:d} robots working".format(Robot.population))

    def say_hi(self):
        """来自机器人的问候"""
        print("Greetings, my master call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        """打印当前人口数量"""
        print("We have {:d} robots.".format(Robot.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3P0")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destory them.")
droid1.die()
droid2.die()

Robot.how_many()

print(Robot.die.__doc__)
