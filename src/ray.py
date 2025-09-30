import pygame, math


def normalizeAngle(angle):
    angle = angle % (2 * math.pi)
    if angle < 0:
        angle = (2 * math.pi) + angle
    return angle


class Ray:
    def __init__(self, angle, player) -> None:
        self.rayAngle = normalizeAngle(angle)
        self.player = player

    def cast(self): ...

    def render(self, screen):
        step = 50
        pygame.draw.line(
            screen,
            "red",
            (self.player.x, self.player.y),
            (
                self.player.x * math.cos(self.rayAngle) * step,
                self.player.y * math.sin(self.rayAngle) * step,
            ),
        )
