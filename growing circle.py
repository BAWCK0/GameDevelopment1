import pygame
pygame.init
screen = pygame.display.set_mode((600,600))
screen.fill((255,255,255))
pygame.display.update()
class Circle():
    def __init__(self, pos, color, radius, width):
        self.circle_radius = radius
        self.circle_width = width
        self.circle_color = color
        self.circle_pos = pos
    def draw(self):
        self.draw_circle = pygame.draw.circle(self.circle_color, self.circle_pos, self.circle_width, self.circle_radius)
    def grow(self,r):
        self.circle_radius = self.circle_radius+r
        self.draw_circle
circle = Circle((300,300),(0,0,0),25,0)
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            circle.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
            circle.grow()
            pygame.display.update()