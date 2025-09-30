import pygame
import sys
from settings import *
from map import Map
from player import Player
from ray import Ray
from raycaster import RayCaster

()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

game_map = Map()
player_instance = Player()


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.fill("black")
    game_map.render(screen=screen)
    player_instance.render(screen)
    ray = Ray(player_instance.rotationAngle, player_instance)
    ray.render(screen)
    pygame.display.update()
    clock.tick(60)
