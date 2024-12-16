import matplotlib.pyplot as plt


def edge_function(x1, y1, x2, y2, x, y):
    return round((y2 - y1) * (x - x1) - (x2 - x1) * (y - y1), 4)


def is_pixel_center_inside_triangle(P, V1, V2, V3):
    x, y = P
    x1, y1 = V1
    x2, y2 = V2
    x3, y3 = V3

    E1 = edge_function(x1, y1, x2, y2, x, y)
    E2 = edge_function(x2, y2, x3, y3, x, y)
    E3 = edge_function(x3, y3, x1, y1, x, y)
    print("Edge functions:", E1, E2, E3)

    if (E1 >= 0 and E2 >= 0 and E3 >= 0) or (E1 <= 0 and E2 <= 0 and E3 <= 0):
        return True
    return False


def to_clip_space(x, y):
    x_clip = 2 * x / 8 - 1
    y_clip = 1 - 2 * y / 8
    return (x_clip, y_clip)


P_viewport = (2.5, 5.5)

P_clip = to_clip_space(*P_viewport)
print("Point in clip space:", P_clip)

V1_clip = (-0.8, 1)
V2_clip = (0.9, 0.6)
V3_clip = (-0.2, -1)

if is_pixel_center_inside_triangle(P_clip, V1_clip, V2_clip, V3_clip):
    print("The point is inside the triangle.")
else:
    print("The point is outside the triangle.")
