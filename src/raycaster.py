import math, pygame
from settings import *
from ray import Ray
from map import Map

()


class RayCaster:
    def __init__(self, player, map):
        self.rays = []
        self.player = player
        self.map = map
        self.d = (WIDTH // 2) / math.tan(FOV / 2)

    def cast_all_rays(self):
        self.rays = []
        rayAngle = self.player.rotationAngle - FOV / 2

        for i in range(NUM_RAYS):
            ray = Ray(rayAngle, self.player, self.map)

            ray.bad_cast()
            ray.cast()
            self.rays.append(ray)

            rayAngle += FOV / NUM_RAYS

    def render(self, screen):
        i = 0

        for ray in self.rays:
            ray.render(screen)
            line_height = (TILE_SIZE / ray.distance if ray.distance else 1) * self.d

            draw_begin = (HEIGHT / 2) - (line_height / 2)
            draw_end = line_height

            pygame.draw.rect(
                screen,
                (ray.color, ray.color, ray.color),
                (i * RES, draw_begin, RES, draw_end),
            )

            i += 1
