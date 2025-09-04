import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
root.geometry("700x700")
root.title("Calculater")

def calculate():
    try:
        if symbol_entry.get() == "+":
            answer = int(firstnumber_entry.get())+int(secondnumber_entry.get())
            
        elif symbol_entry.get() == "-":
            answer = int(firstnumber_entry.get())-int(secondnumber_entry.get())
        
        elif symbol_entry.get() == "*":
            answer = int(firstnumber_entry.get())*int(secondnumber_entry.get())
            
        elif symbol_entry.get() == "/":
            answer = int(firstnumber_entry.get())/int(secondnumber_entry.get())
            
        elif symbol_entry.get() == "^":
            answer = int(firstnumber_entry.get())**int(secondnumber_entry.get())
            
        answer_label.config(text=answer)
    except:
        answer_label.config(text="DON'T INPUT THINGS THAT YOU CAN'T INPUT")
        tkinter.messagebox.showinfo("Dialouge Box", "DON'T INPUT THINGS THAT YOU CAN'T INPUT goblin 👺👺👺")
        

title_label = tk.Label(root, text="The Calculater")
title_label.place(x=350, y=30)

firstnumber_entry = tk.Entry(root, width=20)
firstnumber_entry.place(x=20, y=70)

symbol_entry = tk.Entry(root, width=20)
symbol_entry.place(x=700//2, y=70)

secondnumber_entry = tk.Entry(root, width=20)
secondnumber_entry.place(x=600, y=70)

equals_button = tk.Button(root, text="‗", command=calculate)
equals_button.place(x=700//2, y=100)

answer_label = tk.Label(root, text="EMPTY")
answer_label.place(x=700//2, y=200)






secondtitle_label = tk.Label(root, text="Transitioning Lengths")
secondtitle_label.place(x=700//2, y=300)

def translate():

        if firstunit_entry.get() == "mm":
            if secondunit_entry.get() == "mm":
                result = int(length_entry.get())
                
            elif secondunit_entry.get() == "cm":
                result = int(length_entry.get())*10
                
            elif secondunit_entry.get() == "dm":
                result = int(length_entry.get())*100
                
            elif secondunit_entry.get() == "m":
                result = int(length_entry.get())*1000
                
            elif secondunit_entry.get() == "km":
                result = int(length_entry.get())*1000000
                
                
        
                
        answer_box.config(text=result)

        print("no")
            
    
            
        
            
        
            

length_entry = tk.Entry(root, width=50)
length_entry.place(x=20, y=400)

firstunit_entry = tk.Entry(root, width = 50)
firstunit_entry.place(x=350, y=420)

secondunit_entry = tk.Entry(root, width = 50)
secondunit_entry.place(x=350, y=380)

button = tk.Button(root, text="OK", command=translate)
button.place(x=350, y=500)

answer_box = tk.Label(root, text="MTEE")
answer_box.place(x=700//2.5, y=480)

root.mainloop()