import pygame
class Shooter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.colour = (0, 0, 255)
        self.bullets = []
        self.control_keys = [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]
        self.movement_speed = 5

    def draw(self, screen):
        self.shooter = pygame.Rect(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)
        pygame.draw.rect(screen, self.colour, self.shooter)

    def update(self, keys):
        if keys[pygame.K_w]:
            self.y -= self.movement_speed
        if keys[pygame.K_a]:
            self.x -= self.movement_speed
        if keys[pygame.K_s]:
            self.y += self.movement_speed
        if keys[pygame.K_d]:
            self.x += self.movement_speed



    def shoot(self, screen):
        bullet = Bullet(self.x, self.y, screen)
        self.bullets.append(bullet)


class Bullet:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 5
        self.speed = 5
        self.colour = (0, 255, 0)
        self.keep_shooting = True
        self.draw(screen)
    
    def draw(self, screen):
        bullet = pygame.Rect(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)
        pygame.draw.rect(screen, self.colour, bullet)
        self.update(self.x, self.y)

    def update(self, x, y):
        self.y -= self.speed
        if self.y < 0:
            self.keep_shooting = False
