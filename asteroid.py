import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # Draw the asteroid as a circle
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Asteroids move in a straight line at a constant speed
        self.position += self.velocity * dt
        

    def is_colliding(self, other):
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius
     

    def split(self):
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
            
        random_angle= random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        self.kill()
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = new_velocity_1 * 1.2
        
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = new_velocity_2 * 1.2
