import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from datapoints import createDatapoints

# Initialize Pygame and OpenGL
def initialize():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_POINT_SMOOTH)
    glPointSize(10)
    glOrtho(-10, 60, -10, 50, -1, 1)  # Set up an orthographic projection

# Draw data points
def draw_points(data):
    glBegin(GL_POINTS)
    for point in data:
        x, y, weight = point

        # Scale the weight for point size and color intensity
        scaled_weight = max(1, min(weight * 10, 50))
        color_intensity = min(1, weight / 10)

        glColor3f(color_intensity, 0.5 * (1 - color_intensity), 1 - color_intensity)
        glVertex2f(x, y)
    glEnd()

# Animate data visualization
def animate():
    data = createDatapoints()  # Get the data points

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the data points
        draw_points(data)

        pygame.display.flip()

# Main function
def main():
    initialize()
    animate()

if __name__ == "__main__":
    main()

