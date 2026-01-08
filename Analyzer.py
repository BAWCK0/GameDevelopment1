from tkinter import *

ROOT = Tk()

NOUNS = ["dog", "dogs", "cat", "cats", "hamster"]
VERBS = ["running", "ran","run", "eating", "sleeping", "ate", "come", "hamsterified"]

def find_stuff():
    text = input.get()
    found_nouns = []
    found_verbs = []
    for noun in NOUNS:
        if noun in text:
            found_nouns.append(noun)
        
    for verb in VERBS:
        if verb in text:
            found_verbs.append(verb)
            
    output.config(text=f"{found_verbs[0]} is a verb and {found_nouns[0]} is a noun.")
            

title = Label(text="Analyzer", font=("Arial", 32, "bold"))
title.grid(column=0, row=0)

input = Entry(width=50)
input.grid(column=0, row=1)

button = Button(text="OK", bg="lightblue", command=find_stuff)
button.grid(column=0, row=2)

output = Label(text="NO INPUT")
output.grid(column=0, row=3)


                    
                
                
                
            

ROOT.mainloop()
