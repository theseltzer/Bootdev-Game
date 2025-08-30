import pygame
from constants import *

from circleshape import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation=0
        self.timer = 0
        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0,-1).rotate(self.rotation)
        right = pygame.Vector2(1, 0).rotate(self.rotation) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)
    def rotate(self,dt):
        self.rotation+= PLAYER_TURN_SPEED * dt
    def update(self, dt):
        self.timer = max(0, self.timer-dt)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE] and self.timer <=0:
                self.shoot()
    def move(self,dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED *dt



    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        
        # Merminin hızını oyuncunun baktığı yöne ve atış hızına göre ayarla
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN
