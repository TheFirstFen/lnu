import numpy as np

# Normalize the light vector L
L = np.array([2, 6, 3])
L_norm = L / np.linalg.norm(L)

# Normal vector (since the triangle is facing towards the camera)
N = np.array([0, 0, 1])

# Calculate the dot product of the normal and light direction
dot_product = np.dot(N, L_norm)

# Ensure the dot product is non-negative (no negative diffuse lighting)
dot_product = max(0, dot_product)

# Ambient and diffuse light colors
C_ambient = np.array([0.2, 0.2, 0.2])
C_diffuse = np.array([1.0, 1.0, 0.7])

interpolated_color = (0.52, 0.52, 1.0)
# Final color calculation
final_color = C_ambient * interpolated_color + \
    C_diffuse * dot_product * interpolated_color

# Round the final color to two decimals
final_color_rounded = tuple(round(float(c), 2) for c in final_color)
print("Final color:", final_color_rounded)
