from tkinter import *
from tkinter.ttk import *

rooty_boi = Tk()
rooty_boi.title("dinosaurs roaming paris")

title_label = Label(rooty_boi, text="teehee")
title_label.grid(row=0, column=0, columnspan=3, pady=25)

caption = Label(rooty_boi, text="Number and range :3 :")
caption.grid(row=1, column=0, columnspan=3, padx=11)

theTum = IntVar()

numbers = Combobox(rooty_boi, textvariable=theTum, width=5)
numbers.grid(row=1, column=3, columnspan=2)

numbers["values"] = tuple(range(30))

endVal = IntVar()
r10 = Radiobutton(rooty_boi, text="10", variable=endVal, value=10)
r10.grid(row=1, column=6, columnspan=1)

r20 = Radiobutton(rooty_boi, text="20", variable=endVal, value=20)
r20.grid(row=2, column=6, columnspan=1)

r30 = Radiobutton(rooty_boi, text="30", variable=endVal, value=30)
r30.grid(row=3, column=6, columnspan=1)

endVal.set(10)

def generateMulDinos():
    tables = ""
    for oi in range(endVal.get() + 1):
        tables += str(endVal.get()) + "x" + str(oi) + "=" + str(endVal.get()*oi) + "\n"
    table.config(text=tables)
    
generatebutton = Button(rooty_boi, text="Summon", command=generateMulDinos)
generatebutton.grid(row=4, column=1)

table = Label(rooty_boi, anchor="center")
table.grid(row=5, column=1, pady=25)

    

rooty_boi.mainloop()