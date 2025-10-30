from tkinter import *
from tkinter import filedialog, messagebox

root = Tk()
root.title("File Invader 3000")

text_area = Text(width=50, height=15)
text_area.pack(pady=19, padx=19)

def save_file():
    file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("TEXT files", "*.txt"), ("ALL files", "*.*")])
    
    if file:
        content = text_area.get("1.0", END)
        file.write(content)
        file.close()
        messagebox.showwarning("Sucess", "File Saved :D")
        
def open_file():
    file_path = filedialog.askopenfilename(title="INVADE file", filetypes=[("TEXT files", "*.txt"), ("ALL files", "*.*")])
    
    if file_path:
        try:
            with open(file_path, "r") as file:
                content = file.read()
                text_area.delete("1.0", END)
                text_area.insert(END, content)
                 
        except:
            messagebox.showerror("Could not INVADE the file >:(", "Mission FAILED")
        
save_button = Button(root, text="Unleash", command=save_file)
save_button.pack()

open_button = Button(root, text="INVADE", command=open_file)
open_button.pack()

root.mainloop()