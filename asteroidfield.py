import pygame
import random
from asteroid import Asteroid
from constants import *

#pygame.sprite.Sprite() miras alarak asteriodlerin spawnlarını ayarlıyoruz
class AsteroidField(pygame.sprite.Sprite):
    # Asteroidlerin doğabileceği 4 ekran tanımlıyor her kenar için hız vektörü artı konum hesaplama fonksiyonu yazıyor
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]
    # Constructor
    def __init__(self):
        # oluşturulacak asteroidleri ait olduğu gruba ekliyor, drawable ve updatable
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0 # Asteroid spawn timer

    def spawn(self, radius, position, velocity): # spawner radius position ve velocitye göre asteroid spawnlayıcı
        asteroid = Asteroid(position.x, position.y, radius) # Asteroid sınıfından onun self bilgileriyle asteroid bilgileri tanımlanıyor ( Asteroid sınıfının x,y konumu ve radius bilgisi vardı)
        asteroid.velocity = velocity # velocityde burada veriyoruz

    def update(self, dt): #Update etme fonksiyonu
        # delta süresine göre update, zamanlayıcı yani
        self.spawn_timer += dt
        # eğer timer minimum max spawn süresini aşarsa zamanlalyıcı sıfırlanır
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # Sıfırdan sonra asteroid spawn için bilgiler
            edge = random.choice(self.edges)                           # rastgele kenar
            speed = random.randint(40, 100)                            # 40 100 arası rastgele hız
            velocity = edge[0] * speed                                 # kenar vektörü ile hız çarpıp son hız vektörü
            velocity = velocity.rotate(random.randint(-30, 30))        # hıza açı verir
            position = edge[1](random.uniform(0, 1))                   # rastgele konum kenarda
            kind = random.randint(1, ASTEROID_KINDS)                   # ASTEROID_KINDS içinden rastgele asteroid
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity) # bu bilgilerle yeni asteroid spawn
