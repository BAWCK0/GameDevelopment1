import pygame
import os
from math import *
import random

pygame.init()

font = pygame.font.SysFont('Comic Sans', 70)

WIDTH, HEIGHT = 1080, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snakeeeeeeeeeeeeeeeeeeeeeeeeeeee')

# Rects
snake = pygame.Rect(WIDTH/2, HEIGHT/2, 70, 70)
fruit = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 70, 70)
demon = pygame.Rect(0, 0, 70, 70)

# I is short for Image
snakeI = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Black and white California kingsnake.jpg')), (snake.width, snake.height))
fruitI = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'las.jpg')), (fruit.width, fruit.height))
demonI = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'john.jpg')), (demon.width, demon.height))

snakevel = [0, 0]
demonvel = [0, 0]

score = 0
timer = 30

c = pygame.time.Clock()
FPS = 60
run = True

def render():
    WIN.fill((25, 255, 25))
    WIN.blit(snakeI, (snake.x, snake.y))
    WIN.blit(fruitI, (fruit.x, fruit.y))
    WIN.blit(demonI, (demon.x, demon.y))
    WIN.blit(font.render(f'Score = {score}', True, (0, 0, 0)), (14, 14))
    WIN.blit(font.render(f'Time left: {round(timer)}', True, (0, 0, 0)), (14, HEIGHT-80))
    pygame.display.update()
    
def movement(k_p):
    global snake, snakevel, score, fruit, demon
    if demon.x < snake.x:
        demonvel[0] += 3
        
    else:
        demonvel[0] -= 3
        
    if demonvel[1] > snake.y:
        demonvel[1] += 3
        
    else:
        demonvel[1] -= 3
        
    demonvel[0] *= 0.8
    demonvel[1] *= 0.8
        
    if k_p[pygame.K_w]:
        snakevel = [0, -7]
        
    if k_p[pygame.K_a]:
        snakevel = [-7, 0]
        
    if k_p[pygame.K_s]:
        snakevel = [0, 7]
        
    if k_p[pygame.K_d]:
        snakevel = [7, 0]
        
    demon.x += demonvel[0]
    demon.y += demonvel[1]
        
    if snake.left < 0:
        snake.left = 0
        score -= 1000000000
        
    if snake.right > WIDTH:
        snake.right = WIDTH
        score -= 1000000000
        
    if snake.top < 0:
        snake.top = 0
        score -= 1000000000
        
    if snake.bottom > HEIGHT:
        snake.bottom = HEIGHT
        score -= sqrt(10**101)
        
    
        
    if snake.colliderect(fruit):
        score += 1
        fruit.x = random.randint(0, WIDTH-fruit.width)
        fruit.y = random.randint(0, HEIGHT-fruit.height)
        
    if snake.colliderect(demon):
        score -= 3
        snake.x = random.randint(0, WIDTH-snake.width)
        snake.y = random.randint(0, HEIGHT-snake.height)
        
    

while run:
    c.tick(FPS)
    if timer > 0:
        timer -= 1/FPS
        render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
        k_p = pygame.key.get_pressed()
        movement(k_p)
                    
        snake.x += snakevel[0]
        snake.y += snakevel[1]
    
    if timer < 0:
        if score > 15:
            WIN.blit(font.render('You.... WONNN!!!', True, (0, 0, 0)), (WIDTH//2, HEIGHT//2))
            
        else:
            WIN.blit(font.render('You.... are being fed to the hamsters you FAILED >:(', True, (0, 0, 0)), (WIDTH//2, HEIGHT//2))
        pygame.display.update()
