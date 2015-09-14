import pygame
from color import *

from obstacles.obstacle import Obstacle


class Pipe(Obstacle):
    def __init__(self, x, y, width, height, vel_x, gap):
        Obstacle.__init__(self, x, y, width, height, vel_x)
        self.__gap = gap

        # Make sure the gap can always be seen
        screen_height = pygame.display.Info().current_h
        if (self._height + gap) > screen_height:
            self._height = screen_height - gap

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, [self._x, self._y, self._width, self._height])
        pygame.draw.rect(surface, WHITE, [self._x, self._y + self.__gap + self._height,
                                          self._width, self._height])