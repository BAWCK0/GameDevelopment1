import pgzrun
WIDTH = 500
HEIGHT = 500
def draw():
    w = WIDTH - 250
    h = HEIGHT
    r = 255
    g = 0
    b = 55
    for i in range (20):
        ob = Rect((0,0),(w,h))
        ob.center=(250,250)
        screen.draw.rect(ob, (r,g,b))
        w = w+20
        h = h-20
        r = r-10
        g = g +10
pgzrun.go()