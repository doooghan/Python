motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

""" 添加元素 """
motorcycles.append('honda')
print(motorcycles)

motorcycles.insert(0, 'dayun')
print(motorcycles)

""" 删除元素"""
# del 删除需要知道索引, 不存在报错
del motorcycles[0]
print(motorcycles)

# pop默认删除尾部,如果空报错
# motorcycles = []
poped_motorcycle = motorcycles.pop()
print(poped_motorcycle)
print(motorcycles)

# pop 加数字删除下标,不存在报错
first_owned = motorcycles.pop(10)
print("The first motorcycle I owned was a " + first_owned.title() + ".")
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# remove 删除未知位置, 如果不存在报错
# 只能删除第一次出现的元素
motorcycles.remove('ducati')
print(motorcycles)

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")