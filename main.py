# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS, PLAYER_RADIUS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    dt=0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player=Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroidfield=AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        
        for item in updatable:
            item.update(dt)
        for asteroid in asteroids:
            if player.detect_collision(asteroid):
                raise SystemExit("Game over!")
        
        for shot in shots:
            for asteroid in asteroids:
                if shot.detect_collision(asteroid):
                    pygame.sprite.Sprite.kill(shot)
                    #pygame.sprite.Sprite.kill(asteroid)
                    asteroid.split()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt=clock.tick(60)/1000
        
if __name__=="__main__":
    main()