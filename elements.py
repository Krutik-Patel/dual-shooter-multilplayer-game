import pygame
import math
from utils import lerp
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
        self.energy_count = 6
        self.energy_available = 6
        self.energy_rect_side = 15
        self.energy_bar_radius = math.ceil(math.hypot(self.width, self.height))
        self.energy_bar_point_colour = (255, 0, 0)

    def draw(self, screen):
        self.shooter = pygame.Rect(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)
        pygame.draw.rect(screen, self.colour, self.shooter)
        for i in range(self.energy_available):
            point = pygame.Rect(
                self.x - self.energy_bar_radius * math.cos(lerp(0, math.pi, i / (self.energy_count - 1))) - self.energy_rect_side / 2,
                self.y + self.energy_bar_radius * math.sin(lerp(0, math.pi, i / (self.energy_count - 1))) - self.energy_rect_side / 2,
                self.energy_rect_side,
                self.energy_rect_side
                )
            pygame.draw.rect(screen, self.energy_bar_point_colour, point)

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

    def energy(self, screen):
        pass

class Bullet:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.speed = 10
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
