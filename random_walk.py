from random import choice


def get_step():
    """确定每次漫步的距离和方向，并计算这次漫步将如何移动"""
    direction = choice([1, -1])
    distance = choice(range(4))
    step = direction * distance

    return step


class RandomWalk:
    """生成一个随机漫步数据的类"""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        # 所有随机漫步初始点都是 (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步,直到列表达到制定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进的方向以及沿这个方向前进的距离
            x_step = get_step()
            y_step = get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的 x 和 y 值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
