from OpenGL.GL import *


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
