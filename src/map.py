import pygame
from settings import *

()


class Map:
    def __init__(self):
        self.grid = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

    def render(self, screen):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                x = j * TILE_SIZE
                y = i * TILE_SIZE
                color = (40, 40, 40) if self.grid[i][j] == 1 else "white"
                rect = pygame.Rect(x, y, TILE_SIZE - 1, TILE_SIZE - 1)

                pygame.draw.rect(screen, color, rect)

    def has_wall(self, x, y):
        return self.grid[int(y // TILE_SIZE)][int(x // TILE_SIZE)]

    def clear_map(self):
        for row in range(ROWS):
            tmp = []
            for clm in range(COLS):
                if row == ROWS - 1 or row == 0 or clm == COLS - 1 or clm == 0:
                    tmp.append(1)
                else:
                    tmp.append(0)
            self.grid.append(tmp)


m = Map()
