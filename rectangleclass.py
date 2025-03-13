class Rectangle():
    def __init__(self, Width, Height, Color, Name, Position, Rotation):
        self.width = Width
        self.height = Height
        self.color = Color
        self.name = Name
        self.position = Position
        self.rotation = Rotation
        
    def showrectshape(self):
        print(f"{self.name} the rectangle is {self.width} units wide and {self.height} units high along with the area being rotated degrees")
        
    def showrectcolor(self):
        print(f"{self.name} the rectangle is coloured {self.color}")
        
    def showrectposition(self):
        print(f"{self.name} is located at ({self.position[0]}, {self.position[1]})")
        
    def showrectarea(self):
        print(f"{self.name} the rectangle has an area of {self.width*self.height} square units")
Bobby = Rectangle(3**(3**3), (2**(0.5**10))-1, 'Crimson', 'Bobby', [0,0], 45)
Square = Rectangle(25, 25, 'Blue', 'Square', [100,126], 0)
Square.showrectposition()
Bobby.showrectshape()
Bobby.showrectarea()