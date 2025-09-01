import pygame #pygame kütüphanesi
import sys    #sys kütüphanesi


from constants import *     #Sabit değerlerin(oyun başında veya tekrarlanan eylemlarin oyun başladığında etkilemeyeceği) olduğu veriler
from player import *        #CircleShapeden miras alan ve aynı zamanda kendisi de bir circle shape olan oyuncu sınıfının karakteri kararları ve fonksiyonları
from asteroidfield import * #CircleShapeden miras alan rastgele asteroidlerin generate edildiği zemin
from asteroid import *      #CircleShapeden miras alan rastgele asteroidlerin davranışları, boyutları, fonksiyonları
from shot import Shot       #CircleShapeden miraz alan ve player ile asteroid ile etkileşimde olan kendisi de  CircleShape olan shotların obje bilgileri


score= 0

def main():
    global score
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
   
   
    # Pygame başlatıcı
    pygame.init()
    #Oyun ekranını ayarlar Genişlik ve yükseklik
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Oyun nesneleri
    updatable = pygame.sprite.Group()  #Her döngüde güncellenecek nesneler Konum, hız
    drawable = pygame.sprite.Group()   #Ekrana çizilecek nesneler
    asteroids = pygame.sprite.Group()  #Sadece asteroidler collision için
    shots = pygame.sprite.Group()      #Sadece atışlar collision için
    
    # Statik container Oluşturulduğunda ekleneceği gruplar
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)


    # Oyuncu ve asteroit alanı nesneleri
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)

    asteroid_field = AsteroidField()
    
    #Oyun hızını belirlemek için saat
    clock = pygame.time.Clock()
    dt = 0
    
    #Puanı ekranda göstermek için font
    font = pygame.font.Font(None,36)

    #ANA OYUN DÖNGÜSÜ
    while True:
       
        #pygame işlemleri klavye, ekran kapatma vs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #Eğer pencere kapanırsa oyun sonlandırır
                return

        #Ekranı siyah yapar bir önceki kareyi siler
        screen.fill("black")
        #Updatable containerdaki nesneleri günceller(konum hareket vb
        updatable.update(dt)
        
        #Oyuncu ve asteroid arası çapışma kontrolü
        for astero in asteroids:
            if astero.is_colliding(player):
                #Çarpışma halinde game over yazar ve oyunu siler
                print("Game over")
                sys.exit()


        #Mermiler ve asteroidler arasında çarpışma kontrolü
        for astero in asteroids:
            for bullet in shots:
                if bullet.is_colliding(astero):
                    #puanlama
                    
                    
                    if astero.radius>= 25:
                        
                        score += 100
                    elif astero.radius <25 and astero.radius >=15:
                        score += 50

                    elif astero.radius <15 and astero.radius >=0:
                        score += 25

                    #Çarpışma durumunda  büyük asteroidler parçalanır
                    astero.split()
                    #Mermi kill
                    bullet.kill()
        #Drawable nesneleri çiz
        for thing in drawable:
            thing.draw(screen)

         #Ekrana puan metni yazdırma (255ler beyaz renk)
        score_text = font.render(f"Score:{score}", True, (255,255,255))
        screen.blit(score_text,(10,10))


        #ekranı günceller, çizimler görünür
        pygame.display.flip()
        #oyun hızını sınırlar saniyede 60 kare
        dt = clock.tick(60)/1000

#bu dosya doğrudan çalıştırılıyorsa, main fonksiyonunu çalıştırır( Linuz terminalde uv main.py çağırdığımızda, Oyunun döngüsünü başlatan main fonksiyonu çağırılır
if __name__ == "__main__":
    main()
 

