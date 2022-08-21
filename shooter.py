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

keyPressed = False
running = True
while running:
    screen.fill(BACKGROUND)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot(screen)

            if event.key or keyPressed:
                player.update(event.key)
                keyPressed = True


        if event.type == pygame.KEYUP:
            if event.key in player.control_keys and keyPressed:
                keyPressed = False
            
    

    if player.bullets:
        if not player.bullets[0].keep_shooting:
            player.bullets.pop(0)
        for bullet in player.bullets:
            bullet.draw(screen)
    player.draw(screen)
            
    clock.tick(frame_rate)
    pygame.display.update()