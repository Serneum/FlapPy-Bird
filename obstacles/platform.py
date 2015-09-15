import pygame
from color import *

from obstacles.obstacle import Obstacle


class Platform(Obstacle):
    def __init__(self, x, y, width, height, vel_x):
        Obstacle.__init__(self, x, y, width, height, vel_x)

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, [self._x, self._y, self._width, self._height])