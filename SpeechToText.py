from tkinter import *
from tkinter.ttk import *
import speech_recognition as sr
from tkinter import messagebox
from tkinter.filedialog import *

WIN = Tk()
WIN.title("Speech to TEXT")
WIN.geometry("800x400")

def Translate():
    r = sr.Recognizer() # initialise Recogniser
    with sr.Microphone() as source:
        audio = r.listen()
        try:
            text = r.recognize_google(audio)
            
        except:
            text = "SPEAK CLEARLER GOBLIN 👺👺👺👺👺👺👺"
            
        Output_Text.delete(1, END)
        Output_Text.insert(END, text)

heading1 = Label(WIN, text="Voice Notepad (for goblins)")
heading1.grid(row=0, column=1, padx=20, pady=20)

Output_Text = Text(WIN, width=40)
Output_Text.grid(row=1, column=1, padx=20, pady=20)

trans_button = Button(WIN, text="Click on me GOBLIN\nTo start recording!", command=Translate)
trans_button.grid(row=1, column=0, padx=20, pady=20)

'''save_button = Button(WIN, text="Save", command=Save, width=20)
save_button.grid(row=1, column=2, padx=20, pady=20, columnspan=3)'''

WIN.mainloop()
