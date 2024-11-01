import pygame
import random
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from constants import *

class Upgrade(CircleShape):
    def __init__(self, x, y, radius = 10,  velocity = None):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = velocity or pygame.Vector2(0,0)
        self.position = pygame.Vector2(0,0)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt

    def check_upgrade(self):
        pass
    
    def shot_upgrade(self):
        pass

    def speed_upgrade(self):
        pass

    def multiplier_upgrade(self):
        pass
