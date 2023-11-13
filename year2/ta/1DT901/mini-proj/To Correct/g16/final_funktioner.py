import random
import math
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
path1 = 'small.csv'


def n_rows(coordlist):
    ncounter = 0
    for slashn in range(0, len(coordlist)):
        if coordlist[slashn] == '\n':
            ncounter += 1
    ncounter += 1
    return ncounter


def clear_coordlist(coordlist1):
    coordlist1 = [line.strip().replace(' ', '').replace(',', '')
                  for line in coordlist1]
    coordlist2 = list_all(coordlist1)
    return coordlist2


def list_all(coordlist):
    coordlist2 = []
    for addele in coordlist:
        coordlist2.extend(list(addele))
    return coordlist2


def colors(coordlist):
    plot_map = coordlist
    plot_map.reverse()
    rows = len(plot_map)
    cols = len(plot_map[0])
    plt.figure()
    col_map = ListedColormap(['green', 'yellow', 'red'], 'indexed')
    plt.pcolormesh(plot_map, edgecolors='k', linewidth=2, cmap=col_map)
    ax = plt.gca()
    ax.set_yticks(range(0, rows+1, 1))
    ax.set_xticks(range(0, cols+1, 1))
    plt.title(f"Colored grid of size {rows}x{cols}")
    plt.show()


def char_to_digit_map(ncounter, colcounter, maincoord):
    for lettonum1 in range(0, ncounter):
        for lettonum2 in range(0, colcounter):
            if maincoord[lettonum1][lettonum2] == 'L':
                maincoord[lettonum1][lettonum2] = 0
            if maincoord[lettonum1][lettonum2] == 'O':
                maincoord[lettonum1][lettonum2] = 1
            if maincoord[lettonum1][lettonum2] == 'S':
                maincoord[lettonum1][lettonum2] = 2
    return maincoord


def coordinate_list():
    coordlist1 = []
    with open(path1, "r", encoding='utf8') as mapfile:
        for rows in mapfile:
            coordlist1 += rows

        row_counter = n_rows(coordlist1)
        coordlist1 = [line.strip().replace(' ', '').replace(',', '')
                      for line in coordlist1]
        coordlist2 = list_all(coordlist1)
        col_counter = int((len(coordlist2))/row_counter)

        maincoord = []
        for appcoord1 in range(-1, row_counter - 1):
            rowlist = []
            for appcoord2 in range(((appcoord1 + 1) * col_counter),
                                   (((appcoord1 + 2) * col_counter))):
                rowlist.append(coordlist2[appcoord2])
            maincoord.append(rowlist)

        maincoordet = char_to_digit_map(row_counter, col_counter, maincoord)

        flippedcoord = []
        for flipcoord in range(len(maincoordet), 0, -1):
            flippedcoord.append(maincoordet[flipcoord - 1])
        coordinatelist = [[row[rownr] for row in flippedcoord]
                          for rownr in range(col_counter)]
        col_counter -= 1
        row_counter -= 1
    return coordinatelist, maincoordet, col_counter, row_counter


coordlistan, visualmap, xmax, ymax = coordinate_list()


def is_outside(x, y):
    if 0 > x or x > xmax:
        return True
    elif 0 > y or y > ymax:
        return True
    elif y == ymax:
        if coordlistan[x][y-1] == 1:
            return True
    elif y != ymax:
        if coordlistan[x][y] == 1:
            return True
    else:
        return False


def one_step(x, y, vx, vy):
    deltatime = 0.1
    x1 = x + vx * deltatime
    y1 = y + vy * deltatime
    Xround = int(math.floor(x))
    Yround = int(math.floor(y))
    if not is_outside(Xround, Yround):
        return x1, y1, vx, vy
    while is_outside(Xround, Yround):
        alpha = random.uniform(0, 2*math.pi)
        vx = 0.3 * math.sin(alpha)
        vy = 0.3 * math.cos(alpha)
        x2 = x + vx * deltatime
        y2 = y + vy * deltatime
        x2round = int(math.floor(x2))
        y2round = int(math.floor(y2))
        if not is_outside(x2round, y2round):
            return x2, y2, vx, vy


def find_start():
    for find1 in range(0, xmax):
        for find2 in range(0, ymax):
            if coordlistan[find1][find2] == 2:
                return find1, find2


# 'scale_map' fungerar men används inte

# Function to scale the map at a 1:scale scale
def scale_map(coordlist, scale):
    # Required variables
    scaledlist = []
    rowcounter = len(coordlist)
    row0len = coordlist[0]
    colcounter = len(row0len)
    rowlist2 = []
    # Adds elements from original list X times into new list
    # rowlist is reset after every append to rowlist2
    for addcol1 in range(0, rowcounter):
        rowlist = []
        for addcol2 in range(0, colcounter):
            rowlist.append(coordlist[addcol1][addcol2])
            for addcol3 in range(1, scale):
                rowlist.append(coordlist[addcol1][addcol2])
        rowlist2.append(rowlist)
    # Add rows from rowlist2 X times into new list
    for addrow1 in range(0, rowcounter):
        scaledlist.append(rowlist2[addrow1])
        for addrow2 in range(1, scale):
            scaledlist.append(rowlist2[addrow1])
    return scaledlist
