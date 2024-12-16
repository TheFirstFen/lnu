# Function to calculate the area of a triangle using determinant formula
def area_of_triangle(x1, y1, x2, y2, x3, y3):
    return round(abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2, 4)


# Vertices of the triangle and the pixel in clip space
V1 = (-0.8, 1)
V2 = (0.9, 0.6)
V3 = (-0.2, -1)
P = (-0.375, -0.375)

# Color values of the vertices
C1 = (1.0, 1.0, 1.0)  # White
C2 = (0.0, 0.0, 0.0)  # Black
C3 = (0.3, 0.3, 1.0)  # Light Blue

# Compute the area of the full triangle
A_tot = area_of_triangle(V1[0], V1[1], V2[0], V2[1], V3[0], V3[1])
print("Area of the triangle:", A_tot)

# Compute the areas of the sub-triangles formed by point P and each pair of triangle vertices
A_P23 = area_of_triangle(P[0], P[1], V2[0], V2[1], V3[0], V3[1])
A_P31 = area_of_triangle(P[0], P[1], V3[0], V3[1], V1[0], V1[1])
A_P12 = area_of_triangle(P[0], P[1], V1[0], V1[1], V2[0], V2[1])
print("Areas of sub-triangles:", A_P23, A_P31, A_P12)

# Compute the barycentric coordinates (weights)
alpha = round(A_P23 / A_tot, 2)
beta = round(A_P31 / A_tot, 2)
gamma = round(A_P12 / A_tot, 2)
print("Barycentric coordinates:", alpha, beta, gamma)

# Interpolate the colors using the barycentric coordinates
interpolated_color = (
    alpha * C1[0] + beta * C2[0] + gamma * C3[0],  # Red channel
    alpha * C1[1] + beta * C2[1] + gamma * C3[1],  # Green channel
    alpha * C1[2] + beta * C2[2] + gamma * C3[2]   # Blue channel
)

# Round the interpolated color to two decimal places
interpolated_color_rounded = tuple(round(c, 2) for c in interpolated_color)
print("Interpolated color:", interpolated_color_rounded)
