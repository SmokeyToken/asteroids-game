import pygame
from shot import Shot
from player import Player
from circleshape import CircleShape

class Score():
    def __init__(self, font_size = 36):
        self.score = 0
        self.font = pygame.font.Font(None, font_size)
        self.color = (255,255,255)
   
    # Increment score by an amount
    def up_score(self, amount):
        self.score += amount
   
    def get_score(self):
        return self.score
    
    # Update player's score at point on screen
    def display(self, surface, x, y):
        score_text = f"Score: {self.score}"
        score_surface = self.font.render(score_text, True, self.color)
        surface.blit(score_surface, (x,y))    