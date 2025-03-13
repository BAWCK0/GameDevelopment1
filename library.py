class Book:
    def __init__(self, Title, Author, AVST):
        self.title = Title
        self.author = Author
        self.avst = AVST
    
    def showbooktitle(self, bookcreator):
        if self.author == bookcreator:
            print(f"The name of this book is {self.title}")
        else:
            print(f"wrong author")
    
    def showbookauthor(self, bookname):
        if self.title == bookname:  
            print(f"The author of {self.title} is {self.author}")
        else:
            print("Wrong bookname")
            
    def showbookavst(self, bookname):
        if self.title == bookname:
            if self.avst:
                print("This book is available")
            else:
                print("This book is not available 😂🤣🤣🤣😆")
        else:
            print("Wrong book name")
    
class Library:
    def __init__(self):
        self.collection = []
    
    def addbook(self, bookname, author, avst):
        self.collection.append((bookname, author, avst))
        
    def removebook(self, bookname):
        for i in range(len(self.collection)):
            if self.collection[i][0] == bookname
        