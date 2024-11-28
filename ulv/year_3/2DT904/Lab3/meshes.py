from OpenGL.GL import *
import numpy as np

def setupTriangle(programId):
    posAttrLocation = glGetAttribLocation(programId, "position")

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    positions = [0.0, 1.0, 0.0,
                 1.0, -1.0, 0.0,
                 -1.0, -1.0, 0.0]

    vertexData = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vertexData)
    glBufferData(GL_ARRAY_BUFFER, np.array(
        positions, dtype=np.float32), GL_STATIC_DRAW)
    glVertexAttribPointer(posAttrLocation, 3, GL_FLOAT, False, 0, None)
    glEnableVertexAttribArray(posAttrLocation)

    return len(positions) // 3