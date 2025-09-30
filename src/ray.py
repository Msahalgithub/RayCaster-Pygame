import pygame, math
from settings import *


def normalizeAngle(angle):
    angle = angle % (2 * math.pi)
    if angle < 0:
        angle = (2 * math.pi) + angle
    return angle


class Ray:
    def __init__(self, angle, player) -> None:
        self.rayAngle = normalizeAngle(angle)
        self.player = player
        self.is_facing_down = self.rayAngle > 0 and self.rayAngle < math.pi
        self.is_facing_up = not self.is_facing_down
        self.is_facing_right = (
            self.rayAngle < 0.5 * math.pi or self.rayAngle > 1.5 * math.pi
        )
        self.is_facing_left = not self.is_facing_right

        self.wall_hit_x = 0
        self.wall_hit_y = 0

    def cast(self):
        found_horizontal_wall = False
        horizontal_hit_x = 0
        horizontal_hit_y = 0

        first_intersection_x = None
        first_intersection_y = None
        ()

        if self.is_facing_up:
            first_intersection_y = ((self.player.y) // TILE_SIZE) * TILE_SIZE - 1
        elif self.is_facing_down:
            first_intersection_y = (
                (self.player.y) // TILE_SIZE
            ) * TILE_SIZE + TILE_SIZE

        first_intersection_x = self.player.x + (
            first_intersection_y - self.player.y
        ) / math.tan(self.rayAngle)

    def render(self, screen):
        step = 150
        pygame.draw.line(
            screen,
            "red",
            (self.player.x, self.player.y),
            (
                self.player.x + math.cos(self.rayAngle) * step,
                self.player.y + math.sin(self.rayAngle) * step,
            ),
        )
