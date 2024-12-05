from OpenGL.GL import *
from matrix import Matrix
from app import run, readFile
from glslprogram import Program
from meshes import setupCube
from math import pi
import os 
os.environ["SDL_VIDEO_X11_FORCE_EGL"] = "1"

vsCode = readFile('./lab4/transform-vs.glsl')
fsCode = readFile('./lab4/varying-color-fs.glsl')


def init():
    global drawCount
    global program

    program = Program(vsCode, fsCode)
    program.use()

    drawCount = setupCube(program.programId, 2)

    projection = Matrix.makePerspective()
    invCameraPos = Matrix.makeTranslation(0, 0, -5)
    mProjView = projection @ invCameraPos

    program.setUniformMat4('mModel', Matrix.makeIdentity())
    program.setUniformMat4('mProjView', mProjView)


def update(dt, time):
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw cube far away
    mModel = Matrix.makeTranslation(0, 0, -20) @ Matrix.makeRotationZ(
        time*pi / 3.5) @ Matrix.makeRotationX(time*pi / 2.5) @ Matrix.makeRotationY(pi / 5.5)
    program.setUniformMat4('mModel', mModel)
    glDrawArrays(GL_TRIANGLES, 0, drawCount)

    # Draw cube near
    mModel = Matrix.makeRotationZ(
        time*pi / 2.5) @ Matrix.makeRotationX(time*pi / 5.5) @ Matrix.makeRotationY(pi / 3.5)
    program.setUniformMat4('mModel', mModel)
    glDrawArrays(GL_TRIANGLES, 0, drawCount)


run("2DT904 - Rasterization", init=init,
    update=update, screenSize=[512, 512])
