import numpy as np
import matplotlib.pyplot as plt

def rotate(point, angle):
    radians = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(radians), -np.sin(radians)],
        [np.sin(radians), np.cos(radians)]
    ])
    return np.dot(rotation_matrix, point)
    
house = np.array([
    [2, 1],
    [2, 2],
    [2.5, 2.5],
    [3, 2],
    [3, 1],
    [2, 1],
    [2, 2],
    [3, 2]
])

rotation_angle = 45 
translation_vector = np.array([3, 1])

transformed_house = []

for point in house:
    translated = point + translation_vector
    rotated = rotate(translated, rotation_angle)
    transformed_house.append(rotated)
    print(f"Original Point: {point}, Translated Point: {translated}, Rotated Point: {rotated}")

transformed_house = np.array(transformed_house)

plt.figure(figsize=(8, 8))
plt.axis('equal')

plt.plot(house[:, 0], house[:, 1], label="Original House", linestyle='--', marker='o')

plt.plot(transformed_house[:, 0], transformed_house[:, 1], label="Transformed House", marker='o')

plt.title("House Transformation: Translation + Rotation")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

plt.grid()
plt.show()
