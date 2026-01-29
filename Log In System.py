import tkinter as tk

root = tk.Tk()

root.title("Login")

state = "up"

def signup():
    state = "up"
    
def signin():
    state = "in"

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

