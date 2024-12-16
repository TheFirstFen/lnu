# Define the edge function to check if the point is on the left side of the edge
def edge_function(x1, y1, x2, y2, x, y):
    return (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1)

# Define the function to check if a point is inside the triangle using edge functions


def is_point_inside_triangle(P, V1, V2, V3):
    x, y = P
    x1, y1 = V1
    x2, y2 = V2
    x3, y3 = V3

    # Compute the edge functions for the triangle edges
    E1 = edge_function(x1, y1, x2, y2, x, y)
    E2 = edge_function(x2, y2, x3, y3, x, y)
    E3 = edge_function(x3, y3, x1, y1, x, y)

    # If all the edge functions have the same sign (all positive or all negative), the point is inside the triangle
    if (E1 >= 0 and E2 >= 0 and E3 >= 0) or (E1 <= 0 and E2 <= 0 and E3 <= 0):
        return True
    else:
        return False

# Clip space transformation function


def to_clip_space(x, y):
    x_clip = (x - 4) / 4
    y_clip = (y + 4) / 4
    return (x_clip, y_clip)


# Define the viewport space coordinates
P_viewport = (2, -5)

# Convert the point from viewport space to clip space
P_clip = to_clip_space(*P_viewport)

# Vertices of the converted triangle in viewport space
V1 = (0.8, 0)
V2 = (7.6, -1.6)
V3 = (3.2, -8)

# Check if the point is inside the triangle in clip space
if is_point_inside_triangle(P_clip, V1, V2, V3):
    print("The point is inside the triangle.")
else:
    print("The point is outside the triangle.")
