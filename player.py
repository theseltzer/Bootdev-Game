import pygame
from constants import *

from circleshape import *
from shot import Shot
# Circleshapeten miras alıyor
class Player(CircleShape):
    # Constructor
    def __init__(self, x,y):
        # X,y yarıçapı ana sınıfa circleshape gönderiyor
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation=0 # Oyuncunun başlangıçta rotasyonu sıfır
        self.timer = 0  # ateş etme timer 0
        # oyuncu üçgen şeklinde bu köşelerin tasarımı ve bilgilerin gönderilmesi
    def triangle(self):
        # oyuncunun baktığı yönün vektörü
        forward = pygame.Vector2(0,-1).rotate(self.rotation)
        # Oyuncunun sağ sol yön vektörü
        right = pygame.Vector2(1, 0).rotate(self.rotation) * self.radius / 1.5
        # Oyuncunun yani üçgenin köşe bilgileri
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c] # Çizim için köşeler
    

    # Polygon kullanarak oyuncuyu yani üçgeni çiziyor
    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)
    
    # Oyuncunun dönüşü, dönüş açısı + dönüş hızı artı delta
    def rotate(self,dt):
        self.rotation+= PLAYER_TURN_SPEED * dt
    

    # oyuncu durum güncelleme
    def update(self, dt):
        # Ateş etme sayacı sonsuz floattan kurtarmak için sıfırn altına düşmesini engeller
        self.timer = max(0, self.timer-dt)
        # tuşa basılma durumu
        keys = pygame.key.get_pressed()
        # tuşlar ve aksiyonları
        if keys[pygame.K_a]: # sol
            self.rotate(-dt)
        if keys[pygame.K_d]: # sağ
            self.rotate(dt)
        if keys[pygame.K_w]: # ileri
            self.move(dt)
        if keys[pygame.K_s]: # geri
            self.move(-dt)

        if keys[pygame.K_SPACE] and self.timer <=0: # ateş
                self.shoot()
    
    # hareket
    def move(self,dt):
        # ileri doğru vektör
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        # konum hız + zaman güncelleme
        self.position += forward * PLAYER_SPEED *dt


    # ateş
    def shoot(self):
        #oyuncu konumunda mermi spawn
        shot = Shot(self.position.x, self.position.y)
        
        # Merminin hızını oyuncunun baktığı yöne ve atış hızına göre ayarla
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        shot.velocity = forward * PLAYER_SHOOT_SPEED

        # ateş etme sayacı cooldown
        self.timer = PLAYER_SHOOT_COOLDOWN
