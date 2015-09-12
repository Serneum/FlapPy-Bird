import pygame

class Helicopter:
    def __init__(self, surface, image):
        self.__image = pygame.image.load("resources/" + image)
        self.__surface = surface

        self.__x = 50
        # Start in the center of the y axis
        self.__y = (pygame.display.Info().current_h / 2) - (self.__image.get_rect().size[1] / 2)
        self.__velX = 0
        self.__velY = 0

    def draw(self):
        self.__surface.blit(self.__image, (self.__x, self.__y))

    def move(self):
        self.__x += self.__velX
        self.__y += self.__velY