import pygame
from OpenGL.GL import *


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


def initializeProgram(vsCode, fsCode):
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


vsCode = """
void main()
{
  gl_Position = vec4(0.0, 0.0, 0.0, 1.0);
}
"""

fsCode = """

out vec4 fragColor;
void main()
{
  fragColor = vec4(1.0, 1.0, 0.0, 1.0);
}
"""


def main():
    # init pygame modules
    pygame.init()
    title = "2DT904 - Setting the stage"
    screenSize = [512, 512]
    displayFlags = pygame.DOUBLEBUF | pygame.OPENGL

    # use a core ogl profile for cross-platform compatibility
    pygame.display.gl_set_attribute(
        pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)

    # create and display the window
    pygame.display.set_mode(screenSize, displayFlags)
    pygame.display.set_caption(title)

    program = initializeProgram(vsCode, fsCode)

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    glPointSize(5)

    glUseProgram(program)
    glDrawArrays(GL_POINTS, 0, 1)

    pygame.display.flip()

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


main()