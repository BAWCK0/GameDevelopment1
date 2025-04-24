import pygame
import random
import os
WIDTH, HEIGHT = 500*1.5, 800*1.5
WIN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.init()
pygame.display.set_caption('First pgzero game remade in pygame')
score = 0
gh = pygame.Rect(0, 0, 73, 51)
ghost = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'ghostr.png')), (gh.height, gh.width))
ACEL = 5
ghxv = 0
ghyv = 0
FPS = 60
c = pygame.time.Clock()
run = True

def ghost_movement(rmv):
    mx, my = pygame.mouse.get_pos()
    global ghxv, ghyv
    ghxv += random.randint(0-rmv, rmv)
    ghyv += random.randint(0-rmv, rmv)
    
    if gh.x + gh.width/2 > mx:
        ghxv -= ACEL
    
    elif gh.x + gh.width/2 < mx:
        ghxv += ACEL

    if gh.y + gh.height/2 > my:
        ghyv -= ACEL
    
    elif gh.y + gh.height/2 < my:
        ghyv += ACEL
    
    ghxv *= 0.9
    ghyv *= 0.9
    gh.x += ghxv/20
    gh.y += ghyv/20

def render():
    WIN.fill((0,0,0))
    WIN.blit(ghost, (gh.x, gh.y))
    pygame.display.update()

def main():
    global run, score
    while run:
        score += 1
        c.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        if gh.collidepoint(pygame.mouse.get_pos()):
            print(score)
        ghost_movement(ACEL)
        render()
main()