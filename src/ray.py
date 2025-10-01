import pygame, math
from settings import *


def normalizeAngle(angle):
    angle = angle % (2 * math.pi)
    if angle < 0:
        angle = (2 * math.pi) + angle
    return angle


class Ray:
    def __init__(self, angle, player, map) -> None:
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

        self.map = map()

    def cast(self):
        found_horizontal_wall = False
        horizontal_hit_x = 0
        horizontal_hit_y = 0

        first_intersection_x = None
        first_intersection_y = None

        # ()

        if self.is_facing_up:
            first_intersection_y = ((self.player.y) // TILE_SIZE) * TILE_SIZE - 1

        elif self.is_facing_down:
            first_intersection_y = (
                (self.player.y) // TILE_SIZE
            ) * TILE_SIZE + TILE_SIZE

        first_intersection_x = self.player.x + (
            first_intersection_y - self.player.y
        ) / math.tan(self.rayAngle)

        next_horizontal_x = first_intersection_x
        next_horizontal_y = first_intersection_y

        xa = 0
        ya = 0

        if self.is_facing_up:
            ya = -TILE_SIZE

        if self.is_facing_down:
            ya = TILE_SIZE

        xa = ya / math.tan(self.rayAngle)

        while (
            next_horizontal_x <= WIDTH
            and next_horizontal_x >= 0
            and next_horizontal_y <= HEIGHT
            and next_horizontal_y >= 0
        ):
            # print(next_horizontal_x, next_horizontal_y, sep=":")
            # print(
            #     f"Up: {self.is_facing_up}\nDown:{self.is_facing_down}\nRight:{self.is_facing_right}\nLeft:{self.is_facing_left}"
            # )

            if self.map.has_wall((next_horizontal_x), (next_horizontal_y)):

                found_horizontal_wall = True
                horizontal_hit_x = next_horizontal_x
                horizontal_hit_y = next_horizontal_y
                break
            else:
                next_horizontal_x += xa
                next_horizontal_y += ya

        # Test
        self.wall_hit_x = horizontal_hit_x
        self.wall_hit_y = horizontal_hit_y

    def render(self, screen):

        pygame.draw.line(
            screen,
            "red",
            (self.player.x, self.player.y),
            (
                self.wall_hit_x,
                self.wall_hit_y,
            ),
        )
