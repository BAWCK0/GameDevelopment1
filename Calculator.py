from tkinter import *

root = Tk()
root.title("CALCULATOR")

equation = ""

title = Label(root, text="CALCULATOR 👺")
title.grid(row=1, column=2, padx=2, pady=1)

equation_box = Label(root, text="")
equation_box.grid(row=2, column=2, padx=2, pady=2)

result_box = Label(root, text="")
result_box.grid(column=2, row=3, padx=2, pady=2)

def one():
    global equation
    equation += "1"
    equation_box.config(text=f"{equation}")
    
def two():
    global equation
    equation += "2"
    equation_box.config(text=f"{equation}")
    
def three():
    global equation
    equation += "3"
    equation_box.config(text=f"{equation}")
    
def four():
    global equation
    equation += "4"
    equation_box.config(text=f"{equation}")
    
def five():
    global equation
    equation += "5"
    equation_box.config(text=f"{equation}")
    
def six():
    global equation
    equation += "6"
    equation_box.config(text=f"{equation}")
    
def seven():
    global equation
    equation += "7"
    equation_box.config(text=f"{equation}")
    
def eight():
    global equation
    equation += "8"
    equation_box.config(text=f"{equation}")
    
def nine():
    global equation
    equation += "9"
    equation_box.config(text=f"{equation}")
    
def zero():
    global equation
    equation += "0"
    equation_box.config(text=equation)

def plus():
    global equation
    equation += "+"
    equation_box.config(text=equation)
    
def minus():
    global equation
    equation += "-"
    equation_box.config(text=equation)
    
def minus():
    global equation
    equation += "-"
    equation_box.config(text=equation)
    
def multiply():
    global equation
    equation += "*"
    equation_box.config(text=equation)
    
def divide():
    global equation
    equation += "/"
    equation_box.config(text=equation)
    
def clear():
    global equation
    result_box.config(text="")
    equation = ""
    equation_box.config(text=equation)
    
def back():
    global equation
    equation = equation[0:len(equation)-1]
    equation_box.config(text=equation)

def equals():
    global equation
    result_box.config(text=int(eval(equation))) # I wanna test eval more :D

onebutton = Button(root, text="1", width=12, height=3, command=one)
onebutton.grid(row=4, column=1)

twobutton = Button(root, text="2", width=12, height=3, command=two)
twobutton.grid(row=4, column=2)

threebutton = Button(root, text="3", width=12, height=3, command=three)
threebutton.grid(row=4, column=3)

fourbutton = Button(root, text="4", width=12, height=3, command=four)
fourbutton.grid(row=5, column=1)

fivebutton = Button(root, text="5", width=12, height=3, command=five)
fivebutton.grid(row=5, column=2, pady=2)

sixbutton = Button(root, text="6",  width=12, height=3, command=six)
sixbutton.grid(row=5, column=3)

sevenbutton = Button(root, text="7", width=12, height=3, command=seven)
sevenbutton.grid(row=6, column=1)

eightbutton = Button(root, text="8", width=12, height=3, command=eight)
eightbutton.grid(row=6, column=2)

ninebutton = Button(root, text="9",  width=12, height=3, command=nine)
ninebutton.grid(row=6, column=3)

zerobutton = Button(root, text="0",  width=12, height=3, command=zero)
zerobutton.grid(row=7, column=2)

plusbutton = Button(root, text="+", width=12, height=3, command=plus)
plusbutton.grid(row=6, column=4)

minusbutton = Button(root, text="-", width=12, height=3, command=minus)
minusbutton.grid(row=5, column=4)

timesbutton = Button(root, text="x", width=12, height=3, command=multiply)
timesbutton.grid(row=7, column=4)

dividebutton = Button(root, text="/", width=12, height=3, command=divide)
dividebutton.grid(row=8, column=4)

equalsbutton = Button(root, text="=", width=12, height=3, command=equals)
equalsbutton.grid(row=9, column=4, padx=2, pady=2)

backspacebutton = Button(root, text="<--",  width=12, height=3, command=back)
backspacebutton.grid(row=7, column=3)

clearbuttonbutton = Button(root, text="CLEAR", width=12, height=3, command=clear)
clearbuttonbutton.grid(row=7, column=1)



root.mainloop()
