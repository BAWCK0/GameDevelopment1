import tkinter as tk
import random
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2

root = tk.Tk()

root.title("Login")

string = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!£$%௹"
print(len(string))

account = None
image = cv2.imread("pikachu.png", 1)
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
                Red_Button.grid(row=1, column=1)
                Green_Button.grid(row=1, column=2)
                Blue_Button.grid(row=1, column=3)
                Normal_Button.grid(row=1, column=4)
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
        Red_Button.grid_forget()
        Green_Button.grid_forget()
        Blue_Button.grid_forget()
        Normal_Button.grid_forget()
        account = None
        messagebox.showinfo("Success", "You are now signed out.")
        
def Password_Maker():
    stringggggggggggggggg = ""
    for i in range(16):
        stringggggggggggggggg += string[random.randint(0, 66)]
    
    Password_Entry.config(text=stringggggggggggggggg)

            

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
Password_Entry = tk.Entry()
Password_Entry.grid(row=1, column=4)
Strong_Password_Button = tk.Button(root, text="Strong Password generator", command=Password_Maker)
Strong_Password_Button.grid(row=2,column=2)

'''Red_Button = tk.Button(root, text="Red", command=cv2.imshow("Blue saturation!", B), bg="red")
Green_Button = tk.Button(root, text="Green", command=cv2.imshow("Goblin saturation!", G), bg="lime")
Blue_Button = tk.Button(root, text="Blue", command=cv2.imshow("Red saturation!", R), bg="blue")
Normal_Button = tk.Button(root, text="Normal", command=cv2.imshow("Original!", image), bg="lightgrey")'''

Red_Button = tk.Button(root, text="Red", bg="red")
Green_Button = tk.Button(root, text="Green", bg="lime")
Blue_Button = tk.Button(root, text="Blue", bg="blue")
Normal_Button = tk.Button(root, text="Normal", bg="lightgrey")
root.mainloop()

