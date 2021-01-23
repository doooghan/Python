class Restaurant():
    """餐馆类"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """描述餐馆的信息"""
        print(self.restaurant_name + " is a " + self.cuisine_type + " restaurant")

    def open_restaurant(self):
        """指出餐馆正在鹰眼"""
        print(self.restaurant_name + " restaurant is open")


restaurant = Restaurant('hhh', 'coffee')
print(restaurant.restaurant_name, restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_2 = Restaurant('ddd', 'xiaomian')
restaurant_3 = Restaurant('robin', 'big')
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
