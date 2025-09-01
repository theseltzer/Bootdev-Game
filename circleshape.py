import pygame

# Pygameden miras alarak tüm oyun objelerini buradan tasarlıyoruz, sıfır noktası
class CircleShape(pygame.sprite.Sprite):
    # Consturctor
    def __init__(self, x, y, radius):
        # self.containers özelliği varsa bu gruba ekliyor(updatable drawable)
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        # konum hız yarıçap
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):        
	# alt sınıflarda override ediliyor
        pass

    def update(self, dt):
        # alt sınıflarda override ediliyor
        pass

    # Çarpışma hesaplama
    def is_colliding(self,other):
        distance = self.position.distance_to(other.position)
        return distance< self.radius + other.radius
