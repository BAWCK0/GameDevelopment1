import pygame
import os

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #Sets the window up
pygame.display.set_caption('Game :)') #Sets the name of the window
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH/2, 0, 10, HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/')

HEALTH_FONT = pygame.font.SysFont('wingdings', 42)
WINNER_FONT = pygame.font.SysFont('wingdings', 126)

FPS = 60
VEL = 7
BULLET_VEL = VEL/2
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 60,50

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets'), 'spaceship_yellow.png')
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets'), 'spaceship_red.png')
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_HEIGHT, SPACESHIP_WIDTH, 90))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_HEIGHT, SPACESHIP_WIDTH, 90))
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

def main():
    red = pygame.Rect(700,300,SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(700,300,SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red_bullets = []
    yellow_bullets = []
    
    red_health = 10
    yellow_health = 10
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                run = False
                pygame.quit()
            if eve.type == pygame.KEYDOWN:
                if eve.key == pygame.K.LCTRL and len(yellow_bullets < MAX_BULLETS):
                    bullet = pygame.Rect(YELLOW.x + yellow.width, YELLOW.y + yellow.height/2, 10,5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                    
            if eve.key == pygame.K.RCTRL and len(red_bullets < MAX_BULLETS):
                    bullet = pygame.Rect(RED.x, RED.y + red.height/2, 10,5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

