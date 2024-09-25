import pygame
import random
import sys

# Pygame başlat
pygame.init()

# Renk tanımlamaları
BLUE = (135, 206, 235)  # Gökyüzü rengi

# Ekran boyutları
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Ducks")

# Resimleri yükle
sitting_duck_image = pygame.image.load('float.png')  # Oturan ördek resmi
standing_duck_image = pygame.image.load('duck.png')  # Ayakta duran ördek resmi

# Resim boyutunu ayarlama fonksiyonu
def sittin_scale_image(image, width_ratio, height_ratio):
    new_width = int(sitting_duck_image.get_width() * width_ratio)
    new_height = int(sitting_duck_image.get_height() * height_ratio)
    return pygame.transform.scale(image, (new_width, new_height))
def stand_scale_image(image, width_ratio, height_ratio):
    new_width = int(standing_duck_image.get_width() * width_ratio)
    new_height = int(standing_duck_image.get_height() * height_ratio)
    return pygame.transform.scale(image, (new_width, new_height))

# Resimleri ölçeklendir
sitting_duck_image = sittin_scale_image(sitting_duck_image, 0.1, 0.1)  # Boyutunu %10'a ölçeklendir
standing_duck_image = stand_scale_image(standing_duck_image, 0.2, 0.2)  # Boyutunu %10'a ölçeklendir

# Ördek sınıfı
class Duck:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_standing = False  # Ördek oturuyor

    def draw(self):
        if self.is_standing:
            # Ayağa kalkmış ördek
            screen.blit(standing_duck_image, (self.x - standing_duck_image.get_width() // 2, self.y - standing_duck_image.get_height()))
        else:
            # Oturan ördek
            screen.blit(sitting_duck_image, (self.x - sitting_duck_image.get_width() // 2, self.y - sitting_duck_image.get_height()))

# Ördekleri oluştur
ducks = [Duck(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)) for _ in range(10)]

# Ana döngü
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fare pozisyonu
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Ekranı temizle
    screen.fill(BLUE)

    # Ördekleri çiz
    for duck in ducks:
        # Eğer fare ördeğin üzerindeyse, ayağa kalk
        if (duck.x - 30 < mouse_x < duck.x + 30) and (duck.y - 30 < mouse_y < duck.y + 30):
            duck.is_standing = True
        else:
            duck.is_standing = False
        duck.draw()

    # Ekranı güncelle
    pygame.display.flip()
