import pygal

from chapter_16.die import Die

# 创建两个 D6 骰子
die1 = Die()
die2 = Die(10)

# 掷骰子多次，并将结果存储到一个列表中
results = []
for roll_num in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化结果
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = [str(i) for i in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add("D6 + D10", frequencies)
hist.render_to_file("dice_visual.svg")
