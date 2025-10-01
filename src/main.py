import pygame
import sys
from settings import *
from map import Map
from player import Player

from raycaster import RayCaster

()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

game_map = Map()
player_instance = Player()

raycaster = RayCaster(player_instance, Map)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.fill("black")
    # game_map.render(screen=screen)

    player_instance.render(screen)

    raycaster.cast_all_rays()
    raycaster.render(screen=screen)

    pygame.display.update()
    clock.tick(60)
