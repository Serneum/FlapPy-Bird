import pygame
from pygame.locals import *
from color import BLACK, WHITE
from helicopter import Helicopter
from message import Logger
from obstacles.pipe import Pipe
from random import randint

class Game:
    def __init__(self):
        self.__screen_width = 800
        self.__screen_height = 600
        self.__display = pygame.display
        self.__surface = self.__display.set_mode((self.__screen_width, self.__screen_height))
        self.__clock = pygame.time.Clock()
        self.__heli = Helicopter("helicopter.png")
        self.__logger = None
        self.__obstacle_list = []

    def update(self):
        self.__heli.update()
        for obstacle in self.__obstacle_list:
            obstacle.update()
            # Check if colliding with obstacle
            if obstacle.is_colliding(self.__heli):
                self.game_over()
            if obstacle.get_x() + obstacle.get_width() <= 0:
                self.__obstacle_list.remove(obstacle)

        # Check for hitting ceiling/floor after checking objects
        if self.__heli.is_out_of_bounds():
            self.game_over()

    def draw(self):
        self.__heli.draw(self.__surface)
        for obstacle in self.__obstacle_list:
            obstacle.draw(self.__surface)

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
        self.__logger.message("Kaboom!", 1)
        while self.replay_or_quit() is None:
            self.__clock.tick()
        self.reset()
        self.run()

    def reset(self):
        self.__heli.reset()
        self.__obstacle_list = []

    def run(self):
        pygame.init()
        diff_mod = {'EASY': 3, 'NORMAL': 2}
        self.__logger = Logger(self.__display, self.__surface)
        obstacle = Pipe(self.__screen_width, 0, 75, randint(0, self.__screen_height), 3, self.__heli.get_height() * diff_mod['EASY'])
        self.__obstacle_list.append(obstacle)
        while True:
            self.__surface.fill(BLACK)
            self.update()
            self.draw()
            self.replay_or_quit()
            self.__display.update()
            self.__clock.tick(60)

Game().run()