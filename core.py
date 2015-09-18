import pygame
from pygame.locals import *
from color import *
from helicopter import Helicopter
from logger import Logger
from obstacles.platform import Platform
from obstacles.pipe import Pipe
from obstacles.doublePipe import DoublePipe
from random import randint, randrange

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
        self.__colors = [LIGHTBLUE, ORANGE, PURPLE, YELLOW, YELLOWGREEN]
        self.score = 0

    # Update all objects
    def update(self):
        self.__heli.update()
        for obstacle in self.__obstacle_list:
            # Check if colliding with obstacle
            if obstacle.is_colliding(self.__heli):
                self.game_over()
            # Check if we've successfully passed this obstacle. Only count score once
            if not obstacle.passed_player and obstacle.x + obstacle.width <= self.__heli.x:
                obstacle.passed_player = True
                self.score += 1

            # Remove obstacles that are now off the screen
            if obstacle.x + obstacle.width <= 0:
                self.__obstacle_list.remove(obstacle)

        # Check for hitting ceiling/floor after checking objects
        if self.__heli.is_out_of_bounds():
            self.game_over()

        # Update obstacle speed and position.
        # We do this after checking for scores to guarantee that all speeds will be the same
        for obstacle in self.__obstacle_list:
            diff_settings = self.get_difficulty_settings()
            obstacle.vel_x = diff_settings[0]
            obstacle.update()

        # Decide whether to generate a new obstacle
        self.generate_obstacle()

    # Draw all objects
    def draw(self):
        self.__heli.draw(self.__surface)
        for obstacle in self.__obstacle_list:
            obstacle.draw(self.__surface)
        self.__logger.score(self.score)

    # Quit the game or return user input
    def replay_or_quit(self):
        for event in pygame.event.get([KEYDOWN, KEYUP, QUIT]):
            if event.type is QUIT or event.key is K_ESCAPE:
                pygame.quit()
                quit()
            elif event.type is KEYDOWN or event.type is KEYUP:
                return event.key
        if pygame.mouse.get_pressed()[0]:
                return True
        return None

    # Display game over message and wait for user input
    def game_over(self):
        self.__logger.game_over("Kaboom!", 1)
        while self.replay_or_quit() is None:
            self.__clock.tick()
        self.reset()
        self.run()

    # Reset the game
    def reset(self):
        self.__heli.reset()
        self.__obstacle_list = []
        self.score = 0

    # Determine when and what type of obstacle to generate
    def generate_obstacle(self):
        types = {0: Platform, 1: Pipe, 2: DoublePipe}

        create_obstacle = len(self.__obstacle_list) is 0
        if not create_obstacle:
            last_obstacle = self.__obstacle_list[-1]
            if last_obstacle.x + last_obstacle.width <= self.__screen_width - 400:
                create_obstacle = randint(0, 1) is 1
        if create_obstacle:
            color = self.__colors[randrange(0, len(self.__colors))]
            diff_settings = self.get_difficulty_settings()
            obs_type = types[randint(0, 2)]
            if obs_type is Platform:
                platform_height = 50
                obstacle = obs_type(self.__screen_width, (self.__screen_height - platform_height) / 2,
                                    randint(150, self.__screen_width / 2), platform_height, diff_settings[0], color)
            else:
                obstacle = obs_type(self.__screen_width, 0, 75, randint(0, self.__screen_height), diff_settings[0],
                                    self.__heli.height * diff_settings[1], color)
            self.__obstacle_list.append(obstacle)

    # Change difficulty based on the player's score
    def get_difficulty_settings(self):
        # First part is speed, second is gap modifier
        settings = (3, 3.2)
        if 3 <= self.score < 5:
            settings = (4, 3.1)
        elif 5 <= self.score < 8:
            settings = (5, 3.0)
        elif 8 <= self.score < 14:
            settings = (6, 2.9)
        elif self.score >= 14:
            settings = (7, 2.8)
        return settings

    # Run the game
    def run(self):
        self.__logger = Logger(self.__display, self.__surface)
        self.generate_obstacle()
        while True:
            self.__surface.fill(BLACK)
            self.update()
            self.draw()
            self.replay_or_quit()
            self.__display.update()
            self.__clock.tick(75)

pygame.init()
Game().run()