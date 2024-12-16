import numpy as np

# Function to compute the area of a triangle given three points


def triangle_area(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

# Function to compute the barycentric coordinates for a point inside the triangle


def barycentric_coordinates(P, V1, V2, V3):
    x, y = P
    x1, y1 = V1
    x2, y2 = V2
    x3, y3 = V3

    # Calculate the total area of the triangle
    A_total = triangle_area(x1, y1, x2, y2, x3, y3)
    print("Total Area:", A_total)

    # Calculate the areas of the sub-triangles
    A1 = round(triangle_area(x, y, x2, y2, x3, y3), 4)
    A2 = round(triangle_area(x1, y1, x, y, x3, y3), 4)
    A3 = round(triangle_area(x1, y1, x2, y2, x, y), 4)
    print("Sub-Triangle Areas:", A1, A2, A3)

    # Barycentric coordinates
    alpha = A1 / A_total
    beta = A2 / A_total
    gamma = A3 / A_total

    return round(alpha, 2), round(beta, 2), round(gamma, 2)

# Interpolate the color based on barycentric coordinates


def interpolate_color(P, V1, V2, V3, C1, C2, C3):
    # Calculate the barycentric coordinates
    alpha, beta, gamma = barycentric_coordinates(P, V1, V2, V3)
    print("Barycentric Coordinates:", alpha, beta, gamma)

    # Interpolate the color
    R = alpha * C1[0] + beta * C2[0] + gamma * C3[0]
    G = alpha * C1[1] + beta * C2[1] + gamma * C3[1]
    B = alpha * C1[2] + beta * C2[2] + gamma * C3[2]

    return (round(R, 2), round(G, 2), round(B, 2))


# Define the vertices (in viewport space)
V1 = (0.8, 0)
V2 = (7.6, -1.6)
V3 = (3.2, -8)

V1_clip = (-0.8, 1)
V2_clip = (0.9, 0.6)
V3_clip = (-0.2, -1)

# Define the colors for the vertices (white, black, light blue)
C1 = (1.0, 1.0, 1.0)  # White
C2 = (0.0, 0.0, 0.0)  # Black
C3 = (0.3, 0.3, 1.0)  # Light Blue

# Point in clip space (from previous example)
P_clip = (-0.5, -0.25)

# Interpolate the color at the point
interpolated_color = interpolate_color(
    P_clip, V1_clip, V2_clip, V3_clip, C1, C2, C3)

print("Interpolated Color:", interpolated_color)
