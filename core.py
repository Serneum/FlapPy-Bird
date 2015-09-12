import pygame
from pygame.locals import *
from color import BLACK, WHITE
from helicopter import Helicopter
from message import Logger

class Game:
    def __init__(self):
        self.__game_over = False
        self.__screen_width = 800
        self.__screen_height = 600
        self.__display = pygame.display
        self.__surface = self.__display.set_mode((self.__screen_width, self.__screen_height))
        self.__clock = pygame.time.Clock()
        self.__heli = None
        self.__logger = None

    def update(self):
        self.__heli.update()
        if self.__heli.is_colliding():
            self.__logger.message("Kaboom!")
            self.game_over()

    def draw(self):
        self.__heli.draw()

    def replay_or_quit(self):
        for event in pygame.event.get([KEYDOWN, KEYUP, QUIT]):
            if event.type is QUIT or (event.type is KEYDOWN and event.key is K_ESCAPE):
                pygame.quit()
                quit()
            elif event.type is KEYDOWN:
                return event.key
        if pygame.mouse.get_pressed()[0]:
                return True
        return None

    def game_over(self):
        while self.replay_or_quit() is None:
            self.__clock.tick()

        self.run()

    def run(self):
        pygame.init()
        self.__logger = Logger(self.__display, self.__surface)
        self.__heli = Helicopter(self.__surface, "helicopter.png")
        while not self.__game_over:
            self.__surface.fill(BLACK)
            self.update()
            self.draw()
            self.replay_or_quit()
            self.__display.update()
            self.__clock.tick(60)

Game().run()