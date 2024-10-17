import pgzrun
import random
HEIGHT = 500
WIDTH = 750
gameover = False
level = 1
time = 10
stars = []
def create_stars():
    for i in range(level):
        star = Actor("star")
        star.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
        stars.append(star)
def draw():
    global time, level
    screen.blit('starbg', (0,0))
    if gameover == False:
        screen.draw.text("level:" + str(level) + (" time:" + str(time)), (375, 450), fontsize = 40)
    else:
        screen.draw.text("GAMEOVER", (WIDTH/2, HEIGHT/2), fontsize = 60)
        screen.draw.text("You made it to level " + str(level), (WIDTH/2, HEIGHT/2 + 100), fontsize=40)
    for i in stars:
        i.draw()
def on_mouse_down(pos):
    global time
    for i in stars:
        if i.collidepoint(pos):
            if gameover == False:
                time = time + 2
            stars.pop(stars.index(i))
def update():
    global time, level
    if 0 >= time:
        gameover == True
    if gameover == False:
        time = time - 0.5
        if len(stars) == 0:
            time = time+50
            level = level+1
            create_stars()
pgzrun.go()