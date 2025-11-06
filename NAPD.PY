from tkinter import *
from tkinter import filedialog, messagebox

root = Tk()
root.title("Personal Dictionary")

label_date = Label(root, text="Date")
label_date.pack(pady=2, padx=19)

text_date = Text(width=50, height=5)
text_date.pack(pady=2, padx=19)


label_topic = Label(root, text="Topic")
label_topic.pack(pady=2, padx=19)

text_topic = Text(width=50, height=5)
text_topic.pack(pady=2, padx=19)


label_content = Label(root, text="Content")
label_content.pack(pady=2, padx=19)

text_content = Text(width=50, height=5)
text_content.pack(pady=2, padx=19)

def save_file():
    file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("TEXT files", "*.txt"), ("ALL files", "*.*")])
    
    if file:
        content = f"{text_date.get(1.0, END)}\n{text_topic.get(1.0, END)}\n\n{text_content.get(1.0, END)}"
        file.write(content)
        file.close()
        messagebox.showwarning("Sucess", "File Saved :D")
        
def open_file():
    file_path = filedialog.askopenfilename(title="INVADE file", filetypes=[("TEXT files", "*.txt"), ("ALL files", "*.*")])
    
    if file_path:
        try:
            with open(file_path, "r") as file:
                content = file.read()
                text_date.delete("1.0", END)
                text_date.insert(END, content)
                 
        except:
            messagebox.showerror("Could not INVADE the file >:(", "Mission FAILED")
        
save_button = Button(root, text="Unleash", command=save_file)
save_button.pack()

open_button = Button(root, text="INVADE", command=open_file)
open_button.pack()

root.mainloop()