import math, pygame
from settings import *
from ray import Ray

()


class RayCaster:
    def __init__(self, player):
        self.rays = []
        self.player = player

    def cast_all_rays(self):
        rayAngle = self.player.rotaionAngle - (FOV / 2)

        for i in range(NUM_RAYS):
            ray = Ray(rayAngle, self.player)
            ray.cast()
            self.rays.append(ray)

            rayAngle += FOV / NUM_RAYS - 1

    def render(self, screen):
        for ray in self.rays:
            ray.render(screen)
