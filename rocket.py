import pygame
import os
pygame.init()
pygame.display.set_caption('Rockettttttttttttttttttttttttttttttttttttt')
WIN = pygame.display.set_mode((700,500))

class Rocket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
        self.image = pygame.transform.scale(image)
        self.rect = self.image.get_rect()
        
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_a]:
            self.rect.ip(-5,0)