import math
import tkinter
import tkinter.messagebox
import random

root = tkinter.Tk()
root.minsize(350, 260)
root.title("Guess the number")

numberofguesses = 0

number = random.randint(0, 50)

label = tkinter.Label(root, text="Welcome to our gam e")
label.pack()

label_name = tkinter.Label(root, text="What is your name?")
label_name.place(x=35, y=90)

label_guesses = tkinter.Label(root, text=f"Guesses: {numberofguesses}")
label_guesses.place(x=35, y=220)

input_name = tkinter.Entry(root, width=20)
input_name.place(x=35, y=110)

def nae():
    name = input_name.get()
    tkinter.messagebox.showinfo("Welcome", f"So, {name}, you must guess the number which is between 0 and 50. If you don't, you DIE")

def nue():
    global numberofguesses
    numberofguesses += 1
    label_guesses.config(text=f"Guesses: {numberofguesses}")
    
    guess = int(number_entry.get())
    if guess > number:
        tkinter.messagebox.showinfo("High", "haha GOBLIN 👺 your guess it too HIGH.")
        
    elif guess < number:
        tkinter.messagebox.showinfo("Low", "hehe GOBLIN 👺 your guess it too LOW.")
        
    elif guess == number:
        tkinter.messagebox.showinfo("You win :(", "GOBLIN 👺 your guess is CORRECT.")
        

confirm_name = tkinter.Button(root, text="OK", bg="green", command=nae)
confirm_name.place(x=170, y=110, height=20)

guess_label = tkinter.Label(root, text="Guess the number")
guess_label.place(x=35, y=150)

number_entry = tkinter.Entry(root, width=20)
number_entry.place(x=35, y=180)

confirm_number = tkinter.Button(root, text="GUESS (goblin)", bg="red", command=nue)
confirm_number.place(x=170, y=180, height=20)

root.mainloop()