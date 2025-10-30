'''di = {
    "dino":"yes",
    "secondary":"primary"
}

print(di["dino"])
print(di.keys())
print(di.values())
print(di.items())'''

import tkinter as tk

root = tk.Tk()
root.title("Thingy")

people = {}

yas = ""

def add():
    people[Name_Entry.get()] = (Address_Entry.get(), Pn_Entry.get(), Email_Entry.get())
    for names in people.keys(): 
        yas = names + "\n"
        if yas == "\n":
            yas = ""
    Name_List.config(text=Name_List.cget("text")+yas)
    
def show():
    yes = ""
    for values in people.values():
        yes += values[0] + " " + values[1] + " " + values[2] + "\n"
        
    Values_list.config(text=yes)
    
    

Name_Label = tk.Label(root, text="Name:")
Name_Label.grid(row=1, column=8)

Name_Entry = tk.Entry(root, width=10)
Name_Entry.grid(row=1, column=9)

#ADDRESS

Address_Label = tk.Label(root, text="Address:")
Address_Label.grid(row=2, column=8)

Address_Entry = tk.Entry(root, width=10)
Address_Entry.grid(row=2, column=9)

Pn_Label = tk.Label(root, text="Phone Number:")
Pn_Label.grid(row=3, column=8)

Pn_Entry = tk.Entry(root, width=10)
Pn_Entry.grid(row=3, column=9)

Email_Label = tk.Label(root, text="Email:")
Email_Label.grid(row=4, column=8)

Email_Entry = tk.Entry(root, width=10)
Email_Entry.grid(row=4, column=9)

#Buttonsss

Add_button = tk.Button(root, text="Add", width=15, command=add)
Add_button.grid(column=1, row=1, padx=10, pady=10)

Show_button = tk.Button(root, text="Show", width=15, command=show)
Show_button.grid(column=1, row=2, padx=10, pady=10)


Name_List = tk.Label(root, text="")
Name_List.grid(column=1, row=3, pady=10, padx=10)

Values_list = tk.Label(root, text="")
Values_list.grid(column=1, row=4, padx=10, pady=10)



root.mainloop()

