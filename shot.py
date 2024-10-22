from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOT_SPEED
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x,y,SHOT_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt