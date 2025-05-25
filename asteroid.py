from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE
import pygame
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x),int(self.position.y)), int(self.radius), 2)

    def update(self, dt):
        self.position+=self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle=random.uniform(20,50)
            velocity1=self.velocity.rotate(angle)*1.2
            velocity2=self.velocity.rotate(-angle)*1.2
            new_radius=self.radius - ASTEROID_MIN_RADIUS
            asteroid1=Asteroid(self.position.x,self.position.y,new_radius)
            asteroid2=Asteroid(self.position.x,self.position.y,new_radius)
            asteroid1.velocity=velocity1
            asteroid2.velocity=velocity2