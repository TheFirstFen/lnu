import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from math import sin, cos, radians
from sphere import generateSphere

# Initialize Pygame and OpenGL
def init():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    
    # Set up light properties
    glLightfv(GL_LIGHT0, GL_POSITION, (1, 1, 1, 0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.3, 0.3, 0.3, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.7, 0.7, 0.7, 1))

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    # Move the camera back and rotate it
    glTranslatef(0.0, 0.0, -30)
    glRotatef(60, 1, 0, 0)

# Load an image as a texture
def image_texture(image_path):
    texture_surface = pygame.image.load(image_path)
    texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
    width = texture_surface.get_width()
    height = texture_surface.get_height()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    return texture_id

# Draw a sphere with a texture
def draw_sphere(position, scale, texture, rotation_angle):
    glPushMatrix()
    glTranslatef(*position)
    glRotatef(rotation_angle, 0, 1, 0)
    glScalef(scale, scale, scale)

    glBindTexture(GL_TEXTURE_2D, texture)
    glEnable(GL_TEXTURE_2D)
    
    sphere = generateSphere()
    glBegin(GL_TRIANGLES)

    for vertex in sphere:
        glTexCoord2d((vertex[0] + 1) / 2, (vertex[1] + 1) / 2)
        glNormal3fv(vertex)  # Use the vertex as the normal
        glVertex3fv(vertex)
    glEnd()

    glDisable(GL_TEXTURE_2D)
    glPopMatrix()

def rotation():
    clock = pygame.time.Clock()
    orbit_angle = 0  # Angle for orbiting the sun
    axis_rotational_angle = [0, 20, 140, 0]  # Rotation angle for each planet's axis
    rotational_speed = [5, 1.4, 1, 0.4]  # Speeds for orbit
    axis_rotational_speed = [2, 1.5, 1, 0.8]  # Speeds for axial rotation
    moon_angle = 0  # Angle for the moon's orbit

    # Orbit direction: 1 for counterclockwise, -1 for clockwise
    orbit_directions = [1, -1, 1, -1]

    # Load textures for planets and moon
    planet_colors = [
        image_texture('./img/planet1.jpg'),
        image_texture('./img/planet2.jpg'),
        image_texture('./img/planet3.jpg'),
        image_texture('./img/planet4.jpg')
    ]
    moon_color = image_texture('./img/moon.jpg')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the sun
        draw_sphere((0, 0, 0), 2, image_texture('./img/sun.png'), 0)

        # Draw planets
        planets = 4
        for i in range(planets):
            orbit_radius = 4 + i * 3  # Distance of the planet from the sun
            planet_orbit_position = (
                cos(radians(orbit_angle * (orbit_directions[i] * rotational_speed[i]))) * orbit_radius,  # X
                0,
                sin(radians(orbit_angle * (orbit_directions[i] * rotational_speed[i]))) * orbit_radius   # Z
            )

            # Draw the planet with axial rotation
            draw_sphere(planet_orbit_position, 0.5 + 0.2 * i, planet_colors[i], axis_rotational_angle[i])

            # Update the planet's orbit and axial rotation angles
            axis_rotational_angle[i] += axis_rotational_speed[i]

            # Draw the moon orbiting the third planet
            if i == 2:
                moon_orbit_radius = 1.2
                moon_position = (
                    planet_orbit_position[0] + cos(radians(moon_angle)) * moon_orbit_radius,  # X
                    0,
                    planet_orbit_position[2] + sin(radians(moon_angle)) * moon_orbit_radius   # Z
                )
                draw_sphere(moon_position, 0.1, moon_color, 0)
                moon_angle += 5  # Update the moon's angle for its orbit

        pygame.display.flip()

        orbit_angle += 1
        clock.tick(60)


def main():
    init()
    rotation()


if __name__ == '__main__':
    main()
