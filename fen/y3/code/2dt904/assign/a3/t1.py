import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
from sphere import generateSphere

# Initialize Pygame and OpenGL
def initialize():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    # Set light properties
    glLightfv(GL_LIGHT0, GL_POSITION, [0, 0, 0, 1])  # Sun as light source
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.1, 0.2])  # Dim ambient light
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 0.4, 0.2])  # Diffuse light from the Sun
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 0.5, 0.2])  # Specular light from the Sun

    gluPerspective(45, display[0] / display[1], 0.1, 100.0)
    glTranslatef(0.0, 0.0, -30)  # Adjust camera to view from above
    glRotatef(60, 1, 0, 0)  # Rotate camera to focus on the Sun in the center

# Load textures
def load_texture(image_path):
    texture_surface = pygame.image.load(image_path)
    texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
    width, height = texture_surface.get_rect().size

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
    return texture_id

# Draw a textured sphere
def draw_sphere(position, scale, texture_id, rotation_angle):
    glPushMatrix()
    glTranslatef(*position)
    glRotatef(rotation_angle, 0, 1, 0)
    glScalef(scale, scale, scale)

    glBindTexture(GL_TEXTURE_2D, texture_id)
    glEnable(GL_TEXTURE_2D)

    sphere_data = generateSphere()
    glBegin(GL_TRIANGLES)
    for vertex in sphere_data:
        glTexCoord2f((vertex[0] + 1) / 2, (vertex[1] + 1) / 2)  # Map texture coordinates
        glNormal3fv(vertex)  # Normals are the same as vertex positions for a unit sphere
        glVertex3fv(vertex)
    glEnd()

    glDisable(GL_TEXTURE_2D)
    glPopMatrix()

# Animate the solar system
def animate():
    clock = pygame.time.Clock()
    angle = 0
    rotation_angles = [0, 0, 0, 0]
    rotation_speeds = [0.5, -1.0, 1.5, -2.0]  # Different rotation speeds for planets
    moon_angle = 0  # Angle for the moon's orbit

    # Load textures for planets
    planet_textures = [
        load_texture("./img/planet1.jpg"),
        load_texture("./img/planet2.png"),
        load_texture("./img/planet3.jpg"),
        load_texture("./img/planet4.jpg")
    ]

    moon_texture = load_texture("./img/moon.jpg")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the sun
        draw_sphere((0, 0, 0), 2, load_texture("./img/sun.png"), 0)  # Sun emits light and has a texture

        # Draw the planets
        num_planets = 4
        for i in range(num_planets):
            orbit_radius = 5 + i * 2
            planet_position = (
                math.cos(math.radians(angle * rotation_speeds[i] + i * 90)) * orbit_radius,
                0,
                math.sin(math.radians(angle * rotation_speeds[i] + i * 90)) * orbit_radius,
            )

            draw_sphere(planet_position, 0.5 + 0.2 * i, planet_textures[i], rotation_angles[i])

            # Increment rotation angles for local rotation
            rotation_angles[i] += rotation_speeds[i]

            # Draw the moon for the third planet
            if i == 2:
                moon_orbit_radius = 1.5
                moon_position = (
                    planet_position[0] + math.cos(math.radians(moon_angle)) * moon_orbit_radius,
                    0,
                    planet_position[2] + math.sin(math.radians(moon_angle)) * moon_orbit_radius,
                )
                draw_sphere(moon_position, 0.2, moon_texture, 0)

        pygame.display.flip()
        clock.tick(60)
        angle += 2
        moon_angle += 5  # Moon rotates faster than the planet

# Main function
def main():
    initialize()
    animate()

if __name__ == "__main__":
    main()

