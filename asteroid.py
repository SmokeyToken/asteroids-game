import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from score import Score

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity = None):
        super().__init__(x,y,radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.position = pygame.Vector2(x, y)
        self.velocity = velocity or pygame.Vector2(0,0)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, asteroids):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            #  player_score += 2
            return
        else:
            angle = random.uniform(20,50)
            #  player_score += 1
            new_velocity1 = self.velocity.rotate(angle) * random.uniform(1,2)
            new_velocity2 = self.velocity.rotate(-angle) * random.uniform(1,2)
            # print(f"1: {new_velocity1}")
            # print(f"2: {new_velocity2}")
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, new_velocity1)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, new_velocity2)
            asteroids.add(new_asteroid1)
            asteroids.add(new_asteroid2)
