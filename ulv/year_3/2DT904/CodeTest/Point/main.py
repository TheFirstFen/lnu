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
        glPointSize(5.0)  # Adjust the size of the point

        # Initialize the angle for rotation
        self.angle = 0

        self.mainLoop()

    def drawPoint(self):
        # Calculate the position of the point using trigonometry
        radius = 0.5
        x = radius * cos(radians(self.angle))
        y = radius * sin(radians(self.angle))

        glBegin(GL_POINTS)
        glColor3f(1, 1, 0)  # Set color of the point (red in this case)
        glVertex2f(x, y)  # Position of the point
        glEnd()

    def mainLoop(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
            glClear(GL_COLOR_BUFFER_BIT)

            # Draw the spinning point
            self.drawPoint()

            # Update the angle to rotate the point
            self.angle += 1  # Increment the angle for rotation
            if self.angle >= 360:  # Reset angle after a full rotation
                self.angle = 0

            pg.display.flip()
            self.clock.tick(60)

        self.quit()

    def quit(self):
        pg.quit()

if __name__ == "__main__":
    myApp = App()
