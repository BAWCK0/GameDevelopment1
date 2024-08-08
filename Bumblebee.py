import pgzrun
import random
WIDTH = 500
HEIGHT = 500
score = 0
gameover = False
bee = Actor("bee")
bee.scale = 0.05
bee.pos = 400, 400
flower = Actor("flower")
flower.pos = 100, 100

def draw():
    screen.blit('fieldbackground', (0,0))
    bee.draw()
    flower.draw()
    screen.draw.text('score:' + str(score),color = "yellow", topleft=(10,10))
    if gameover:
        screen.fill('black')
        screen.draw.text('Gameover, your final score was' +str(score),midtop=(WIDTH/2,12),fontsize=35,color='yellow')

def update():
    global score
    if keyboard.A:
        bee.x = bee.x-4
    if keyboard.D:
        bee.x = bee.x+4
    if keyboard.W:
        bee.y = bee.y-4
    if keyboard.S:
        bee.y = bee.y+4
    if bee.colliderect(flower):
        moveflower()
        score = score+1



def moveflower():
    flower.x = random.randint(50,WIDTH-50)
    flower.y = random.randint(50,HEIGHT-50)

def time_up():
    global gameover
    gameover = True

clock.schedule(time_up,10)

pgzrun.go()