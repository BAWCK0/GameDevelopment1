from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.geometry("300x250")
root.title("Stap Wotch")

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

def hi():
    try:
        preferedtimee = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
        timee = 0
        
    except:
        messagebox.showerror("INVALID GOBLIN", "SSSSONLY INTEGERS creature")
        return

    while timee <= preferedtimee:
        mins, secs = divmod(timee, 60)
        hours, mins = divmod(mins, 60)
        
        hour.set(f"{hours}")
        minute.set(f"{mins}")
        second.set(f"{secs}")
        
        root.update()
        time.sleep(1)

        if timee >= preferedtimee:
            messagebox.showinfo("Hi", "Times up creature goblin")
            return
            
        timee += 1
        print(timee)
        
HourEntry = Entry(root, width=3, font=("Arial", 18, "bold"), textvariable=hour)
HourEntry.pack(side="left", padx=40)

MinuteEntry = Entry(root, width=3, font=("Arial", 18, "bold"), textvariable=minute)
MinuteEntry.pack(side="left")

SecondEntry = Entry(root, width=3, font=("Arial", 18, "bold"), textvariable=second)
SecondEntry.pack(side="left", padx=40)

btn = Button(root, text="Start", bd=4, command=hi)
btn.place(x=140, y= 210)

root.mainloop()