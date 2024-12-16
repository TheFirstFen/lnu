import numpy as np

# Function to normalize a vector


def normalize(v):
    norm = np.linalg.norm(v)
    return (round(float(v[0] / norm), 2), round(float(v[1] / norm), 2), round(float(v[2] / norm), 2))

# Function to compute the dot product between two vectors


def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

# Ambient, diffuse, and specular lighting components


def phong_lighting(interpolated_color, L, N, C_ambient, C_diffuse, K_a, K_d):
    # Normalize the light direction
    L = normalize(L)
    print("Normalized Light Direction:", L)

    # Ambient light component
    I_ambient = tuple(round(K_a * c, 4) for c in C_ambient)
    print("Ambient Light Component:", I_ambient)

    # Diffuse light component
    # Ensures the dot product is non-negative
    L_dot_N = max(0, dot_product(L, N))
    I_diffuse = tuple(round(float(K_d * c * L_dot_N), 2) for c in C_diffuse)
    print("Diffuse Light Component:", I_diffuse)

    # Final color by combining ambient and diffuse components
    final_color = tuple(
        round(interpolated_color[i] + I_ambient[i] + I_diffuse[i], 2)
        for i in range(3)
    )

    return final_color


# Given values
C_ambient = (0.2, 0.2, 0.2)  # Ambient light color
C_diffuse = (1.0, 1.0, 0.7)  # Diffuse light color
L = (2, 6, 3)  # Light direction in camera space
N = (0, 0, 1)  # Normal vector (triangle facing towards camera)
K_a = 0.1  # Ambient coefficient
K_d = 1.0  # Diffuse coefficient

# The interpolated color we computed earlier
interpolated_color = (0.51, 0.51, 0.73)

# Calculate the final color of the pixel using Phong lighting
final_color = phong_lighting(
    interpolated_color, L, N, C_ambient, C_diffuse, K_a, K_d)

print("Final Color after Phong Lighting:", final_color)
