import pygame
import random
from constants import *
from upgrade import Upgrade


class UpgradeField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        upgrade = Upgrade(position.x, position.y, radius)
        upgrade.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        # print(f"Spawn timer: {self.spawn_timer}") # debug code
        if self.spawn_timer > UPGRADE_SPAWN_RATE:
            # print("Spawning upgrade!") # debug code
            self.spawn_timer = 0

            # spawn a new upgrade at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            # kind = random.randint(1, UPGRADE_TYPES)
            self.spawn(UPGRADE_RADIUS, position, velocity)