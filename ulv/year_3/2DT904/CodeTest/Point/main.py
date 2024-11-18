import pygame as pg
from OpenGL.GL import *
from math import sin, cos, radians

class App:
    def __init__(self):
        pg.init()
        pg.display.set_mode((640, 480), pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        glClearColor(0.1, 0.1, 0.1, 1)
        
        # Set up the point size
        glPointSize(5.0)  # Adjust the size of the points

        # Initialize rotation angles for three points
        self.num_points = 3  # We only need 3 points for the triangle
        self.angles = [i * (360 / self.num_points) for i in range(self.num_points)]  # Evenly spaced angles

        self.mainLoop()

    def calculateVertices(self):
        # Calculate the positions of the three points
        radius = 0.5  # Radius of the circular path
        vertices = []
        for i in range(self.num_points):
            x = radius * cos(radians(self.angles[i]))
            y = radius * sin(radians(self.angles[i]))
            vertices.append((x, y))
        return vertices

    def drawTriangle(self, vertices):
        glBegin(GL_TRIANGLES)
        glColor3f(1, 0, 0)  # Set the color of the triangle (green in this case)
        for vertex in vertices:
            glVertex2f(vertex[0], vertex[1])  # Add each vertex to the triangle
        glEnd()

    def drawPoints(self, vertices):
        glBegin(GL_POINTS)
        for vertex in vertices:
            glColor3f(1, 1, 0)  # Yellow for points
            glVertex2f(vertex[0], vertex[1])  # Position of the point
        glEnd()

    def mainLoop(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
            glClear(GL_COLOR_BUFFER_BIT)

            # Calculate vertices of the triangle
            vertices = self.calculateVertices()

            # Draw the filled triangle
            self.drawTriangle(vertices)

            # Draw the points
            self.drawPoints(vertices)

            # Update the angles to rotate the points
            for i in range(self.num_points):
                self.angles[i] += 1  # Increment each angle for rotation
                if self.angles[i] >= 360:
                    self.angles[i] = 0

            pg.display.flip()
            self.clock.tick(60)

        self.quit()

    def quit(self):
        pg.quit()

if __name__ == "__main__":
    myApp = App()
