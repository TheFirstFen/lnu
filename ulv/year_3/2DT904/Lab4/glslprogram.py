from OpenGL.GL import *
import numpy as np


def fromSource(vsCode, fsCode):

    def initializeShader(shaderCode, shaderType):
        shaderCode = '#version 330\n' + shaderCode

        ref = glCreateShader(shaderType)
        glShaderSource(ref, shaderCode)
        glCompileShader(ref)

        success = glGetShaderiv(ref, GL_COMPILE_STATUS)
        if not success:
            message = glGetShaderInfoLog(ref)
            glDeleteShader(ref)

            message = '\n' + message.decode('utf-8')
            raise Exception(message)
        return ref

    vsRef = initializeShader(vsCode, GL_VERTEX_SHADER)
    fsRef = initializeShader(fsCode, GL_FRAGMENT_SHADER)

    ref = glCreateProgram()
    glAttachShader(ref, vsRef)
    glAttachShader(ref, fsRef)

    glLinkProgram(ref)

    success = glGetProgramiv(ref, GL_LINK_STATUS)
    if not success:
        message = glGetProgramInfoLog(ref)
        glDeleteProgram(ref)

        message = '\n' + message.decode('utf-8')
        raise Exception(message)

    return ref


class Program(object):
    def __init__(self, vsSource, fsSource) -> None:
        self.programId = fromSource(vsSource, fsSource)

    def setUniformFloat(self, name, value):
        ref = glGetUniformLocation(self.programId, name)
        glUniform1f(ref, value)

    def setUniformVec4(self, name, value):
        ref = glGetUniformLocation(self.programId, name)
        glUniform4fv(ref, 1, np.array(value, dtype=np.float32))

    def setUniformMat4(self, name, value):
        ref = glGetUniformLocation(self.programId, name)
        glUniformMatrix4fv(ref, 1, GL_TRUE, value)

    def use(self):
        glUseProgram(self.programId)
