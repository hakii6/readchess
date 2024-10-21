import matplotlib.pyplot as plt
import numpy as np

from enum import Enum

plt.figure(facecolor="#312e2b")


# 129, 182, 76
class Player(Enum):
    BLACK = 1
    WHITE = 2


row_labels = "12345678"
column_labels = "abcdefgh"


def rgb_color_to_plt_color(rgb_color: list[float]):
    plt_color = list(map(lambda x: x / 255, rgb_color))
    if len(rgb_color) == 4:
        plt_color[-1] = rgb_color[-1]
    return plt_color


colors = [
    rgb_color_to_plt_color([235, 236, 208, 1]),
    rgb_color_to_plt_color([115, 149, 82, 1]),
]


nrows, ncols = 8, 8
square_colors = np.zeros(shape=(8, 8, 4))

for i in range(8):
    for j in range(8):
        square_colors[i][j] = colors[(i + j) % 2]

ax = plt.axes()


plt.xticks(np.arange(0, 8, step=1), column_labels)
plt.yticks(np.arange(0, 8, step=1), row_labels[::-1])
ax.xaxis.label.set_color("white")
plt.imshow(square_colors, vmax=1, vmin=0)
plt.show()
