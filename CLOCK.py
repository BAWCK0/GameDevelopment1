from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

def time():
    timestring = strftime("%H:%M:%S %p")
    lbl.config(text=timestring)
    lbl.after(1000, time)
    
lbl = Label(root, font=("wingdings", 40, 'bold'), background="255", foreground="green")
lbl.pack(anchor="center")

time()

root.mainloop()