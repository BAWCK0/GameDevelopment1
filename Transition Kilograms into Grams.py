import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title('Transitions INC')
root.geometry('600x600')
root.config(bg='mediumslateblue')

def transition():
    try:
        kg = float(entry_kilo.get())
        g = kg*1000
        result.config(text=f"{g} Grams.")
    except:
        result.config(text="DO NOT INPUT STRING")

n_font = font.Font(family="Arial", size=20)
italics_font = font.Font(family="Arial", size=20, slant="italic")
bold_font = font.Font(family="Arial", size=20, weight="bold")
ib_font = font.Font(family="Arial", size=20, weight="bold", slant="italic")

title = tk.Label(root, text="Transition Kilograms to Grams.", font=ib_font, bg="white", fg="black")
title.pack(pady=10)

input_frame = tk.Frame(root, bg="red")
input_frame.pack(pady=30)

kilo_label = tk.Label(input_frame, text="Populate Kilogram value.", font=italics_font, fg="black", bg="red")
kilo_label.pack(side="bottom")

entry_kilo = tk.Entry(input_frame, font=n_font, width=20)
entry_kilo.pack()

transition_button = tk.Button(root, text="Transition", font=italics_font, fg="lime", bg="white", command=transition)
transition_button.pack(pady=100)

result = tk.Label(root, text=" ", font=n_font, fg="black", bg="white")
result.pack()

root.mainloop()