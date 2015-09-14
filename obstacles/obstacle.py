import pygame
from color import *

class Obstacle:
    def __init__(self, x, y, width, height, vel_x):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._vel_x = vel_x

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def update(self):
        self._x -= self._vel_x
