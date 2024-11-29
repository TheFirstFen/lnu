from OpenGL.GL import *
from matrix import Matrix
from app import run, readFile
from glslprogram import Program
from meshes import setupTriangle
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

    mModel = Matrix.makeIdentity()
    program.setUniformMat4('mModel', mModel)

    mProjView = Matrix.makeIdentity()
    program.setUniformMat4('mProjView', mProjView)


def update(dt, time):
    glDrawArrays(GL_TRIANGLES, 0, drawCount)


run("2DT904 - Transformations", init=init, update=update, screenSize=[512,512])
