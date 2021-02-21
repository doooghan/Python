import pygal

from die import Die

# 创建一个 6 面骰子
die = Die()

# 掷几次骰子,将结果存在列表中
results = list()
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# print(results)

# 分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ["1", "2", "3", "4", "5", "6"]
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add("D6", frequencies)
hist.render_to_file("die_visual.png")
