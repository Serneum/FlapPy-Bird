import pygame
from pygame.locals import K_SPACE, K_UP

class Helicopter:
    def __init__(self, image):
        self.__image = pygame.image.load("resources/" + image)
        self.__speed = 7

        self.__x = 100
        # Start in the center of the y axis
        self.__y = (pygame.display.Info().current_h / 2) - (self.height / 2)
        self.__vel_y = self.__speed

    def draw(self, surface):
        surface.blit(self.__image, (self.x, self.y))

    def update(self):
        keys = pygame.key.get_pressed()
        is_key_pressed = keys[K_SPACE] or keys[K_UP] or pygame.mouse.get_pressed()[0]
        self.__determine_vel_y(is_key_pressed)
        self.__move()

    def is_out_of_bounds(self):
        result = False
        if self.y <= 0 or self.y > pygame.display.Info().current_h - self.__image.get_rect().size[1]:
            result = True
        return result

    def reset(self):
        self.__y = (pygame.display.Info().current_h / 2) - (self.__image.get_rect().size[1] / 2)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def width(self):
        return self.__image.get_rect().size[0]

    @property
    def height(self):
        return self.__image.get_rect().size[1]

    def __move(self):
        self.__y += self.__vel_y

    def __determine_vel_y(self, is_key_pressed):
        if is_key_pressed:
            self.__vel_y = -self.__speed
        else:
            self.__vel_y = self.__speed