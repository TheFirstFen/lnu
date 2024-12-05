from OpenGL.GL import *
import numpy as np
from ctypes import c_void_p


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


def setupSquare(programId, sideLength=2):
    halfLen = sideLength / 2.0

    posAttrLocation = glGetAttribLocation(programId, "position")
    uvAttrLocation = glGetAttribLocation(programId, "vertexUV")

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    # pos(vec3), uv(vec2)
    vertexData = [-halfLen, -halfLen, 0.0, 0.0, 0.0,  # L B
                  halfLen, halfLen, 0.0, 1.0, 1.0,  # R T
                  -halfLen, halfLen, 0.0, 0.0, 1.0,  # L T
                  halfLen, -halfLen, 0.0, 1.0, 0.0,  # R B
                  halfLen, halfLen, 0.0, 1.0, 1.0,  # R T
                  -halfLen, -halfLen, 0.0, 0.0, 0.0]  # L B
    NumComponents = 5

    vertexBuffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vertexBuffer)
    glBufferData(GL_ARRAY_BUFFER, np.array(
        vertexData, dtype=np.float32), GL_STATIC_DRAW)

    FloatSize = np.dtype(np.float32).itemsize
    glVertexAttribPointer(posAttrLocation, 3, GL_FLOAT,
                          False, NumComponents * FloatSize, c_void_p(0))
    glEnableVertexAttribArray(posAttrLocation)
    if uvAttrLocation != -1:
        glVertexAttribPointer(uvAttrLocation, 2, GL_FLOAT, False, NumComponents * FloatSize, c_void_p(3*FloatSize))
        glEnableVertexAttribArray(uvAttrLocation)


    return len(vertexData) // NumComponents


def setupCube(programId, sideLength):
    halfLen = sideLength / 2.0

    P0 = [-halfLen, -halfLen, -halfLen]
    P1 = [halfLen, -halfLen, -halfLen]
    P2 = [-halfLen, halfLen, -halfLen]
    P3 = [halfLen, halfLen, -halfLen]
    P4 = [-halfLen, -halfLen, halfLen]
    P5 = [halfLen, -halfLen, halfLen]
    P6 = [-halfLen, halfLen, halfLen]
    P7 = [halfLen, halfLen, halfLen]

    C1, C2 = [1, 0.5, 0.5], [0.5, 0, 0]
    C3, C4 = [0.5, 1, 0.5], [0, 0.5, 0]
    C5, C6 = [0.5, 0.5, 1], [0, 0, 0.5]

    positionData = np.array([P5, P1, P3, P5, P3, P7, P0, P4, P6, P0, P6, P2, P6, P7, P3, P6, P3, P2, P0,
                            P1, P5, P0, P5, P4, P4, P5, P7, P4, P7, P6, P1, P0, P2, P1, P2, P3]).ravel().astype(np.float32)
    colorData = np.array([C1]*6 + [C2]*6 + [C3]*6 + [C4]
                         * 6 + [C5]*6 + [C6]*6).ravel().astype(np.float32)

    posAttrLocation = glGetAttribLocation(programId, "position")
    colorAttrLocation = glGetAttribLocation(programId, "vertexColor")

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    positionBufferId = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, positionBufferId)
    glBufferData(GL_ARRAY_BUFFER, positionData, GL_STATIC_DRAW)

    glVertexAttribPointer(posAttrLocation, 3, GL_FLOAT, False, 0, None)
    glEnableVertexAttribArray(posAttrLocation)

    colorBufferId = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, colorBufferId)
    glBufferData(GL_ARRAY_BUFFER, colorData, GL_STATIC_DRAW)
    glVertexAttribPointer(colorAttrLocation, 3, GL_FLOAT, False, 0, None)
    glEnableVertexAttribArray(colorAttrLocation)

    return len(positionData) // 3
