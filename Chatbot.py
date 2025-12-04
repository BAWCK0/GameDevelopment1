import tkinter as tk

ROOT = tk.Tk()

QUESTIONS = ["?", "who", "what", "when", "why", "how"]
EXCLAMATION_STATEMENTS = ["wow", "woah", "ouch", "hm", "!", "👺"]
POSITIVE_STATEMENTS = ["good", "great", "fantastic", ":)"]
NEGATIVE_STATEMENTS = ["bad", "horribe", "garbage", ":(", "sad"]

def CHATBOT_THING():
    question_indicators = 0
    exclamation_indicators = 0
    positive_indicators = 0
    negative_indicators = 0
    message = Input.get()
    
    for indicator in QUESTIONS:
        if indicator in message:
            question_indicators += 1
            
    for indicator in EXCLAMATION_STATEMENTS:
        if indicator in message:
            exclamation_indicators += 1
            
    for indicator in POSITIVE_STATEMENTS:
        if indicator in message:
            if "not" in message:
                negative_indicators += 1
                
            else:
                positive_indicators += 1
            
    for indicator in POSITIVE_STATEMENTS:
        if indicator in message:
            if "not" in message:
                positive_indicators_indicators += 1
                
            else:
                negative_indicators += 1
                
    if question_indicators > 0:
        Output.config(text="I dunno.")
        
    else:
        if positive_indicators > negative_indicators:
            if exclamation_indicators > 1:
                Output.config(text="That's very goodddd :D")
                
            else:
                Output.config(text="That's good")
            
        elif negative_indicators == positive_indicators:
            
            
        else:
            Output.config(text="Haha 👺 :) :) :)")
        
    
    

Title = tk.Label(ROOT, text="Chatbot for goblins 👺")
Title.grid(column=0, row=0, columnspan=1, padx=5, pady=5)

Output = tk.Label(ROOT, text="")
Output.grid(column=0, row=2, padx=5, pady=5)

Input = tk.Entry(ROOT)
Input.grid(column=0, row=3, columnspan=1, padx=5, pady=5, bg="lime")

OK_Button = tk.Button(ROOT, text="OK", width=7, command=CHATBOT_THING)
OK_Button.grid(column=1, row=3, padx=5, pady=5)

ROOT.mainloop()