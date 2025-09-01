import pygame
import random
from circleshape import CircleShape # Miras alınan kütüphane
from constants import *             # Constants


class Asteroid(CircleShape):           # CircleShapeten miras alıyor asteroid bir CircleShape
    def __init__(self, x, y, radius):  # Constructor
        super().__init__(x, y, radius) # Circleshapeten konum x,y ve yarıçap alıyoruz

    def draw(self, screen):
        # Asteroidi pygame ile beyaz çiziyoruz  pozisyon ve radius inherit ediliyor 2 pixel kalınlığında çizim
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # asteroidlerin hareketi update ediliyor, dt ile oyun hızına entegre
        # dt bir onceki kareden bu kareye geçen zaman delta time
        # konumu hızına bir dt ekleyerek çiziyor her karede
        self.position += self.velocity * dt
        

    def is_colliding(self, other):
        # collide detection
        # iki nesnenin merkezleri arasındaki mesafeyi hesaplıyor
        distance = self.position.distance_to(other.position)
        # mesafe iki nesnenin yarı çapından küçükse true dönüyoruz ve oyun döngüsünde collide çalışıyor
        return distance <= self.radius + other.radius
     
        # collide sonrası parçalama
    def split(self):
        # eğer mermi ile collide gerçekleşen asteroid yarı çapı min değerden küçükse kill
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return # fonksiyon sonlandırıyor
        
        # parçalanan asteroid parçaları için rastgele açı 20 ile 50 arası
        random_angle= random.uniform(20, 50)
        # parçalanan asteroidlerin yeni yarı çapı
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # Orjinal asteroid ded
        self.kill()
        # yeni asteroidlere eski hızı rastgele açılar vererek vektörleştirme
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)
        # 1. parça tanımlaması  ve hızı (biraz daha hızlı büyüğünden 1.2 katsayı verdik
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = new_velocity_1 * 1.2
        # 2. parça için aynısı
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = new_velocity_2 * 1.2
