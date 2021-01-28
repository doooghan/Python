from Python_Crash_Course.Part_1.Chapter_9.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """冰淇淋小店是一种特殊的餐馆"""

    def __init__(self):
        super().__init__('bql', 'ice_cream')
        self.flavors = ['Chocolate', 'Vanilla']

    def show_ice_cream(self):
        """显示这些冰淇淋的口味"""
        for flavor in self.flavors:
            print(flavor + " ice cream")


bql_restaurant = IceCreamStand()
bql_restaurant.describe_restaurant()
bql_restaurant.open_restaurant()
bql_restaurant.show_ice_cream()
