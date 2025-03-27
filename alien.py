import pgzrun
import random
HEIGHT = 500
WIDTH = 500
score = 0
Alien = Actor("spaceship_red.png")
text = "Click the ALIEN"

def draw():
    screen.clear()
    screen.fill(color=(35,35,35))
    Alien.draw()
    screen.draw.text(text, center=(400,250), fontsize = 20)
    screen.draw.text(f"Your score is {score}", center=(100, 250), fontsize = 10)
    
def replace_alien():
    Alien.x = random.randint(75, WIDTH - 75)
    Alien.y = random.randint(75, HEIGHT - 75)
    
def on_mouse_down(pos):
    global score, text
    if Alien.collidepoint(pos):
        replace_alien()
        score += 1
        text = "You hit the alien :D"
    else:
        text = "It was... WORTH A SHOT HAHAHA (LAUGH NOW BEFORE I SUMMON ZEUS AND 10^60 FACTORIAL SQUARED HAMSTERS)"
        score -= 1
pgzrun.go()
    
    
