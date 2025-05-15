import pygame
import random
import os
pygame.font.init()
WIDTH, HEIGTH = 650,600
WIN = pygame.display.set_mode((WIDTH, HEIGTH))
WIN.fill(255,255,255)
pygame.display.set_caption('Match or godzilla will arise')
pygame.display.update

garfield_image = pygame.image.load(os.path.join('Assets', 'garfield.jpg'))
snake_image = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
ghost_image = pygame.image.load(os.path.join('Assets', 'ghostr'))
font = pygame.font.SysFont('wingdings', 40)
texts = {
    'garfield': font.render('Garfield', True, (0,0,0)), 
    'snake': font.render('Snake', True, (0,0,0)),
    'ghost': font.render('Ghost spooookyyyyy', True, (0,0,0))
    }
run = True

game_names = list(texts.keys())
game_names = random.shuffle(game_names[:])
image_position = {
    'garfield': (150, 100),
    'snake': (150, 300),
    'ghost': (150, 500)
}

for name, pos in image_position.items():
    if name == 'garfield':
        WIN.blit(garfield_image, pos)

    elif name == 'snake':
        WIN.blit(snake_image, pos)

    elif name == 'ghost':
        WIN.blit(ghost_image, pos)

ypositions = [100, 300, 500]
labelpositions = {}
for i, name in enumerate(game_names):
    WIN.blit(texts[name], (350, ypositions[i]))
    labelpositions[name] = pygame.Rect(350, ypositions[i], 200, 50)

image_rects = {}

for names, positions in image_position.items():
    image_rects[names] = pygame.Rect(positions[0], positions[1], 175, 175)
    
pygame.display.update()

c_matches = {
    "garfield":"garfield",
    "snake":"snake",
    "ghost":"ghost"
}
user_matches = []
match_count = 0
pos = None

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(WIN, (0, 0, 0), pos, 10, 0)
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
