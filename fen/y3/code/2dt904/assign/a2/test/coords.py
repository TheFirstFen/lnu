import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots()

# Set the limits of the axes to match the required coordinate system
ax.set_xlim(0, 8)
ax.set_ylim(-8, 0)

# Add grid lines for better visualization
ax.grid(True)

# Add labels for the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Add tick marks for both axes
ax.set_xticks(range(9))  # X-axis ticks from 0 to 8
ax.set_yticks(range(-8, 1))  # Y-axis ticks from -8 to 0

# Draw the axes lines
ax.axhline(0, color='black', linewidth=2)  # X-axis
ax.axvline(0, color='black', linewidth=2)  # Y-axis

# Vertices of the converted triangle
V1 = (0.8, 0)
V2 = (7.6, -1.6)
V3 = (3.2, -8)

# Plot the triangle
triangle = plt.Polygon([V1, V2, V3], closed=True, fill=None, edgecolor='y')
ax.add_patch(triangle)

# Plot the vertices
ax.plot([V1[0], V2[0], V3[0]], [V1[1], V2[1], V3[1]],
        'r*')  # Red points for vertices
# Plot the point (2, -5)
p = (2, -5)
ax.plot(p[0] + 0.5, p[1] - 0.5, 'bx')  # Blue point for (2, -5)

# Show the plot
plt.show()
