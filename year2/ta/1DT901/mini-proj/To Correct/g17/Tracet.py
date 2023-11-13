import math
import random
import matplotlib.pyplot as plt


def convert_ground_map(script):
    ls = []
    for i in script:
        a = []
        for b in i:
            if b == "L":
                a.append(0)
            elif b == "S":
                a.append(1)
            elif b == "O":
                a.append(2)
        ls.append(a)
    return ls


# Använda funktionen
dir_path = "my_map.csv"
with open(dir_path, "r") as file:
    script = file.readlines()
ground_map = convert_ground_map(script)
print(ground_map)


def is_outside(x, y, ground_map):
    x = math.floor(x)
    y = math.floor(y)
    if x >= len(ground_map) or x < 0:
        return True
    elif y >= len(ground_map[0]) or y < 0:
        return True
    elif ground_map[x][y] == 0:
        return False
    elif ground_map[x][y] == 1:
        return False
    elif ground_map[x][y] == 2:
        return True


def one_step(x, y):
    a = random.uniform(0, 2 * math.pi)
    Vx = 0.3 * math.cos(a)
    Vy = 0.3 * math.sin(a)

    return x, Vx, y, Vy


ls_x = []
ls_y = []


def movement(x, y, ground_map):
    first = one_step(x, y)
    Xn = x
    Yn = y
    Xf = first[1]
    Yf = first[3]

    for i in range(90000):
        if is_outside(Xn, Yn, ground_map) is False:
            ls_x.append(Xn)
            ls_y.append(Yn)
            Xn += Xf
            Yn += Yf
            if is_outside(Xn, Yn, ground_map) is True:
                Xb = Xn - Xf
                Yb = Yn - Yf
                while is_outside(Xn, Yn, ground_map) is True:
                    first = one_step(Xb, Yb)
                    Xf = first[1]
                    Yf = first[3]
                    Xn = Xb + Xf
                    Yn = Yb + Yf

    return ls_y, ls_x


# Startposition
start_x = 12
start_y = 31

# Skapa en ny figur och subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Visualisera kartan
ax1.imshow(ground_map, cmap='viridis')
ax1.set_xlabel('Y-position')
ax1.set_ylabel('X-position')
ax1.set_title('Ground Map')

# Utför rörelsen
trajectory_y, trajectory_x = movement(start_x, start_y, ground_map)

# Visualisera rörelsen
ax2.plot(trajectory_y, trajectory_x)
ax2.invert_yaxis()
ax2.set_xlabel('Y-position')
ax2.set_ylabel('X-position')
ax2.set_title('Trace')

# Visa figuren
plt.tight_layout()
plt.show()