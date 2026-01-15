import tkinter as tk
import random
import cv2

ROOT = tk.Tk()

ROOT.title("Dice")

number = 1

img = "paint.png"

def roll():
    global number
    number = random.randint(1, 5)
    cv2.destroyAllWindows()
    if number == 1:
        cv2.imshow("normal", cv2.imread(img, 1))
    
    elif number == 2:
        cv2.imshow("greyscale", cv2.imread(img, 0))
        
    elif number == 3:
        cv2.imshow("red", cv2.split(cv2.imread(img, 1))[0])
        
    elif number == 4:
        cv2.imshow("blue", cv2.split(cv2.imread(img, 1))[1])
        
    elif number == 5:
        cv2.imshow("green", cv2.split(cv2.imread(img, 1))[2])
    button.config(text=number)
        

button = tk.Button(ROOT, text="Roll", bg="lime", command=roll)
button.pack()

ROOT.mainloop()