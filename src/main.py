import pygame
import sys
from settings import *
from map import Map
from player import Player

()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
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

    pygame.display.update()
