import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from datapoints import createDatapoints

# Initialize the pygame and OpenGL environment
def init():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glClearColor(1, 1, 1, 1)
    glOrtho(-10, 60, -10, 60, -1, 1)

def draw_axes():
    glColor3f(0, 0, 0)

    # x-axis
    glBegin(GL_LINES)
    glVertex2f(-10, 0)
    glVertex2f(60, 0)
    glEnd()

    # x-axis ticks
    for i in range(-10, 60, 5):
        glBegin(GL_LINES)
        glVertex2f(i, -1)
        glVertex2f(i, 1)
        glEnd()

    # y-axis
    glBegin(GL_LINES)
    glVertex2f(0, -10)
    glVertex2f(0, 50)
    glEnd()

    # y-axis ticks
    for i in range(-10, 50, 5):
        glBegin(GL_LINES)
        glVertex2f(-1, i)
        glVertex2f(1, i)
        glEnd()

# Draw a quad at the given position with the given radius and color
def draw_quad(x, y, radius, color):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glColor4f(*color)

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(-radius, -radius)
    glVertex2f(radius, -radius)
    glVertex2f(radius, radius)
    glVertex2f(-radius, radius)

    glEnd()

    glPopMatrix()

# Visualize the data points
def data_visualization():
    data_points = createDatapoints()
    max_weight = max([point[2] for point in data_points])

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_axes()

        for point in data_points:
            x, y, w = point
            radius = (w / max_weight) 
            color = (w / max_weight, 0.2, 1 - w / max_weight, 0.8)
            draw_quad(x, y, radius, color)

        pygame.display.flip()
        pygame.time.wait(10)

def main():
    init()
    data_visualization()

main()
