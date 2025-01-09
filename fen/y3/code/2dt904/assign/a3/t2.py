import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from datapoints import createDatapoints

# Initialize Pygame and OpenGL
def initialize():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    gluOrtho2D(-10, 60, -10, 60)  # Set up 2D coordinate system

# Draw a data point as a circle
def draw_circle(x, y, radius, color):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glColor4f(*color)

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)  # Center of the circle
    for angle in np.linspace(0, 2 * np.pi, 50):
        glVertex2f(radius * np.cos(angle), radius * np.sin(angle))
    glEnd()

    glPopMatrix()

# Draw the x and y axes with increments
def draw_axes():
    glColor3f(0, 0, 0)  # Black color for the axes

    # Draw x-axis
    glBegin(GL_LINES)
    glVertex2f(-10, 0)
    glVertex2f(60, 0)
    glEnd()

    # Draw y-axis
    glBegin(GL_LINES)
    glVertex2f(0, -10)
    glVertex2f(0, 60)
    glEnd()

    # Draw x-axis increments
    for x in range(-10, 61, 10):
        glBegin(GL_LINES)
        glVertex2f(x, -0.5)
        glVertex2f(x, 0.5)
        glEnd()

    # Draw y-axis increments
    for y in range(-10, 61, 10):
        glBegin(GL_LINES)
        glVertex2f(-0.5, y)
        glVertex2f(0.5, y)
        glEnd()

# Visualize the dataset
def visualize_data():
    datapoints = createDatapoints()
    max_weight = max([point[2] for point in datapoints])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClearColor(1, 1, 1, 1)  # White background
        glClear(GL_COLOR_BUFFER_BIT)

        draw_axes()  # Draw axes

        for point in datapoints:
            x, y, weight = point
            radius = weight / max_weight * 2  # Scale radius based on weight
            color = (weight / max_weight, 0.2, 1 - weight / max_weight, 0.8)  # Color gradient
            draw_circle(x, y, radius, color)

        pygame.display.flip()

    pygame.quit()

# Main function
def main():
    initialize()
    visualize_data()

if __name__ == "__main__":
    main()

