# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS

def main():
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    dt=0
    number=1

    while number!=0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        number-=2
        pygame.Surface.fill(screen,color=(0,0,0))
        pygame.display.flip()
        dt=clock.tick(60)/1000

if __name__=="__main__":
    main()