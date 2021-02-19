"""
立方：数字的三次方被称为其立方。请绘制一个图形，显示前 5 个整数的立方
值，再绘制一个图形，显示前 5000 个整数的立方值。
彩色立方：给你前面绘制的立方图指定颜色映射。
"""

import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
# x_values = list(range(1, 6))
y_values = [x ** 3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=40)

plt.title("cubes numbers")
plt.xlabel("value")
plt.ylabel("cube of value")

plt.show()
