class Student():
    Eyes = ""
    Noses = ""
    Arms = ""
    Legs = ""
    Toes = ""
    Fingers = ""
    Paws = ""
    Claws = ""
    Ears = ""
    
    def __init__(self):
        print("Making a new humanoid creature")
    
    def create_creature(self):
        print("How many eyes?")
        self.Eyes = int(input())

        print("How many noses")
        self.Noses = input()

        print("How many arms?")
        self.Arms = input()

        print("How many legs?")
        self.Legs = input()

        print("How many toes?")
        self.Toes = input()

        print("How many fingers?")
        self.Fingers = input()

        print("How many paws?")
        self.Paws = input()

        print("How many claws?")
        self.Claws = input()

        print("How many ears?")
        self.Ears = input()
    
    def show_creature_details(self):
        print("The details of this creature is...")
        print("Eyes:", self.Eyes)
        print("Noses:", self.Noses)
        print("Arms:", self.Arms)
        print("Legs:", self.Legs)
        print("Toes:", self.Toes)
        print("Fingers:", self.Fingers)
        print("Paws:", self.Paws)
        print("Claws:", self.Claws)
        print("Ears:", self.Ears)

humanoid_creature = Student()
humanoid_creature.create_creature()
humanoid_creature.show_creature_details()
            