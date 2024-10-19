# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *
import pygame
def main():
	pygame.init
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	while True:
		# Check if user has closed window
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		# Fill the screen with black
		screen.fill((0, 0, 0))
		# Constantly refresh the black
		pygame.display.flip()
if __name__ == "__main__":
	main()
