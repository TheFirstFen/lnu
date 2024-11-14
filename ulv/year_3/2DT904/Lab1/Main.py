import pygame as pg
import ctypes
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import sys

class App:
    def __init__(self, screenSize = [512, 512]):
        pg.init()
        displayFlags = pg.DOUBLEBUF | pg.OPENGL
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLEBUFFERS, 1)
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLESAMPLES, 4)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        self.screen = pg.display.set_mode(screenSize, displayFlags)
        pg.display.set_caption("Graphics window")
        self.running = True
        self.clock = pg.time.Clock()

    def initialize(self):
        pass

    def update(self):
        pass

    def run(self):
        self.initialize()

        while self.running:
            self.update()

            pg.display.flip()
            self.clock.tick(60)

        pg.quit()
        sys.exit()

class Input(object):
    def __init__(self):
        self.quit = False
    
    def update(self):
        

    

if __name__ == '__main__':
    myApp = App()