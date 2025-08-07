from tkinter import *
from tkinter.ttk import *
from time import strftime
import random

colors = ["red", "green", "blue", "yellow", "violet", "orange", "grey", "lightgrey", "brown", "pink"]

root = Tk()
root.title("CLOOCK")

title = Label(root, font=("arial", 70, "bold"), text="My digital clock", background="white", foreground="black")
title.pack(side="top")

clt = Label(root, font=("arial", 60, "bold"), background=colors[random.randint(0, len(colors)-1)], foreground=colors[random.randint(0, len(colors)-1)])
clt.pack(anchor="center")

def time():
    thetime = strftime("%H:%M:%S %p")
    clt.config(text=thetime)
    clt.config(background=colors[random.randint(0, len(colors)-1)], foreground=colors[random.randint(0, len(colors)-1)])
    clt.after(random.randint(999, 1001), time)
    
time()

root.mainloop()