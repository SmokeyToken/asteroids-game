import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            new_velocity1 = self.velocity.rotate(angle)
            new_velocity2 = self.velocity.rotate(-angle)