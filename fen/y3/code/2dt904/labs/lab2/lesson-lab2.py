from OpenGL.GL import *
from app import run
from glslprogram import fromSource
import numpy as np
import ctypes

vsCode = """
    in vec3 position;
    in vec3 vertexColor;
    out vec3 color;
    uniform vec3 offset;
    void main()
    {
        gl_Position = vec4(position + offset, 1.0);
        color = vertexColor;
    }
    """

fsCode = """
    in vec3 color;
    out vec4 fragColor;
    void main()
    {
        fragColor = vec4(color, 1.0);
    }
    """

def render():
    program = fromSource(vsCode, fsCode)
    positionAttribLocation = glGetAttribLocation(program, "position")
    colorAttribLocation = glGetAttribLocation(program, "vertexColor")
    offsetUniformLocation = glGetUniformLocation(program, "offset")

    offset_value = np.array([0.2, 0.3, 0.4], dtype=np.float32)

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    positions = [
        -0.5, -0.5, 0.0,
        0.5, -0.5, 0.0,
        0.0, 0.5, 0.0,
    ]

    colors = [
        1.0, 0.0, 0.0,  # R
        0.0, 1.0, 0.0,  # G
        0.0, 0.0, 1.0,  # B
    ]

    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, np.array(positions + colors, dtype=np.float32), GL_STATIC_DRAW)
    glVertexAttribPointer(positionAttribLocation, 3, GL_FLOAT, False, 0, None)
    glEnableVertexAttribArray(positionAttribLocation)

    glVertexAttribPointer(colorAttribLocation, 3, GL_FLOAT, False, 0, ctypes.c_void_p(len(positions) * 4))
    glEnableVertexAttribArray(colorAttribLocation)

    glUseProgram(program)
    glUniform3fv(offsetUniformLocation, 1, offset_value)

    glDrawArrays(GL_TRIANGLES, 0, 3)

run('Lab 2', render)
