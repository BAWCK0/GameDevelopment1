import pygame
import time
from math import*
import random
import os

pygame.init()

WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping Pong')

font = pygame.font.SysFont('comic sans', 40)

RedPadel = pygame.Rect(35, 250 + 62.5, 35, 125)
BluePadel = pygame.Rect(WIDTH - 70, 250 + 62.5, 35, 125)
Ball = pygame.Rect(WIDTH/2 - 35/2, HEIGHT/2 - 35/2, 35, 35)

SpeedFactor = 1
RedYVel = 0
BlueYVel = 0
BallVel = [(random.randint(0, 1)-0.5)*7.5, (random.randint(0, 1)-0.5)*7.5]


RedI = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Red.png')), (RedPadel.width, RedPadel.height))
BlueI = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Blue.png')), (BluePadel.width, BluePadel.height))
BallI = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Ball.png')), (Ball.width, Ball.height))

RedScore = 0
BlueScore = 0

run = True
FPS = 67
c = pygame.time.Clock()

Reset = pygame.USEREVENT + 1

def render():
    WIN.fill((0, 0, 0))
    WIN.blit(RedI, (RedPadel.x, RedPadel.y))
    WIN.blit(BlueI, (BluePadel.x, BluePadel.y))
    WIN.blit(BallI, (Ball.x, Ball.y))
    WIN.blit(font.render(str(RedScore), True, (255, 0, 0)), (35, 35))
    WIN.blit(font.render(str(BlueScore), True, (0, 0, 255)), (WIDTH-35*1.5, 35))
    pygame.display.update()

def movement(k_p, Red, RedVel, Blue, BlueVel, Ball, BallVel):
    global SpeedFactor, RedScore, BlueScore
    RedVel = 0
    BlueVel = 0
    if k_p[pygame.K_w]:
        RedVel += -7
        
    if k_p[pygame.K_s]:
        RedVel += 7
        
    if k_p[pygame.K_o]:
        BlueVel += -7
        
    if k_p[pygame.K_l]:
        BlueVel += 7    
        
    if Red.top < 0:
        RedVel = 0
        Red.y = 0
        
    elif Red.bottom > HEIGHT:
        RedVel = 0
        Red.y = HEIGHT - Red.height
        
    if Blue.top < 0:
        BlueVel = 0
        Blue.y = 0
        
    elif Blue.bottom > HEIGHT:
        BlueVel = 0
        Blue.y = HEIGHT - Blue.height
    
    if Ball.top < 0:
        Ball.y = 0
        BallVel[1] *= -1
        
    elif Ball.bottom > HEIGHT:
        Ball.y = HEIGHT - Ball.height
        BallVel[1] *= -1
    
    if Ball.left < Red.right and Red.top < Ball.bottom and Red.bottom > Ball.top:
        Ball.x = Red.right
        BallVel[0] *= -1
        BallVel[1] += RedVel/7
        SpeedFactor += 1/SpeedFactor
        
    if Ball.right > Blue.left and Blue.top < Ball.bottom and Blue.bottom > Ball.top:
        Ball.x = Blue.left - Ball.width
        BallVel[0] *= -1
        BallVel[1] += BlueVel/7
        SpeedFactor += 1/SpeedFactor
        
    # i need to add the other collisions
        
    if Ball.left < 0:
        BlueScore += 1
        pygame.event.post(pygame.event.Event(Reset))
        
    if Ball.right > WIDTH:
        RedScore += 1
        pygame.event.post(pygame.event.Event(Reset))
        
    
    Red.y += RedVel*sqrt(SpeedFactor)
    Blue.y += BlueVel*sqrt(SpeedFactor)
    Ball.x += BallVel[0]*SpeedFactor
    Ball.y += BallVel[1]*SpeedFactor

while run:
    c.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            
        elif event.type == Reset:
            SpeedFactor = 1
            Ball.x = WIDTH/2 - 35/2
            Ball.y = HEIGHT/2 - 35/2
            BallVel = [(random.randint(0, 1)-0.5)*7.5, (random.randint(0, 1)-0.5)*7.5]
            RedPadel.y = 250 + 62.5
            BluePadel.y = 250 + 62.5
        
        
            
    
    k_p = pygame.key.get_pressed()
    movement(k_p, RedPadel, RedYVel, BluePadel, BlueYVel, Ball, BallVel)
    render()
    
    if RedScore > 4:
        run = False
        WIN.blit(font.render('Red Wins! :DDDDDD donkey', True, (255, 0, 0)), (0, 0))
        pygame.display.update()
    
    
    elif BlueScore > 4:
        run = False
        WIN.blit(font.render('Blue Wins! :DDDDDDD shrek', True, (0, 0, 255)), (0, 0))
        pygame.display.update()

time.sleep(5)
pygame.quit()
        
        