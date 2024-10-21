import matplotlib.pyplot as plt
import numpy as np


def rgb_color_to_plt_color(rgb_color: list[int]):
    plt_color = list(map(lambda x: x / 255, rgb_color))
    if len(rgb_color) == 4:
        plt_color[-1] = rgb_color[-1]
    return plt_color


colors = [
    rgb_color_to_plt_color([49, 46, 43, 1]),
    rgb_color_to_plt_color([255, 255, 255, 1]),
]


nrows, ncols = 8, 8
square_colors = np.zeros(shape=(8, 8, 4))

for i in range(8):
    for j in range(8):
        square_colors[i][j] = colors[(i + j) % 2]
print(square_colors)


plt.imshow(square_colors, vmax=255, vmin=0)
plt.show()
