import pygame as pg
from OpenGL.GL import *
from math import sin, cos, radians

class App:
    def __init__(self):
        pg.init()
        pg.display.set_mode((800, 600), pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        glClearColor(0.1, 0.1, 0.1, 1)
        
        # Set up the point size
        glPointSize(5.0)  # Adjust the size of the point

        # Initialize rotation angles for multiple points
        self.num_points = 5  # Number of points to display
        self.angles = [i * (360 / self.num_points) for i in range(self.num_points)]  # Evenly spaced angles

        self.mainLoop()

    def drawPoints(self):
        radius = 0.5  # Radius of the circular path
        glBegin(GL_POINTS)
        for i in range(self.num_points):
            # Calculate each point's position based on its angle
            x = radius * cos(radians(self.angles[i]))
            y = radius * sin(radians(self.angles[i]))

            # Set color for each point (you can make it dynamic if desired)
            glColor3f(1, 1, 0)  # Yellow for all points
            glVertex2f(x, y)  # Position of the point

            # Update the angle to make the points rotate
            self.angles[i] += 1  # Increment the angle for rotation
            if self.angles[i] >= 360:
                self.angles[i] = 0
        glEnd()

    def mainLoop(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
            glClear(GL_COLOR_BUFFER_BIT)

            # Draw the spinning points
            self.drawPoints()

            pg.display.flip()
            self.clock.tick(60)

        self.quit()

    def quit(self):
        pg.quit()

if __name__ == "__main__":
    myApp = App()
