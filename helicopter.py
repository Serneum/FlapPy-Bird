import pygame

pygame.init()

display = pygame.display
display.set_caption("Helicopter")
surface = display.set_mode((800, 400))
clock = pygame.time.Clock()

game_over = False

while not game_over:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            game_over = True

    display.update()
    clock.tick(60)

pygame.quit()
quit()