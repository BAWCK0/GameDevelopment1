from tkinter import *
import random
import tkinter.font as font

you_score = 0
computer_score = 0

window = Tk()

window.geometry("800x500")
window.title("Stone Shears Sheet")
window.config(bg="white")

title_font = font.Font(family="Arial", size=20, weight="bold")
button_font = font.Font(family="Arial", size=14)
app_font = font.Font(family="Arial", size=12)

title = Label(window, text="Stone, Shears, Sheet", font=title_font, bg="lightgrey", fg="black")
title.pack(pady=12)

computer_choices = ["Stone", "Shear", "Sheet"]

def rock():
    global computer_score, you_score
    computer_choice = computer_choices[random.randint(0, 2)]
    you_selected.config(text="You Selected: Stone")
    computer_selected.config(text=f"computer selected: {computer_choice}")
    
    if computer_choice == "Stone":
        result.config(text="TIE")
        
    elif computer_choice == "Sheet":
        result.config(text="Computer wins hehe")
        computer_score += 1
        computer_score_label.config(text=f"Computer score: {computer_score}")
        
    elif computer_choice == "Shear":
        result.config(text="You win")
        you_score += 1
        you_score_label.config(text=f"You score: {you_score}")
         

def paper():
    global computer_score, you_score
    computer_choice = computer_choices[random.randint(0, 2)]
    you_selected.config(text="You Selected: Sheet")
    computer_selected.config(text=f"computer selected: {computer_choice}")
    
    if computer_choice == "Sheet":
        result.config(text="TIE")
        
    elif computer_choice == "Shear":
        result.config(text="Computer wins hehe")
        computer_score += 1
        computer_score_label.config(text=f"Computer score: {computer_score}")
        
    elif computer_choice == "Stone":
        result.config(text="You win")
        you_score += 1
        you_score_label.config(text=f"You score: {you_score}")
        


def scissor():
    global computer_score, you_score
    computer_choice = computer_choices[random.randint(0, 2)]
    you_selected.config(text="You Selected: Shears")
    computer_selected.config(text=f"computer selected: {computer_choice}")
    
    if computer_choice == "Shear":
        result.config(text="TIE")
        
    elif computer_choice == "Stone":
        result.config(text="Computer wins hehe")
        computer_score += 1
        computer_score_label.config(text=f"Computer score: {computer_score}")
        
    elif computer_choice == "Sheet":
        result.config(text="You win")
        you_score += 1
        you_score_label.config(text=f"You score: {you_score}")
        


you_selected = Label(window, text="You selected: ", font=app_font, bg="lightgrey", fg="black")
you_selected.pack()


computer_selected = Label(window, text="Compter selected: ", font=app_font, bg="lightgrey", fg="black")
computer_selected.pack(pady=10)


you_score_label = Label(window, text=f"Your score: {you_score}", font=app_font, bg="lightgrey", fg="black")
you_score_label.pack(pady=10)


computer_score_label = Label(window, text=f"Computer score: {computer_score}", font=app_font, bg="lightgrey", fg="black")
computer_score_label.pack()

result = Label(window, text="", font=app_font, bg="lightgrey", fg="black")
result.pack(pady=10)


rock_button = Button(window, text="Stone", font=button_font, bg="lightgrey", fg="black", command=rock)
rock_button.pack(side="left", padx=150)


paper_button = Button(window, text="Sheet", font=button_font, bg="lightgrey", fg="black", command=paper)
paper_button.pack(side="left", padx=0)


scissor_button = Button(window, text="Shears", font=button_font, bg="lightgrey", fg="black", command=scissor)
scissor_button.pack(side="left", padx=150)


window.mainloop()