from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
import pygame
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 180
        surface=pygame.Surface((2*PLAYER_RADIUS,2*PLAYER_RADIUS))
        pygame.draw.circle(surface,"red",(int(PLAYER_RADIUS),int(PLAYER_RADIUS)),int(self.radius),2)
        self.image = surface 
        self.rect = surface.get_rect(center=self.position)
        self.gun_timer=0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(),2)

    def rotate(self, dt):
        self.rotation+=PLAYER_TURN_SPEED*dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.gun_timer-=dt
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.gun_timer<=0:
            self.shoot(dt)
            self.gun_timer=PLAYER_SHOOT_COOLDOWN

    def shoot(self, dt):
        shot=Shot(self.position.x,self.position.y)
        shot.velocity=pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
        shot.position+=shot.velocity*dt
        
        