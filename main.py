import pygame
import sys
from constants import *
from player import *
from asteroidfield import *
from asteroid import *
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
   
   
    # Pygame'i başlat
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Oyun nesnelerini tutacak grupları oluştur
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Statik container alanlarını ayarla
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)


    # Oyuncu ve asteroit alanı nesnelerini oluştur
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)

    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        
        for astero in asteroids:
            if astero.is_colliding(player):
                print("Game over")
                sys.exit()
        for astero in asteroids:
            for bullet in shots:
                if bullet.is_colliding(astero):
                    astero.split()
                    bullet.kill()

        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()


