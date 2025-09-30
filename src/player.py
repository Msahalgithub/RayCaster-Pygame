import pygame
import math
from settings import *


class Player:
    def __init__(self) -> None:
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.radius = 15
        self.color = "red"

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
