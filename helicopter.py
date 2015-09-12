import pygame
from pygame.locals import K_SPACE, K_UP

class Helicopter:
    def __init__(self, surface, image):
        self.__image = pygame.image.load("resources/" + image)
        self.__surface = surface

        self.__x = 50
        # Start in the center of the y axis
        self.__y = (pygame.display.Info().current_h / 2) - (self.__image.get_rect().size[1] / 2)
        self.__velX = 4
        self.__velY = 4

    def draw(self):
        self.__surface.blit(self.__image, (self.__x, self.__y))

    def update(self):
        keys = pygame.key.get_pressed()
        is_key_pressed = keys[K_SPACE] or keys[K_UP] or pygame.mouse.get_pressed()[0]
        self.__setVelY(is_key_pressed)
        self.__move()

    def __move(self):
        self.__x += self.__velX
        self.__y += self.__velY

    def __setVelY(self, is_key_pressed):
        if is_key_pressed:
            self.__velY = -4
        else:
            self.__velY = 4