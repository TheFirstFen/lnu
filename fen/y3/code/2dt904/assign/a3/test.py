import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from sphere import generateSphere

# Initialize Pygame and OpenGL


def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Solar System")
    return screen


def init_opengl():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background


def create_shader(shader_type, source):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)
    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(shader).decode()
        raise RuntimeError(f"Shader compilation failed: {error}")
    return shader


def create_program(vertex_src, fragment_src):
    vertex_shader = create_shader(GL_VERTEX_SHADER, vertex_src)
    fragment_shader = create_shader(GL_FRAGMENT_SHADER, fragment_src)
    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)
    if not glGetProgramiv(program, GL_LINK_STATUS):
        error = glGetProgramInfoLog(program).decode()
        raise RuntimeError(f"Program linking failed: {error}")
    return program


# GLSL shaders
VERTEX_SHADER = """
#version 330 core
layout(location = 0) in vec3 position;
out vec3 fragPosition;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main() {
    fragPosition = position;
    gl_Position = projection * view * model * vec4(position, 1.0);
}
"""

FRAGMENT_SHADER = """
#version 330 core
in vec3 fragPosition;
out vec4 fragColor;

void main() {
    fragColor = vec4(1.0, 1.0, 0.0, 1.0); // Yellow color for the Sun
}
"""

# Main function


def main():
    screen = init_pygame()
    init_opengl()

    # Compile and link shaders
    shader_program = create_program(VERTEX_SHADER, FRAGMENT_SHADER)
    glUseProgram(shader_program)

    # Generate sphere vertex data
    sphere_vertices = np.array(generateSphere(), dtype=np.float32)
    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)

    glBindVertexArray(vao)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, sphere_vertices.nbytes,
                 sphere_vertices, GL_STATIC_DRAW)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, None)
    glEnableVertexAttribArray(0)

    # Projection and view matrices
    projection = gluPerspective(45, (800 / 600), 0.1, 50.0)
    view = np.eye(4, dtype=np.float32)
    glUniformMatrix4fv(glGetUniformLocation(
        shader_program, "projection"), 1, GL_TRUE, projection)
    glUniformMatrix4fv(glGetUniformLocation(
        shader_program, "view"), 1, GL_TRUE, view)

    # Main loop
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Set up model matrix for the Sun
        model = np.eye(4, dtype=np.float32)
        glUniformMatrix4fv(glGetUniformLocation(
            shader_program, "model"), 1, GL_TRUE, model)

        # Draw the Sun
        glBindVertexArray(vao)
        glDrawArrays(GL_TRIANGLES, 0, len(sphere_vertices) // 3)

        pygame.display.flip()
        clock.tick(60)

    # Cleanup
    pygame.quit()


if __name__ == "__main__":
    main()
