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
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Ball.png')), (30, 30))
        self.rect = self.image.get_rect()
        
recycleimages = ['las.jpg','pizza.jpg' ,'chipsimg.png']

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
myfont = pygame.font.SysFont('Comic Sans', 22)
timingfont = pygame.font.SysFont('Comic Sans', 22)
text = myfont.render(f'Score = {score}', True, WHITE)

while playing:
    c.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bin.rect.x -= 17.5
                
            if event.key == pygame.K_RIGHT:
                bin.rect.x += 17.5
            
            if event.key == pygame.K_DOWN:
                bin.rect.y += 17.5
                
            if event.key == pygame.K_UP:
                bin.rect.y -= 17.5
                
            if bin.rect.right > WIDTH:
                bin.rect.x = WIDTH-bin.rect.width
                
            if bin.rect.left < 0:
                bin.rect.x = 0
                
            if bin.rect.top > HEIGHT:
                bin.rect.y = HEIGHT
                
            if bin.rect.bottom < 0:
                bin.rect.y = 0 + bin.rect.height
                
            for recyclables in item_list:
                if bin.collidepoint(recyclables):
                    score += 1
                    item_list.remove(recyclables)
                    allsprites.remove(recyclables)
                    text = myfont.render(f'Score = {score}', True, WHITE)
                    
            for nonrecyclables in plastic_list:
                if bin.collidepoint(nonrecyclables):
                    score -= 5
                    plastic_list.remove(nonrecyclables)
                    allsprites.remove(nonrecyclables)
                    text = myfont.render(f'Score = {score}', True, WHITE)
                    
            
            
        timeelapsed = time.time() - start_time
        if timeelapsed >= 60:
            if score >= 10:
                text = myfont.render('Bin loot successful', True, GREEN)
            
            else:
                text = myfont.render('Bin loot FAILED', True, RED)
        
        for sprites in allsprites:
            WIN.blit(sprites.image, sprites.rect) # CAN BE SHORTENED WITH 'allspirtes.draw' 😱😱😱😱😱😱
        
        WIN.blit(text, (250, 40))
        countdown = timingfont.render(f'Time left = {60 - timeelapsed}', True, WHITE)
        WIN.blit(countdown, (20, 10))
        pygame.display.update()
            
pygame.quit()
    
    
