import pygame
from color import BLACK, WHITE
from helicopter import Helicopter

class Game:
    def __init__(self):
        self.__game_over = False
        self.__screen_width = 800
        self.__screen_height = 600
        self.__display = pygame.display
        self.__surface = self.__display.set_mode((self.__screen_width, self.__screen_height))
        self.__heli = Helicopter(self.__surface, "helicopter.png")

    def update(self):
        self.__heli.draw()

    def check_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.__game_over = True

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        while not self.__game_over:
            self.update()
            self.check_exit()
            self.__display.update()
            clock.tick(60)

        pygame.quit()
        quit()

Game().run()