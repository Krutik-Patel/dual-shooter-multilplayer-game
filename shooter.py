GAME_NAME = "Shooter"
ICON_PATH = "./images/"
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
BACKGROUND = (0, 0, 0)

import pygame
import elements


pygame.init()
clock = pygame.time.Clock()
frame_rate = 50
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption(GAME_NAME)
# icon = pygame.image.load(ICON_PATH).convert()
# pygame.display.set_icon(icon)


# player
player = elements.Shooter(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
# player = pygame.Rect(50, 50, 50, 50)


running = True
while running:
    screen.fill(BACKGROUND)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    player.draw(screen)
    # pygame.draw.rect(screen, (0, 0, 255), player)
    clock.tick(frame_rate)
    pygame.display.update()