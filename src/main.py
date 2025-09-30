import pygame
import sys
from settings import *
from map import Map

()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_map = Map()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    m = pygame.mouse.get_pos()

    k = game_map.has_wall(m[0], m[1])

    print(k)
    screen.fill("black")
    game_map.render(screen=screen)
    pygame.display.update()
