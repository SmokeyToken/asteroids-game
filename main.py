# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *
import pygame
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)

	# Need to instantiate the objects after putting the class in the container
	player_instance = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	while True:
		# Check if user has closed window
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		# Limit frame rate to 60 FPS
		dt = clock.tick(60) / 1000.0

		# Fill the screen with black
		screen.fill((0, 0, 0))	
		
		# Update everything that should be updated
		for thing in updatable:
			thing.update(dt)
		# Render everything on screen constantly
		for thing in drawable:
			thing.draw(screen)

		# Constantly update the screen
		pygame.display.flip()
		

		
if __name__ == "__main__":
	main()
