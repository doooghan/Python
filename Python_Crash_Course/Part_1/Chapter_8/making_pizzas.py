
# 导入整个模块,所有信息都导入
# import Python_Crash_Course.Part_1.Chapter_8.pizza
# Python_Crash_Course.Part_1.Chapter_8.pizza.make_pizza(9, 'pepperoni')

# 导入模块起别名
# import Python_Crash_Course.Part_1.Chapter_8.pizza as p
# p.make_pizza(9, 'pepperoni')

# 导入特定函数,所有信息都导入
# from Python_Crash_Course.Part_1.Chapter_8.pizza import make_pizza
# make_pizza(9, 'pepperoni')


# 导入特定函数起别名
# from Python_Crash_Course.Part_1.Chapter_8.pizza import make_pizza as mp
# mp(9, 'pepperoni')


# 导入所有函数
from Python_Crash_Course.Part_1.Chapter_8.pizza import *
make_pizza(9, 'pepperoni')



