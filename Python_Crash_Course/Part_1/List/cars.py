# 对列表本身进行排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# 返回一个排序后的列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)

print()
cars.reverse()
print(cars)
