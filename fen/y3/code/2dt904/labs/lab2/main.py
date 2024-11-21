from OpenGL.GL import *
from app import run
from glslprogram import fromSource
import numpy as np

vsCode = """
    in vec3 position;
    void main()
    {
        gl_Position = vec4(position, 1.0);
    }
    """

fsCode = """
    out vec4 fragColor;
    void main()
    {
        fragColor = vec4(1.0, 1.0, 0.0, 1.0);
    }
    """

def render():
    program = fromSource(vsCode, fsCode)
    positionAttribLocation = glGetAttribLocation(program, "position")

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    positions = [
        -0.5, -0.5, 0.0,
        0.5, -0.5, 0.0,
        0.0, 0.5, 0.0,
    ]

    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, np.array(positions, dtype=np.float32), GL_STATIC_DRAW)
    glVertexAttribPointer(positionAttribLocation, 3, GL_FLOAT, False, 0, None)
    glEnableVertexAttribArray(positionAttribLocation)

    glUseProgram(program)
    glDrawArrays(GL_TRIANGLES, 0, 3)

    pass

run('Lab 2', render)
