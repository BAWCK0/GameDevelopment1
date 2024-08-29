#The best simulator ever made in history. Game of the year, decade and century.
import random
import pgzrun
HEIGHT = 500
WIDTH = 500
score = 0
loose = False
garfield = Actor("garfield")
las = Actor("las")
john = Actor("john")
las.x = random.randint(100,400)
las.y = random.randint(100,400)
    
def movement():
    if john.x >= garfield.x:
        john.x = john.x-1
    else:
        john.x = john.x+1
    if john.y >= garfield.y:
        john.y = john.y-1
    else:
        john.y = john.y+1
    if garfield.colliderect(john):
        loose = True
    
    if keyboard.W:
        garfield.y = garfield.y-5
    if keyboard.A:
        garfield.x = garfield.x-5
    if keyboard.S:
        garfield.y = garfield.y+5
    if keyboard.D:
        garfield.x = garfield.x+5
def draw():
    screen.fill("white")
    garfield.draw()
    las.draw()
    john.draw()
    screen.draw.text('score:' + str(score),color = "orange", topleft=(10,10))
    if loose:
        screen.draw.text('Gameover, your final score was' +str(score),midtop=(WIDTH/2,12),fontsize=35,color='orange')
def update():
    global loose
    global score
    if not loose:
        movement()
        draw()
        if las.colliderect(garfield):
            las.x = random.randint(100,400)
            las.y = random.randint(100,400)
            score = score+1
pgzrun.go()