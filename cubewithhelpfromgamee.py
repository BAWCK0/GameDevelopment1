import pygame
import os
WIDTH, HEIGHT = 500, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Cube Cube Cube Cube Cube Cube Cube Cube Cube Cube Cube Cube Cube Cube Cube Cube Cube Cube Cube Cube Cube Cube')
cube = pygame.Rect(0,0,25,25)
FPS = 60
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
                pygame.quit()
            if e.type == pygame.KEYDOWN:
                if e.type == pygame.K_w:
                    cube.y -= 25/FPS
                if e.type == pygame.K_s:
                    cube.y += 25/FPS
                if e.type == pygame.K_a:
                    cube.x += 25/FPS
                if e.type == pygame.K_d:
                    cube.x -= 25/FPS
main()
                