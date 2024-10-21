import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

board_color = []
for i in range(8):
    board_color.append([])
    for j in range(8):
        board_color[i].append((i + j) % 2)

ax.imshow(np.array(board_color), cmap="binary")
plt.show()
