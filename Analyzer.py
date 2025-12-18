from tkinter import *

ROOT = Tk()

NOUNS = ["dog", "dogs", "cat", "cats"]
VERBS = ["running", "eating", "sleeping"]

def find_stuff():
    text = input.get()
    for noun in NOUNS:
        if noun in 

title = Label(text="Analyzer", font=("Arial", 32, "bold"))
title.grid(column=0, row=0)

input = Entry(width=50)
input.grid(column=0, row=1)

button = Button(text="OK", bg="lightblue", command=find_stuff)
button.grid(column=0, row=2)

output = Label(text="NO INPUT")
output.grid(column=0, row=3)


                    
                
                
                
            

ROOT.mainloop()