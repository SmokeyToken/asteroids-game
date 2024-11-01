# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *
import pygame
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot
from score import Score
from upgradefield import UpgradeField
from upgrade import Upgrade

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
	shots = pygame.sprite.Group()
	upgrades = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	Shot.containers = (shots, updatable, drawable)
	UpgradeField.containers = (updatable,)
	Upgrade.containers = (upgrades, updatable, drawable)

	# Need to instantiate the objects AFTER putting the class in the container
	player_instance = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()
	player_score = Score()
	upgrade_field = UpgradeField()

	while True:
		# Check if user has closed window
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		keys = pygame.key.get_pressed()

		if keys[pygame.K_SPACE]:
			player_instance.shoot()

		# Limit frame rate to 60 FPS
		dt = clock.tick(60) / 1000.0

		# Fill the screen with black
		screen.fill((0, 0, 0))	
		
		# Update everything that should be updated
		for thing in updatable:
			thing.update(dt)

		# Check if a shot ever comes into contact with an asteroid
		for shot in shots:
			for asteroid in asteroids:
				if shot.collision(asteroid):
					shot.kill()
					asteroid.split(asteroids, player_score)	
					# player_score.up_score(1)
		
		# Check if the player ever comes into contact with an asteroid
		for asteroid in asteroids:
			if player_instance.collision(asteroid):
				print("Game over!")
				print(f"Congratulations! You scored {player_score.get_score()}")
				sys.exit()

		# Check if the player ever comes into contact with an upgrade
		for upgrade in upgrades:
			if player_instance.collision(upgrade):
				print("Upgrade Collected!")
				upgrade.check_upgrade()
				upgrade.kill()
				# print("Upgrade Deleted") # debug code

		# Render everything on screen constantly
		for thing in drawable:
			thing.draw(screen)

		# Display the score in the top right of the screen
		player_score.display(screen,1050,100)
		# Constantly update the screen
		pygame.display.flip()
		
if __name__ == "__main__":
	main()
