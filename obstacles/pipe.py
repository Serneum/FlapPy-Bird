import pygame
from color import *
from platform import Platform

from obstacles.obstacle import Obstacle


class Pipe(Obstacle):
    def __init__(self, x, y, width, height, vel_x, gap):
        Obstacle.__init__(self, x, y, width, height, vel_x)
        # Make sure the gap can always be seen
        screen_height = pygame.display.Info().current_h
        if (height + gap) > screen_height:
            height = screen_height - gap

        top = Platform(x, y, width, height, vel_x)

        bottom_y = y + gap + height
        bottom_height = height
        if height * 2 + gap < screen_height:
            bottom_height = screen_height - bottom_y
        bottom = Platform(x, bottom_y, width, bottom_height, vel_x)
        self.__pipes = [top, bottom]

    def update(self):
        for pipe in self.__pipes:
            pipe.update()

    def get_pipes(self):
        return self.__pipes

    def draw(self, surface):
        for pipe in self.get_pipes():
            pygame.draw.rect(surface, WHITE, [pipe.get_x(), pipe.get_y(), pipe.get_width(), pipe.get_height()])

    def is_colliding(self, player):
        result = False
        top = self.__pipes[0]
        bottom = self.__pipes[1]
        if player.get_x() + player.get_width() >= top.get_x() and player.get_x() <= (top.get_x() + top.get_width()):
            if player.get_y() <= top.get_y() + top.get_height():
                result = True
            elif player.get_y() + player.get_height() >= bottom.get_y():
                result = True
        return result