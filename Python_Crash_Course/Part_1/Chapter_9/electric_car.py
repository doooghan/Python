class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer) + " miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表数往回调
        """
        if mileage > self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        """将里程表读数增加制定的量"""
        self.odometer += miles


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性,再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    # def __init__(self, make, model, year):
    #     """初始化父类的属性"""
    #     Car.__init__(self, make, model, year)

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-KWh battery")

    def fill_gas_tank(self):
        """电动汽车没有汽油"""
        print("This car doesn't need a gas tank")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
