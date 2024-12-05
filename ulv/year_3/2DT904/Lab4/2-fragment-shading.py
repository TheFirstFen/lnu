from OpenGL.GL import *
from matrix import Matrix
from app import run, readFile
from glslprogram import Program
from meshes import setupSquare
from math import pi
import os 
os.environ["SDL_VIDEO_X11_FORCE_EGL"] = "1"

vsCode = readFile('./2-fragment-shading-vs.glsl')
fsCode = readFile('./2-fragment-shading-fs.glsl')


def init():
    global drawCount
    global program

    program = Program(vsCode, fsCode)
    program.use()

    drawCount = setupSquare(program.programId, 2)

    projection = Matrix.makePerspective()
    invCameraPos = Matrix.makeTranslation(0, 0, -2)
    mProjView = projection @ invCameraPos

    program.setUniformMat4('mModel', Matrix.makeIdentity())
    program.setUniformMat4('mProjView', mProjView)


def update(dt, time):
    program.setUniformFloat('time', time)
    glClear(GL_COLOR_BUFFER_BIT)
    glDrawArrays(GL_TRIANGLES, 0, drawCount)


run("2DT904 - Rasterization", init=init,
    update=update, screenSize=[512, 512])
