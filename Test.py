import pgzrun
HEIGHT = 480
WIDTH = 480
billy = Actor("billy")
billy.x = 240
billy.y = 240
def draw_billy():
    screen.clear()
    billy.draw()
def movement():
    if keyboard[keys.W]:
        billy.y = billy.y-3
    if keyboard[keys.S]:
        billy.y = billy.y+3
    if keyboard[keys.A]:
        billy.x = billy.x-3
    if keyboard[keys.D]:
        billy.x = billy.x+3
def update():
    movement()
    draw_billy()
pgzrun.go()