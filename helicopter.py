import pygame

pygame.init()

display = pygame.display
display.set_caption("Helicopter")
surface = display.set_mode((800, 400))
clock = pygame.time.Clock()

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    display.update()
    clock.tick(60)

pygame.quit()
quit()