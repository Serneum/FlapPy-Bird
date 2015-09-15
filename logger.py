import pygame
from color import WHITE, SUNSET
import time

class Logger:
    def __init__(self, display, surface):
        self.__display = display
        self.__surface = surface

    def game_over(self, text, wait):
        screen_info = pygame.display.Info()
        screen_width = screen_info.current_w
        screen_height = screen_info.current_h

        small_text = pygame.font.Font("freesansbold.ttf", 20)
        large_text = pygame.font.Font("freesansbold.ttf", 150)
        continue_text_surf, continue_text_rect = self.__make_text_objects("Press any key to continue...", small_text)

        title_text_surf, title_text_rect = self.__make_text_objects(text, large_text)
        title_text_rect.center = screen_width / 2, screen_height / 2
        continue_text_rect.center = screen_width / 2, ((screen_height / 2) + 100)

        self.__surface.blit(title_text_surf, title_text_rect)
        self.__surface.blit(continue_text_surf, continue_text_rect)
        self.__display.update()
        time.sleep(wait)

    def score(self, score):
        font = pygame.font.Font("freesansbold.ttf", 20)
        text = font.render("Score: " + str(score), True, WHITE)
        self.__surface.blit(text, [0, 0])

    def __make_text_objects(self, text, font):
        text_surface = font.render(text, True, SUNSET)
        return text_surface, text_surface.get_rect()