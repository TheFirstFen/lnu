from OpenGL.GL import *
from matrix import Matrix
from app import run, readFile
from glslprogram import Program
from meshes import setupTriangle
from math import pi
import os 
os.environ["SDL_VIDEO_X11_FORCE_EGL"] = "1"


vsCode = readFile('1-transformations-vs.glsl')
fsCode = readFile('varying-color-fs.glsl')


def init():
    global program
    global drawCount

    program = Program(vsCode, fsCode)
    program.use()

    drawCount = setupTriangle(program.programId)

    mModel = Matrix.makeTranslation(0.5, 0.5, -40.0) @ Matrix.makeScale(0.5) @ Matrix.makeRotationZ(pi / 2.444)
    program.setUniformMat4('mModel', mModel)

    projection = Matrix.makePerspective()
    mProjView = projection #Matrix.makeIdentity()

    invcameraPos = Matrix.makeTranslation(0, 0, -10)
    mProjView = projection @ invcameraPos
    program.setUniformMat4('mProjView', mProjView)


def update(dt, time):
    glDrawArrays(GL_TRIANGLES, 0, drawCount)


run("2DT904 - Transformations", init=init, update=update, screenSize=[800,800])
