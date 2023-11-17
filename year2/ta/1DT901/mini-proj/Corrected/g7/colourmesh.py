import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Create grid data
plot_map = [[0, 0, 1, 1],
            [0, 1, 2, 0],
            [2, 1, 2, 2]]

rows = len(plot_map)     # 3
cols = len(plot_map[0])  # 4


plt.figure()
# Assign color to value: 0 = green, 1 = yellow, 2 = red
color_map = ListedColormap(['green', 'yellow', 'red'], 'indexed')
print("Plot origo", plot_map[0][0])  # Green, not red as might be expected

# Plot grid
plot_map.reverse()  # Turn plot upside-down
plt.pcolormesh(plot_map, edgecolors='k', linewidth=2, cmap=color_map)

# Fine tune plot layout
ax = plt.gca()  # Get current axis object
ax.set_yticks(range(0, rows+1, 1))
ax.set_xticks(range(0, cols+1, 1))
plt.title(f"Colored grid of size {rows}x{cols}")
plt.show()
