import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import final_funktioner as lawnf
import math

# Ändra .csv path i final_funktioner.py under 'path1'
coordlist, visualmap, xmax, ymax = lawnf.coordinate_list()
startXpos, startYpos = lawnf.find_start()
xnew, ynew, vx, vy = startXpos, startYpos, math.sqrt(0.045), math.sqrt(0.045)
inputtime1 = int(input("Enter the time to mow (minutes): "))
inputtime = round(inputtime1*600)

plot_map2 = visualmap
plot_map2.reverse()
rows = len(plot_map2)
cols = len(plot_map2[0])
plt.figure()
col_map = ListedColormap(['green', 'red', 'yellow'], 'indexed')
plt.pcolormesh(plot_map2, edgecolors='k', linewidth=0.3, cmap=col_map)
ax = plt.gca()
ax.set_yticks(range(0, rows+1, 5))
ax.set_xticks(range(0, cols+1, 5))
plt.title(f"Colored grid of size {rows}x{cols}")
plt.show()


coordinatelist = []
for test in range(0, inputtime):
    tempcoord = []
    xnew, ynew, vx, vy = lawnf.one_step(xnew, ynew, vx, vy)
    lawnf.one_step(xnew, ynew, vx, vy)
    tempcoord.append(xnew)
    tempcoord.append(ynew)
    coordinatelist.append(tempcoord)


xcoords = []
ycoords = []


for test2 in range(0, int(len(coordinatelist))):
    xcoords.append(coordinatelist[test2][0])
    ycoords.append(coordinatelist[test2][1])


plt.plot(xcoords, ycoords, linestyle='-')
plt.show()
