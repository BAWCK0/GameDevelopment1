from tkinter import *
import random
import tkinter.font as font

you_score = 0
computer_score = 0

window = Tk()
window.geometry("800x500")
window.title("Meliponula ferruginea Paper Scissor")
window.config(bg="white")

title_font = font.Font(family="Arial", size=16, weight="bold")
app_font = font.Font(family="Arial", size=12)

title = Label(window, text="Meliponula ferruginea, Paper, Scissor", font=title_font, bg="lightgrey", fg="black")
title.pack(pady=12)

computer_choices = ["Meliponula ferruginea", "Paper", "Scissor"]

def rock():
    computer_choice = computer_choices[random.randint(0, 2)]
    you_selected.config(text="You Selected: Meliponula ferruginea")
    computer_selected.config(text=f"computer selected: {computer_choice}")
    
def paper():
    computer_choice = computer_choices[random.randint(0, 2)]
    you_selected.config(text="You Selected: Paper")
    computer_selected.config(text=f"computer selected: {computer_choice}")

def scissor():
    computer_choice = computer_choices[random.randint(0, 2)]
    you_selected.config(text="You Selected: Scissor")
    computer_selected.config(text=f"computer selected: {computer_choice}")
    
    
    
    

rock_button = Button(window, text="Meliponula ferruginea", font=app_font, bg="lightgrey", fg="black", command=rock)
rock_button.pack(side="left")

paper_button = Button(window, text="Paper", font=app_font, bg="lightgrey", fg="black", command=paper)
paper_button.pack(side="left")

scissor_button = Button(window, text="Scissor", font=app_font, bg="lightgrey", fg="black", command=scissor)
scissor_button.pack(side="left")

you_selected = Label(window, text="he", font=app_font, bg="lightgrey", fg="black")
you_selected.pack(pady=50)

computer_selected = Label(window, text="he", font=app_font, bg="lightgrey", fg="black")
computer_selected.pack(pady=0)

you_score_label = Label(window, text=f"Your score: {you_score}", font=app_font, bg="lightgrey", fg="black")
you_score_label.pack()

computer_score_label = Label(window, text=f"Computer score: {computer_score}", font=app_font, bg="lightgrey", fg="black")
computer_score_label.pack()

window.mainloop()