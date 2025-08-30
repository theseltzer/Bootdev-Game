import pygame
from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        # Draw the asteroid as a circle
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Asteroids move in a straight line at a constant speed
        self.position += self.velocity * dt


    def is_colliding(self, other):
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius
