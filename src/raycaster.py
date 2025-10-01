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

    def cast_all_rays(self):
        self.rays = []
        rayAngle = self.player.rotationAngle - FOV / 2

        for i in range(NUM_RAYS):
            ray = Ray(rayAngle, self.player, self.map)
            ray.cast()
            self.rays.append(ray)

            rayAngle += FOV / NUM_RAYS

    def render(self, screen):
        for ray in self.rays:
            ray.render(screen)
