import pygame
pygame.init()
screen = pygame.display.set_mode([600,600])
screen.fill((255,255,255))
pygame.display.update()
class Circle():
    def __init__(self, pos, color, radius, width):
        self.circle_radius = radius
        self.width = width
        self.circle_color = color
        self.circle_pos = pos
    def draw(self):
        pygame.draw.circle(self.circle_color, self.circle_pos, self.width, self.circle_radius)
    def grow(self,r):
        self.circle_radius += r
        pygame.draw.circle(self.circle_color, self.circle_pos, self.circle_radius, self.width)
pos = (300,300)
radius = 50
width = 2
pygame.draw.circle(screen,(255,0,0), pos, radius, width)
pygame.display.update()
red_circle = Circle("red", pos, radius+40)
blue_circle = Circle("blue", pos, radius+60,)
green_circle = Circle("green", pos, 20)
yellow_circle = Circle("yellow", pos, radius, 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            red_circle.draw()
            blue_circle.draw()
            green_circle.draw()
            yellow_circle.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
            red_circle.grow(2)
            blue_circle.grow(2)
            green_circle.grow(2)
            yellow_circle.grow(2)
            pygame.display.update()
        elif event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            pygame.display.update