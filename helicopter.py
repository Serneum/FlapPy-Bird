import pygame
from pygame.locals import K_SPACE, K_UP

class Helicopter:
    def __init__(self, image):
        self.__image = pygame.image.load("resources/" + image)

        self.__x = 100
        # Start in the center of the y axis
        self.__y = (pygame.display.Info().current_h / 2) - (self.__image.get_rect().size[1] / 2)
        self.__velY = 4

    def draw(self, surface):
        surface.blit(self.__image, (self.__x, self.__y))

    def update(self):
        keys = pygame.key.get_pressed()
        is_key_pressed = keys[K_SPACE] or keys[K_UP] or pygame.mouse.get_pressed()[0]
        self.__setVelY(is_key_pressed)
        self.__move()

    def is_colliding(self, obstacle):
        result = False
        if obstacle is None and (self.__y <= 0 or self.__y > pygame.display.Info().current_h - self.__image.get_rect().size[1]):
            result = True
        elif obstacle is not None and (self.__x >= object.get_x() and self.__x <= (object.get_x() + object.get_width()) and self.__y >= object.get_y() and self.__y <= (object.get_y() + object.get_height())):
            result = True
        return result

    def __move(self):
        self.__y += self.__velY

    def __setVelY(self, is_key_pressed):
        if is_key_pressed:
            self.__velY = -4
        else:
            self.__velY = 4