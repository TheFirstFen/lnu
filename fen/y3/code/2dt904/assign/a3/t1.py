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
    glLightfv(GL_LIGHT0, GL_AMBIENT, [1.0, 1.0, 0.0, 0.2])  # Turn off ambient light from the Sun
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.0, 0.0, 0.0, 1.0])  # Turn off diffuse light from the Sun
    glLightfv(GL_LIGHT0, GL_SPECULAR, [0.0, 0.0, 0.0, 1.0])  # Turn off specular light from the Sun

    gluPerspective(45, display[0] / display[1], 0.1, 100.0)
    glTranslatef(0.0, 0.0, -30)  # Adjust camera to view from above
    glRotatef(60, 1, 0, 0)  # Rotate camera to focus on the Sun in the center

# Draw a sphere using vertex data
def draw_sphere(position, scale, base_color, assist_color, shininess, rotation_angle):
    glPushMatrix()
    glTranslatef(*position)
    glRotatef(rotation_angle, 0, 1, 0)
    glScalef(scale, scale, scale)

    # Combine base and assist colors based on local coordinates
    combined_color = [
        (base_color[i] + assist_color[i]) / 2 for i in range(3)
    ]

    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, combined_color)
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, shininess)

    sphere_data = generateSphere()
    glBegin(GL_TRIANGLES)
    for vertex in sphere_data:
        glNormal3fv(vertex)  # Normals are the same as vertex positions for a unit sphere
        glVertex3fv(vertex)
    glEnd()

    glPopMatrix()

# Animate the solar system
def animate():
    clock = pygame.time.Clock()
    angle = 0
    rotation_angles = [0, 0, 0, 0]
    rotation_speeds = [0.5, 1.0, 1.5, 2.0]  # Different rotation speeds for planets
    moon_angle = 0  # Angle for the moon's orbit

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the sun
        draw_sphere((0, 0, 0), 2, (1.0, 1.0, 0.0), (1.0, 1.0, 0.0), 0, 0)  # Sun with no emitted light, no rotation

        # Draw the planets
        num_planets = 4
        for i in range(num_planets):
            orbit_radius = 5 + i * 2
            planet_position = (
                math.cos(math.radians(angle * rotation_speeds[i] + i * 90)) * orbit_radius,
                0,
                math.sin(math.radians(angle * rotation_speeds[i] + i * 90)) * orbit_radius,
            )
            base_color = (0.2 * i, 0.3 + 0.1 * i, 0.5 - 0.1 * i)  # Base color for the planet
            assist_color = (0.5 - 0.1 * i, 0.2 * i, 0.3 + 0.1 * i)  # Assist color for rotation effect

            draw_sphere(planet_position, 0.5 + 0.2 * i, base_color, assist_color, 10 + i * 5, rotation_angles[i])

            # Increment rotation angles for local rotation
            rotation_angles[i] += rotation_speeds[i]

            # Draw the moon for the third planet
            if i == 2:
                moon_orbit_radius = 1.0
                moon_position = (
                    planet_position[0] + math.cos(math.radians(moon_angle)) * moon_orbit_radius,
                    0,
                    planet_position[2] + math.sin(math.radians(moon_angle)) * moon_orbit_radius,
                )
                draw_sphere(moon_position, 0.2, (0.8, 0.8, 0.8), (0.6, 0.6, 0.6), 20, 0)

        pygame.display.flip()
        clock.tick(60)
        angle += 1
        moon_angle += 5  # Moon rotates faster than the planet

# Main function
def main():
    initialize()
    animate()

if __name__ == "__main__":
    main()

