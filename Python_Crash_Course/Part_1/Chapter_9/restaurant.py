class Restaurant():
    """餐馆类"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """描述餐馆的信息"""
        print(self.restaurant_name + " is a " + self.cuisine_type + " restaurant")

    def open_restaurant(self):
        """指出餐馆正在营业"""
        print(self.restaurant_name + " restaurant is open")

    def set_number_served(self, number):
        """设置就餐人数"""
        self.number_served = number

    def increment_number_served(self, number):
        """每日新增的就餐人数"""
        self.number_served += number


"""
restaurant = Restaurant('hhh', 'coffee')
print(restaurant.restaurant_name, restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_2 = Restaurant('ddd', 'xiaomian')
restaurant_3 = Restaurant('robin', 'big')
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

print(restaurant.number_served)
restaurant.set_number_served(10000)
print(restaurant.number_served)

restaurant.increment_number_served(1500)
print(restaurant.number_served)
"""
