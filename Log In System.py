import tkinter as tk
import random
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
from tkinter import filedialog
import cv2
import os

root = tk.Tk()
0
account = None
image1 = cv2.imread(os.path.join("OpenCV", "pikachu.png"), 1)
image2 = cv2.imread(os.path.join("OpenCV", "bee.png"), 1)
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
imagechoice = image1
string = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!£$%"
'''R, G, B = cv2.split(image)'''

def signup():
    taken = False
    with open("Logins.txt", "a") as file:
        with open("Logins.txt", "r") as f:
            lines = f.readlines()
            for linee in lines:
                if Username_Entry.get() == linee.split(":")[0]:
                    taken = True
            if not taken:
                if Password_Entry.get() == "":
                    messagebox.showerror("Important message", "you will get hacked if you don't enter in a passworddd goblin so enter a password")
                    
                else:
                    file.write(f"{Username_Entry.get()}:{Password_Entry.get()}\n")
                    messagebox.showinfo("Success!", "You are now signed up!")
            else:
                messagebox.showerror("Uh oh!", "Username is taken GOBLIN! 👺 HAHAHAHAHAHAHAHAHAHA")

def signin():
    username_right = False
    password_right = False
    with open("Logins.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            username = line.split(":")[0].replace("\n", "")
            password = line.split(":")[1].replace("\n", "")
            if Username_Entry.get() == username:

                username_right = True
                right_username = username
                if Password_Entry.get() == password:
                    password_right = True
        
        if username_right:
            if password_right:
                account = right_username
                Sign_in_Button.grid_forget()
                Sign_up_Button.grid_forget()
                Password_Label.grid_forget()
                Username_Label.grid_forget()
                Password_Entry.grid_forget()
                Username_Entry.grid_forget()
                Strong_Password_Button.grid_forget()
                Image_Choice_Button.grid(row=11, column=1)
                Add_Button.grid(row=1, column=1, rowspan=2)
                Subtract_Button.grid(row=3, column=1, rowspan=2)
                Resize_Button.grid(row=5, column=1, rowspan=2)
                Height_Entry.grid(row=5, column=2)
                Width_Entry.grid(row=6, column=2)
                Erode_Button.grid(row=9, column=1, rowspan=2)
                messagebox.showinfo("Success!", "You are now signed in!")
            
            else:
                if Password_Entry.get() == "":
                    messagebox.showerror("are you dum", "just enter in a password hippo dippo nippo sippo fippo lippo 👁️👄👁️")
                else:
                    messagebox.showerror("haha noob", "password is super wrong 👁️👄👁️")
        
        else:
            if Username_Entry.get() == "":
                messagebox.showerror("...", "you didn't enter a username")
            else:
                messagebox.showerror("Uh oh!", "Username is non existent GOBLIN! 👺 HAHAHAHAHAHAHAHAHAHA")
                
def sign_out():
    global account
    if not account:
        Sign_up_Button.grid(row=0, column=2)
        Sign_in_Button.grid(row=0, column=4)
        Username_Label.grid(row=1, column=1)
        Password_Label.grid(row=1, column=3)
        Password_Entry.grid(row=1, column=4)
        Username_Entry.grid(row=1, column=2)
        Strong_Password_Button.grid(row=2,column=2)
        Image_Choice_Button.grid_forget()
        Add_Button.grid_forget()
        Subtract_Button.grid_forget()
        Resize_Button.grid_forget()
        Erode_Button.grid_forget()
        Height_Entry.grid_forget()
        Width_Entry.grid_forget()
        account = None
        messagebox.showinfo("Success", "You are now signed out.")
        
def Password_Maker():
    stringggggggggggggggg = ""
    for i in range(16):
        stringggggggggggggggg += string[random.randint(0, 65)]
    print(stringggggggggggggggg)
    
    Password_Entry.delete(0, len(Password_Entry.get()))
    Password_Entry.insert(0, stringggggggggggggggg)
    
def switch():
    global imagechoice
    if Image_Choice_Button.cget("text") == "Image1":
        Image_Choice_Button.config(text="Image2")
        imagechoice = image2
    
    else:
        Image_Choice_Button.config(text="Image1")
        imagechoice = image1
        
def add():
    cv2.imshow("Weighted Image", cv2.addWeighted(image1, 0.7, image2, 0.5, 10))
    
def subtract():
    cv2.imshow("Subtracted Image", cv2.subtract(image1, image2))
    
def resize():
    try:
        cv2.imshow("Resized Image", cv2.resize(imagechoice,(int(Height_Entry.get()), int(Width_Entry.get()))))
        
    except:
        messagebox.showerror("Error", "You did something wrong. 👁️👄👁️")
    
def erode():
    cv2.imshow("Eroded Image", cv2.erode(imagechoice, np.ones((6, 6), np.uint8)))

            

Sign_up_Button = tk.Button(root, text="Sign up", command=signup)
Sign_up_Button.grid(row=0, column=2)
Sign_in_Button = tk.Button(root, text="Sign in", command=signin)
Sign_in_Button.grid(row=0, column=4)
Sign_out_Button = tk.Button(root, text="Sign out", command=sign_out, bg="red")
Sign_out_Button.grid(row=0, column=3)

Username_Label = tk.Label(root, text="Username:")
Username_Label.grid(row=1, column=1)
Username_Entry = tk.Entry(root)
Username_Entry.grid(row=1, column=2)
Password_Label = tk.Label(root, text="Password:")
Password_Label.grid(row=1, column=3)
Password_Entry = tk.Entry(root)
Password_Entry.grid(row=1, column=4)
Strong_Password_Button = tk.Button(root, text="Strong Password generator", command=Password_Maker)
Strong_Password_Button.grid(row=2,column=2)

Image_Choice_Button = tk.Button(root, text="Image1", command=switch, bg="lightgrey")
Add_Button = tk.Button(root, text="Add", command=add, bg="lightgrey")
Subtract_Button = tk.Button(root, text="Subtract", command=subtract, bg="lightgrey")
Resize_Button = tk.Button(root, text="Resize", command=resize, bg="lightgrey")
Erode_Button = tk.Button(root, text="Erode", command=erode, bg="lightgrey")
Height_Entry = tk.Entry(root)
Width_Entry = tk.Entry(root)
root.mainloop()
