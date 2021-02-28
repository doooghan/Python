import matplotlib.pylab as plt

input_values = list(range(1, 1001))
squares = [x ** 2 for x in input_values]
plt.plot(input_values, squares, linewidth=5)

# 设置图表标题,并给坐标轴加上标签
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both", labelsize=14)
# plt.tick_params(labelsize=14)
plt.show()
