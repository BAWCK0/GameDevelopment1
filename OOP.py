class Cat():
    def __init__(self, Name, Age, Speed):
        self.name = Name
        self.age = Age
        self.speed = Speed
    def showcatname(self):
        print(f"The cats name is {self.name}.")

    def showcatage(self):
        print(f"The cat is {self.age} years old")

    def showcatspeed(self):
        print(f"The cats speed is {self.speed}m/s")

Supreme_Cat = Cat('SC', 3**27, 3*10**7)
Supreme_Cat.showcatage()
Supreme_Cat.showcatspeed()
Normal_Cat = Cat('Gato', 2, 4**(4**4))
Normal_Cat.showcatname()
Normal_Cat.showcatage()
Normal_Cat.showcatspeed()