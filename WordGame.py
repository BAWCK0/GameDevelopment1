from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Word Game!")

score = 0

Title = Label(root, text="Word Game for GOBLINS.")
Title.grid(row=1, column=1, columnspan=2)

Word_Entry = Entry(root)
Word_Entry.grid(row=3, column=1)

Word_Display = Label(root, text="")
Word_Display.grid(row=2, column=1, columnspan=2)

Score_Display = Label(root, text="Score: 0")
Score_Display.grid(row=4, column=1, columnspan=2)

def Submit():
    global wordchoice, scrambled_word, e, score
    if Word_Entry.get().lower() == wordchoice.lower():
        messagebox.showinfo("Corret! :D", "You're NOT a goblin!")
        score += 1
        Score_Display.config(text=f"Score: {score}")
    
    else:    
        messagebox.showerror("WRONG NOOB", f"ABSOLUTELY MASSIVE GOBLIN, THE WORD WAS {wordchoice.upper()} 👺👺👺👺👺👺👺")
        score -= 1
        Score_Display.config(text=f"Score: {score}")
        
        
    wordchoice = words[random.randint(0, 13)]
    e = list(wordchoice)
    random.shuffle(e)
    scrambled_word = "".join(e)
    Word_Display.config(text=scrambled_word)
        

Submit_Button = Button(root, text="Submit :D", bg="lime", command=Submit)
Submit_Button.grid(row=3, column=2)



words = ["House", "Hippopotomonstrosesquippedaliophobia",
         "Hi", "Dinosaur", "Continent", "Skeleton",
         "Controling", "Random", "TEST",
         "Pneumonoultramicroscopicsilicovolcanoconiosis",
         "Computer", "Taimuresu", "Elephant", "Goblin 👺"]

wordchoice = words[random.randint(0, 13)]
e = list(wordchoice)
random.shuffle(e)
scrambled_word = "".join(e)
Word_Display.config(text=scrambled_word)

root.mainloop()