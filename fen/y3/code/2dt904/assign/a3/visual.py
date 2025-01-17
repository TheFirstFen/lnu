import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from datapoints import createDatapoints


def initialize():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    gluOrtho2D(-10, 60, -10, 60)


def draw_circle(x, y, radius, color):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glColor4f(*color)

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    for angle in np.linspace(0, 2 * np.pi, 50):
        glVertex2f(radius * np.cos(angle), radius * np.sin(angle))
    glEnd()

    glPopMatrix()


def visualize_data():
    datapoints = createDatapoints()
    max_weight = max([point[2] for point in datapoints])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClearColor(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT)

        for point in datapoints:
            x, y, weight = point
            radius = weight / max_weight * 2
            color = (weight / max_weight, 0.2, 1 - weight /
                     max_weight, 0.8)
            draw_circle(x, y, radius, color)

        pygame.display.flip()

    pygame.quit()


def main():
    initialize()
    visualize_data()


if __name__ == "__main__":
    main()
