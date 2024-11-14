import pygame as pg
from OpenGL.GL import *

class App:
    def __init__(self):
        pg.init
        pg.display.set_mode((640, 480), pg.OPENGL|pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        glClearColor(0.1, 0.2, 0.2, 1)
        self.mainLoop()

    def mainLoop(self):

        running = True
        while (running):
            for event in pg.event.get():
                if (event.type == pg.QUIT):
                    running = False
            glClear(GL_COLOR_BUFFER_BIT)
            pg.display.flip()
            
            self.clock.tick(60)

        self.quit()

    def quit(self):
        pg.quit()

if __name__ == "__main__":
    myApp = App()
