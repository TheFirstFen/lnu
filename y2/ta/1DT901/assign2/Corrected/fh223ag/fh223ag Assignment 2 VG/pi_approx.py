# Variables
import random as rd
import math
point_x = 0
point_y = 0
r = 1
origo_dist = 0
points_in_c = 0
points_in_s = 0
n = 1000

# create n points and check if they are in the circle or square
for i in range(n):
    point_x = rd.uniform(-1, 1)
    point_y = rd.uniform(-1, 1)
    origo_dist = point_x**2 + point_y**2
    if origo_dist <= 1:
        points_in_c += 1
    else:
        points_in_s += 1

# calculate approx of pi and the error
pi = points_in_c / points_in_s
error = math.pi - pi

# Print results
print(f"approximation of pi: {pi} and error: {error}")
