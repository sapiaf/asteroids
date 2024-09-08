import pygame
from constants import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
       screen.fill((0, 0, 0))
       pygame.display.flip()

       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

# This line ensures the main() function is only called when this file is run directly; 
# it won't run if it's imported as a module.
if __name__ == "__main__":
    main()