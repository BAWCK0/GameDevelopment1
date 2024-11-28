class Student():
    name = ""
    age = "Type your age."
    schoolclass = "Grade 6"
    classteacher = "Mr Teacher"
    def __init__(self):
        print("Making a new student")
    def change_details(self):
        print("Please type your age. ")
        self.age = int(input())
        print("Please enter the name of the student. ")
        self.name = input()
    def show_details(self):
        print("The details of student are")
        print("name:", self.name)
        print("age:", self.age)
        print("Teacher:", self.classteacher)
        print("Grade:", self.schoolclass)
ramiro = Student()
timither = Student()
peppa_pig = Student()
ramiro.change_details()
ramiro.show_details()
timither.show_details()
    