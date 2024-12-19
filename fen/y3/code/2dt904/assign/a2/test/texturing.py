import numpy as np
import matplotlib.pyplot as plt

file_path = './data/mario_texture'

print("Mario Texture")


def parse_texture(file_path):
    texture = []
    with open(file_path, 'r') as file:
        for line in file:
            row = []
            for item in line.strip().split(']')[:-1]:
                color = item.replace('[RGB(', '').replace(')', '').split(',')
                rgb = tuple(float(c) for c in color)
                row.append(rgb)
            texture.append(row)
    return np.array(texture)


def visualize_texture(texture_data, x0=None, y0=None, x1=None, y1=None):
    plt.imshow(texture_data, extent=(
        0, texture_data.shape[1], texture_data.shape[0], 0))
    plt.colorbar()
    plt.title('Texture Data Visualization')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True)

    if x0 is not None and y0 is not None:
        plt.plot(y0 + 0.5, x0 + 0.5, 'gx', label='Point (x0, y0)')
    if x0 is not None and y1 is not None:
        plt.plot(y1 + 0.5, x0 + 0.5, 'rx', label='Point (x1, y0)')
    if x1 is not None and y0 is not None:
        plt.plot(y0 + 0.5, x1 + 0.5, 'bx', label='Point (x0, y1)')
    if x1 is not None and y1 is not None:
        plt.plot(y1 + 0.5, x1 + 0.5, 'yx', label='Point (x1, y1)')

    plt.legend()
    plt.show()


texture_data = parse_texture(file_path)
print(texture_data.shape)

u, v = 0.42, 0.58
height, width, _ = texture_data.shape

x = u * (height - 1)
y = v * (width - 1)

x_nearest = round(x)
y_nearest = round(y)
nearest_color = texture_data[x_nearest, y_nearest]

x0, y0 = int(np.floor(x)), int(np.floor(y))
x1, y1 = min(x0 + 1, height - 1), min(y0 + 1, width - 1)

wx1, wy1 = x - x0, y - y0
wx0, wy0 = 1 - wx1, 1 - wy1

c00 = texture_data[y0, x0]
c01 = texture_data[y1, x0]
c10 = texture_data[y0, x1]
c11 = texture_data[y1, x1]
print(c00, c01, c10, c11)

visualize_texture(texture_data, x0, y0, x1, y1)

bilinear_color = (wx0 * wy0) * c00 + (wx0 * wy1) * c10 + \
    (wx1 * wy0) * c01 + (wx1 * wy1) * c11

print(nearest_color, bilinear_color)

print('---------------------')
print("Mario Head")

file_path = './data/mario_head'

texture_data = parse_texture(file_path)
print(texture_data.shape)

height_head, width_head, _ = texture_data.shape

visualize_texture(texture_data)


def compute_uv(x, y):
    u = round(x / (width - 1), 4)
    v = round(y / (height - 1), 4)
    return u, v


u_min, v_min = compute_uv(1, 0)
u_max, v_max = compute_uv(width_head, height_head)

print("u_min, v_min, u_max, v_max")
print(u_min, v_min, u_max, v_max)
