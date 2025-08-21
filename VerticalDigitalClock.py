from tkinter import *
from tkinter.ttk import *
from time import strftime
import random

fonts = ["arial", "wingdings", "", "papyrus"] 

root = Tk()
root.title("Kllawhcque")

def timeeee():
    time = strftime("%Hh\n%Mm\n%Ss\n%p")
    clock.config(text=time, font=(fonts[random.randint(0, len(fonts)-1)], 70, "bold"))
    clock.after(1000, timeeee)

clock = Label(root, text="", font=(fonts[random.randint(0,len(fonts)-1)], 70, "bold"), foreground="white", background="red")
clock.pack()

timeeee()

root.mainloop()