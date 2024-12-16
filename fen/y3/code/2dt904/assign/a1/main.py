import numpy as np
import matplotlib.pyplot as plt

# Define the original house vertices
house_points = np.array([
    [2, 1], [2, 2], [2.5, 2.5], [3, 2], [3, 1], [2, 1], [2, 2], [3, 2]
])

# Step 1: Translation T(3, 1)
translation = np.array([3, 1])
translated_points = house_points + translation

# Step 2: Rotation R(45 degrees)
theta = np.radians(45)
rotation_matrix = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])
rotated_points = np.dot(translated_points, rotation_matrix.T)

# Plot the original and transformed house
plt.figure(figsize=(8, 8))
plt.plot(house_points[:, 0], house_points[:, 1],
         label="Original House", linestyle='--')
plt.plot(rotated_points[:, 0], rotated_points[:, 1],
         label="Transformed House", color='red')
plt.scatter(house_points[:, 0], house_points[:, 1], color='blue')
plt.scatter(rotated_points[:, 0], rotated_points[:, 1], color='red')

# Plot settings
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title("House Transformation: R(45°) T(3, 1)")
plt.legend()
plt.axis('equal')  # Equal aspect ratio
plt.show()

# Return the transformed points
print(rotated_points)
