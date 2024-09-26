#C:\Users\s_ort\OneDrive\Desktop\Jetlearn coding\GameDevelopment 1

import pgzrun
import random
from time import time
HEIGHT = 600
WIDTH = 800
starttime = 0
totaltime = 0
endtime = 0
nos = 11
satelites = []
next_satelite = 0
lengths = []

def create_satelites():
    global starttime
    for i in range(nos):
        satelit = Actor("garfield")
        satelit.pos = random.randint(40,WIDTH-40), random.randint(40,HEIGHT-40)
        satelites.append(satelit)
    starttime = time()
#If you eat 27 hamsters, is it still 27 hamsters?
def draw():
    global totaltime
    screen.blit('spacebackground', (0,0))
    number = 1
    for i in satelites:
        screen.draw.text(str(number), (satelites.pos[0], satelites.pos[1]+10))
        i.draw()
        number = number+1
    for j in lengths:
        screen.draw.line(j[0],j[1],(255,255,255))
    if next_satelite < nos:
        totaltime = time()-starttime
    screen.draw.text(str(round(totaltime,1)),(10,10),fontsize = 30)

def on_mouse_down(pos):
    global next_satelite, lengths
    if next_satelite < nos:
        if satelites[next_satelite].collidepoint(pos):
            if next_satelite:
                lengths.append((satelites[next_satelite-1].pos,satelites[next_satelite].pos))
            next_satelite = next_satelite+1
        else:
            lengths=[]
            next_satelite = 0
create_satelites()
pgzrun.go()