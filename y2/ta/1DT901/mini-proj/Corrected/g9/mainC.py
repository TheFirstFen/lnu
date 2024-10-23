import os
import functions as f

# Main

# Set start time and N

N = 5

time = 7200

# Get path
path = os.getcwd() + "/small.csv"

# Create map and pixel map
map = f.create_map(path)

pixel = f.pixel_map(map, N)

# Movement

# Gets list of x and y coordinates from movement
x_list, y_list = f.movement(time, N, pixel)

# A map with all visited coordinates
coverage_map = f.coverage(pixel, x_list, y_list)

# Compares normal pixel map with visited pixel map
percent = f.get_percentage(pixel, coverage_map)

# Gets x and y lists for trace
smallx = [x/N for x in x_list]

smally = [y/N for y in y_list]

# Visualizes coverage and trace

f.tracemap(smallx, smally, map,)

f.visualize_coverage(coverage_map, percent)

# Calculates average and standard deviation for coverage in many runs

f.many_runs(pixel, 10, 5, time)
