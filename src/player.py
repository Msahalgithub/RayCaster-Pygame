import pygame
import math
from settings import *

()


class Player:
    def __init__(self) -> None:
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.radius = 15
        self.color = "red"
        self.rotationAngle = 0
        self.turnDirection = 0
        self.walkDirection = 0
        self.rotationSpeed = 2 * (math.pi / 180)
        self.moveSpeed = 3

    def player_controls(self):
        self.turnDirection = 0
        self.walkDirection = 0

        key = pygame.key.get_pressed()

        if key[pygame.K_d]:
            self.turnDirection = 1

        if key[pygame.K_a]:
            self.turnDirection = -1

        if key[pygame.K_w]:
            self.walkDirection = 1

        if key[pygame.K_s]:
            self.walkDirection = -1

        self.rotationAngle += self.turnDirection * self.rotationSpeed

        move_step = self.walkDirection * self.moveSpeed
        self.x += math.cos(self.rotationAngle) * move_step
        self.y += math.sin(self.rotationAngle) * move_step

    def render(self, screen):
        self.player_controls()
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
