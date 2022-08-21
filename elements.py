import pygame
class Shooter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.colour = (0, 0, 255)
        self.shooter = pygame.Rect(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)


    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.shooter)

        