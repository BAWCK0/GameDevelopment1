import pygame
import random
import os
pygame.font.init()
WIDTH, HEIGTH = 500,800
WIN = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption('Match or godzilla will arise with 10000000000000000000000000000000000 other godzillas')
garfield_box = pygame.Rect(10,10, 170, 170)
snake_box = pygame.Rect(10,190, 170, 170)
garfield_image = pygame.image.load(os.path.join('Assets', 'garfield.jpg'))
snake_image = pygame.transform.rotate(pygame.transform.scale((snake_box.height, snake_box.width, 90)))

run = True


