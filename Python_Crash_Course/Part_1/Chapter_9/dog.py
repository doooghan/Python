class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """初始化"""
        self.name = name
        self.age = age

    def sit(self):
        """下蹲"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """打滚"""
        print(self.name.title() + " rolled back.")


my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()
