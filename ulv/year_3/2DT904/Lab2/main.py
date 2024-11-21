from OpenGL.GL import *
from app import run
from glslprogram import fromSource
import numpy as np
import os 
os.environ["SDL_VIDEO_X11_FORCE_EGL"] = "1"

vsCode = """
in vec3 position;
in vec3 vertexColor;
out vec3 fragColor;
uniform vec3 offset;
void main()
{
    fragColor = vertexColor;
    gl_Position = vec4(position + offset, 1.0);
}
"""

fsCode = """
in vec3 fragColor;
out vec4 finalColor;
void main()
{
    finalColor = vec4(fragColor, 1.0);
}
"""

def render():
    program = fromSource(vsCode, fsCode)
    positionAttribLocation = glGetAttribLocation(program, "position")
    colorAttribLocation = glGetAttribLocation(program, "vertexColor")
    
    offsetLocation = glGetUniformLocation(program, "offset")

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    positions = [
        0.0, 0.5, 0.0,
        0.5, -0.5, 0.0,
        -0.5, -0.5, 0.0,
    ]

    colors = [
        1.0, 0.0, 0.0,
        0.0, 1.0, 0.0,
        0.0, 0.0, 1.0,
    ]

    vertexData = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vertexData)
    glBufferData(GL_ARRAY_BUFFER, np.array(positions, dtype=np.float32), GL_STATIC_DRAW)
    glVertexAttribPointer(positionAttribLocation, 3, GL_FLOAT, False, 0, None)
    glEnableVertexAttribArray(positionAttribLocation)

    colorData = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, colorData)
    glBufferData(GL_ARRAY_BUFFER, np.array(colors, dtype=np.float32), GL_STATIC_DRAW)
    glVertexAttribPointer(colorAttribLocation, 3, GL_FLOAT, False, 0, None)
    glEnableVertexAttribArray(colorAttribLocation)


    glUseProgram(program)

    glUniform3f(offsetLocation, 0.2, 0.1, 0.0)

    glDrawArrays(GL_TRIANGLES, 0, 3)


run("lab2: Triangle", render)