import pygame
from typing import Callable


def readFile(name: str):
    with open(name, encoding='utf-8') as f:
        return f.read()


def run(title: str, init: Callable[[], None], update: Callable[[float, float], None], screenSize = [512,512]):
    pygame.init()
    displayFlags = pygame.DOUBLEBUF | pygame.OPENGL

    # use a core ogl profile for cross-platform compatibility
    pygame.display.gl_set_attribute(
        pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)

    # create and display the window
    pygame.display.set_mode(screenSize, displayFlags)
    pygame.display.set_caption(title)

    init()
    clock = pygame.time.Clock()
    clock.tick(60)

    time = 0
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.tick(60) / 1000.0
        time += dt
        update(dt, time)
        pygame.display.flip()

    pygame.quit()
