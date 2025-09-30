import pygame
import math
from settings import *


class Player:
    def __init__(self) -> None:
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.radius = 15
        self.color = "red"
        self.rotationAngle = 50

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        pygame.draw.line(
            screen,
            "red",
            (self.x, self.y),
            (
                self.x + math.cos(self.rotationAngle) * 50,
                self.y + math.sin(self.rotationAngle) * 50,
            ),
        )
