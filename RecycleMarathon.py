import pygame
import os
import random
import time

pygame.init()   

pygame.display.set_caption('Yes')
HEIGHT, WIDTH = 800, 800
WIN = pygame.display.set_mode((HEIGHT, WIDTH))
class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'garfield.jpg')), (50, 70))
        self.rect = self.image.get_rect()

class Recycalable(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', img)), (30, 30))
        self.rect = self.image.get_rect()
        
class Non_Recycalable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'garfield.jpg')), (30, 30))
        self.rect = self.image.get_rect()
        
recycleimages = ['las.jpg','pizza.jph' ,'chipsimg.png']

item_list = pygame.sprite.Group()
allsprites = pygame.sprite.Group()
plastic_list = pygame.sprite.Group()

for i in range(60):
    item = Recycalable(random.choice(recycleimages))
    item.rect.x = random.randrange(WIDTH)
    item.rect.y = random.randrange(HEIGHT)
    item_list.add(item)
    allsprites.add(item)
    
for i in range(28):
    item = Non_Recycalable()
    item.rect.x = random.randrange(WIDTH)
    item.rect.y = random.randrange(HEIGHT)
    plastic_list.add(item)
    allsprites.add(item)
    
bin = Bin()
allsprites.add(bin)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

playing = True
score = 0
c = pygame.time.Clock()
start_time = time.time()
myfont = pygame.font.SysFont('WingDings', 22)
timingfont = pygame.font.Sysfont('WingDings', 22)
text = myfont.render(f'Score = {score}', True, WHITE)

while playing:
    c.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bin.x -= 17.5
                
            if event.key == pygame.K_RIGHT:
                bin.x += 17.5
            
            if event.key == pygame.K_DOWN:
                bin.y += 17.5
                
            if event.key == pygame.K_UP:
                bin.y -= 17.5
                
            if bin.right > WIDTH:
                bin.x = WIDTH-bin.width
                
            if bin.left < 0:
                bin.x = 0
                
            if bin.top > HEIGHT:
                bin.y = HEIGHT
                
            if bin.bottom < 0:
                bin.y = 0 + bin.height
                
            for recyclables in item_list:
                if bin.collidepoint(recyclables):
                    score += 1
                    item_list.remove(recyclables)
                    allsprites.remove(recyclables)
                    
            for nonrecyclables in plastic_list:
                if bin.collidepoint(nonrecyclables):
                    score -= 5
                    plastic_list.remove(nonrecyclables)
                    allsprites.remove(nonrecyclables)
                    
            
            
        timeelapsed = time.time() - start_time
        if timeelapsed >= 60:
            if score >= 10:
                text = myfont.render('Bin loot successful', True, GREEN)
            
            else:
                text = myfont.render('Bin loot FAILED', True, RED)
        
        for sprites in allsprites:
            WIN.blit(sprites.image, sprites.rect)
        
        WIN.blit(text, (250, 40))
        countdown = timingfont.render(f'Time left = {60 - timeelapsed}', True, WHITE)
        WIN.blit(countdown, (20, 10))
            
    
    
