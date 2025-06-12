import pygame
import os
pygame.init()
pygame.display.set_caption('Rockettttttttttttttttttttttttttttttttttttt')
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

class Rocket(pygame.sprite.Sprite):
    def __init__(self, coordinates):
        super().__init__()
        image = pygame.image.load(os.path.join('Assets', 'garfield.jpg'))
        self.image = pygame.transform.scale(image, (25, 25))
        self.rect = self.image.get_rect()
        self.coordinates = coordinates
        self.rect.x, self.rect.y = self.coordinates[0], self.coordinates[1]
        
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_a]:
            self.rect.x += -5
        
        if pressed_keys[pygame.K_d]:
            self.rect.x += 5
            
        if pressed_keys[pygame.K_w]:
            self.rect.y += -5
            
        if pressed_keys[pygame.K_s]:
            self.rect.y += 5
        
        if self.rect.left < 0:
            self.rect.x = 0
            
        if self.rect.right > WIDTH:
            self.rect.x = WIDTH-25
            
        if self.rect.top < 0:
            self.rect.y = 0
        
        if self.rect.bottom > HEIGHT:
            self.rect.y = HEIGHT-25
            
    def render(self):
        WIN.blit(self.image, (self.rect.x, self.rect.y))
        pygame.display.update()
        
c = pygame.time.Clock()
bigboi = Rocket((0,0))
eaboi = Rocket((100, 100))
while True:
    c.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    k_p = pygame.key.get_pressed()
    WIN.fill((0, 0, 0))
    bigboi.update(k_p)
    bigboi.render()
    eaboi.update(k_p)
    eaboi.render()