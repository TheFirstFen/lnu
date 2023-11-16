import pygame
from options import *
vec = pygame.math.Vector2

# Pacman


class Player:
    def __init__(self, app, pos):
        """
        :param self: Refrence to self
        :param app: Refrence to the application
        :param pos: Pacmans position in the grid
        """
        self.app = app
        self.starting_pos = [pos.x, pos.y]
        self.grid_pos = pos
        self.pos = self.get_pos()
        self.direction = vec(1, 0)
        self.stored_direction = None
        self.able_to_move = True
        self.current_score = 0
        self.speed = 2
        self.lives = 3

    def update(self):
        if self.able_to_move:
            self.pos += self.direction * self.speed
        if self.moveTime():
            if self.stored_direction != None:
                self.direction = self.stored_direction
            self.able_to_move = self.canMove()

        # Setting grid position in reference to pix pos
        self.grid_pos[0] = (self.pos[0] - buffer +
                            self.app.cell_width // 2) // self.app.cell_width + 1
        self.grid_pos[1] = (
            self.pos[1] - buffer + self.app.cell_height // 2) // self.app.cell_height + 1
        if self.onCoin():
            self.eatCoin()

    def draw(self):
        # Drawing pacman
        pygame.draw.circle(self.app.screen, player_colour, (int(
            self.pos.x), int(self.pos.y)), self.app.cell_width // 2 - 2)

        # Drawing player lives
        for x in range(self.lives):
            pygame.draw.circle(self.app.screen, player_colour,
                               (30 + 20 * x, height - 15), 7)

    def onCoin(self):
        # Checks if the picel you are on has a coin or not
        if self.grid_pos in self.app.coins:
            if int(self.pos.x + buffer // 2) % self.app.cell_width == 0:
                if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
                    return True
            if int(self.pos.y + buffer // 2) % self.app.cell_height == 0:
                if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                    return True
        return False

    def eatCoin(self):
        # If there is a coin on the pixel you are on eat it
        self.app.coins.remove(self.grid_pos)
        self.current_score += 1

    def move(self, direction):
        """
        :param self: Refrence to self
        :param direction: Stored direction = current direction
        """
        self.stored_direction = direction

    def get_pos(self):
        return vec((self.grid_pos[0] * self.app.cell_width) + buffer // 2 + self.app.cell_width // 2, (self.grid_pos[1] * self.app.cell_height) + buffer // 2 + self.app.cell_height // 2)
        print(self.grid_pos, self.pos)

    def moveTime(self):
        if int(self.pos.x + buffer // 2) % self.app.cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True
        if int(self.pos.y + buffer // 2) % self.app.cell_height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True

    def canMove(self):
        for wall in self.app.walls:
            if vec(self.grid_pos + self.direction) == wall:
                return False
        return True
