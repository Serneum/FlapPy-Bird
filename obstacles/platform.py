import pygame
from color import *

from obstacles.obstacle import Obstacle


class Platform(Obstacle):
    def __init__(self, x, y, width, height, vel_x, color):
        Obstacle.__init__(self, x, y, width, height, vel_x, color)

    def draw(self, surface):
        pygame.draw.rect(surface, self._color, [self._x, self._y, self._width, self._height])