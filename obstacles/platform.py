import pygame
from color import *

from obstacles.obstacle import Obstacle


class Platform(Obstacle):
    def __init__(self, x, y, width, height, vel_x):
        Obstacle.__init__(self, x, y, width, height, vel_x)

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, [self._x, self._y, self._width, self._height])

    def is_colliding(self, player):
        result = False
        if player.get_x() + player.get_width() >= self.get_x() and player.get_x() <= (self.get_x() + self.get_width())\
                and player.get_y() + player.get_height() >= self.get_y() and player.get_y() <= self.get_y() + self.get_height():
            result = True
        return result