import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("Login")

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
                if Password_Entry.get() == password:
                    password_right = True
        
        if username_right:
            if password_right:
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

                    
            
        

Sign_up_Button = tk.Button(root, text="Sign up", command=signup)
Sign_up_Button.grid(row=0, column=2)
Sign_in_Button = tk.Button(root, text="Sign in", command=signin)
Sign_in_Button.grid(row=0, column=3)

Username_Label = tk.Label(root, text="Username:")
Username_Label.grid(row=1, column=1)
Username_Entry = tk.Entry(root)
Username_Entry.grid(row=1, column=2)
Password_Label = tk.Label(root, text="Password:")
Password_Label.grid(row=1, column=3)
Password_Entry = tk.Entry()
Password_Entry.grid(row=1, column=4)

root.mainloop()

