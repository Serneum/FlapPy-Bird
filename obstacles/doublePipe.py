import pygame
from color import *
from platform import Platform
from random import randint

from obstacles.obstacle import Obstacle


class DoublePipe(Obstacle):
    def __init__(self, x, y, width, height, vel_x, gap, color):
        Obstacle.__init__(self, x, y, width, height, vel_x, color)
        mid_height = randint(0, 150)

        # Make sure the gap can always be seen
        screen_height = pygame.display.Info().current_h
        if (height + (gap * 2) + mid_height) > screen_height:
            height = screen_height - (gap * 2) - mid_height
        top = Platform(x, y, width, height, vel_x, color)

        mid_y = y + gap + height
        mid = Platform(x, mid_y, width, mid_height, vel_x, color)

        # Make sure the bottom of the pipe always takes up the rest of the height of the screen
        bottom_y = mid_y + gap + mid_height
        bottom_height = screen_height - bottom_y
        bottom = Platform(x, bottom_y, width, bottom_height, vel_x, color)
        self.__pipes = [top, mid, bottom]

    @property
    def x(self):
        return self.__pipes[0].x

    def get_pipes(self):
        return self.__pipes

    def update(self):
        for pipe in self.__pipes:
            pipe.update()

    def draw(self, surface):
        for pipe in self.get_pipes():
            pipe.draw(surface)

    def is_colliding(self, player):
        result = False
        for pipe in self.get_pipes():
            result = pipe.is_colliding(player)
            if result:
                break
        return result