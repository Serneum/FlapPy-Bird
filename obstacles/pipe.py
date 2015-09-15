import pygame
from color import *
from platform import Platform

from obstacles.obstacle import Obstacle


class Pipe(Obstacle):
    def __init__(self, x, y, width, height, vel_x, gap, color):
        Obstacle.__init__(self, x, y, width, height, vel_x, color)

        # Make sure the gap can always be seen
        screen_height = pygame.display.Info().current_h
        if (height + gap) > screen_height:
            height = screen_height - gap
        top = Platform(x, y, width, height, vel_x, color)

        # Make sure the bottom half of the pipe always takes up the rest of the height of the screen
        bottom_y = y + gap + height
        bottom_height = screen_height - bottom_y
        bottom = Platform(x, bottom_y, width, bottom_height, vel_x, color)
        self.__pipes = [top, bottom]

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