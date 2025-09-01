import pygame
from circleshape import CircleShape
from constants import *

# Circleshape miras 
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS) # mermi boyutu ve konumu

    def draw(self, screen):
        # mermiyi çizer
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # mermi konum güncelleme
        self.position += self.velocity * dt

        # mermi collide hesaplama 
    def is_colliding(self, other):
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius
