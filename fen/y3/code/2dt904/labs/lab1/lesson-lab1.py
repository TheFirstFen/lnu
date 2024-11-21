import pygame as pg
import ctypes
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import math

class App:
    def __init__(self):
        pg.init()
        pg.display.set_mode((800, 600), pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()

        glClearColor(0.1, 0.2, 0.2, 1)

        self.shader = self.createShader('shaders/vert_point.txt', 'shaders/frag_point.txt')
        glUseProgram(self.shader)

        self.point = Point()

        self.offset_location = glGetUniformLocation(self.shader, "offset")
        
        self.mainLoop()

    def createShader(self, vertexFilePath, fragmentFilePath):
        with open(vertexFilePath, 'r') as f:
            vertex_src = f.readlines()

        with open(fragmentFilePath, 'r') as f:
            fragment_src = f.readlines()
        
        shader = compileProgram(
            compileShader(vertex_src, GL_VERTEX_SHADER),
            compileShader(fragment_src, GL_FRAGMENT_SHADER)
        )

        return shader

    def mainLoop(self):
        running = True
        angle = 0.0

        while (running):
            for e in pg.event.get():
                if (e.type == pg.QUIT):
                    running = False
            
            glClear(GL_COLOR_BUFFER_BIT)
            
            # Movment
            x = 0.5 * math.cos(angle)
            y = 0.5 * math.sin(angle)
            angle += 0.05

            offset_location = glGetUniformLocation(self.shader, "offset")
            glUniform2f(offset_location, x, y)

            glUseProgram(self.shader)
            glBindVertexArray(self.point.vao)
            glPointSize(20)
            glDrawArrays(GL_POINTS, 0, 1)

            pg.display.flip()
            self.clock.tick(1000)

    def quit(self):
        self.point.destroy()
        glDeleateProgram(self.shader)
        pg.quit()

class Point:
    def __init__(self):
        self.vertices = (0.0, 0.0, 0.0, 
                         1.0, 1.0, 1.0)

        self.vertex_data = np.array(self.vertices, dtype=np.float32)

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)

        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertex_data.nbytes, self.vertex_data, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
        
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

    def destroy(self):
        glDeleteVertexArrays(1, [self.vao])
        glDeleteBuffers(1, [self.vbo])

if __name__ == '__main__':
    myApp = App()
