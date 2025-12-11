import tkinter as tk

ROOT = tk.Tk()

QUESTIONS = ["?", "who", "what", "when", "why", "how", "are you"]
EXCLAMATION_STATEMENTS = ["wow", "woah", "ouch", "hm", "!", "👺"]
POSITIVE_STATEMENTS = ["good", "great", "fantastic", ":)"]
NEGATIVE_STATEMENTS = ["bad", "horribe", "garbage", ":(", "sad", "angry", "ugly"]

def CHATBOT_THING():
    message = (Input.get()).lower()
    e = True
    print(message)
    for indicator1 in EXCLAMATION_STATEMENTS:
        if indicator1 in message:
            Output.config(text="Wow!")
            e = False
            
    if e:    
        for indicator2 in NEGATIVE_STATEMENTS:
            if indicator2 in message:
                Output.config(text="That's very bad. HAHA :) 👺👺👺👺")
                e = False
                        
    if e:                    
        for indicator3 in POSITIVE_STATEMENTS:
            if indicator3 in message:
                Output.config(text="That's very good :(")
                e = False
                            
    if e:    
        for indicator4 in QUESTIONS:
            if indicator4 in message:
                Output.config(text="I dunno GOBLIN. 👺👺")
                e = False
            
    
    if e:    
        Output.config(text="I don't understand what you're saying. GOBLIN")
        
    
                    
                
                
        
    
    

Title = tk.Label(ROOT, text="Chatbot for goblins 👺")
Title.grid(column=0, row=0, columnspan=1, padx=5, pady=5)

Output = tk.Label(ROOT, text="")
Output.grid(column=0, row=2, padx=5, pady=5)

Input = tk.Entry(ROOT)
Input.grid(column=0, row=3, columnspan=1, padx=5, pady=5)

OK_Button = tk.Button(ROOT, text="OK", width=7, bg="lime", command=CHATBOT_THING)
OK_Button.grid(column=1, row=3, padx=5, pady=5)

ROOT.mainloop()