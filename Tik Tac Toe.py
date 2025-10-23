import tkinter as tk

win = tk.Tk()
win.title("TI TA TO")

title = tk.Label(win, text="TI TA TO 👽")
title.grid(row=5, column=1)

turn_bar =  tk.Label(win, text="(X) Player 1s turn")
turn_bar.grid(row = 5, column=8)

amount_taken = 0

turn = "P1"

def winn():
    top_left.config(command=taken)
    top_middle.config(command=taken)
    top_right.config(command=taken)
    
    middle_left.config(command=taken)
    middle_middle.config(command=taken)
    middle_right.config(command=taken)
    
    bottom_left.config(command=taken)
    bottom_middle.config(command=taken)
    bottom_right.config(command=taken)
    
    if turn == "P2":
        turn_bar.config(text=f"X WINSSSSSSSSSSSSSSS haha other player you are the ultimate GOBLINO 👺👺👺")
    
    else:
        turn_bar.config(text=f"O WINSSSSSSSSSSSSSSS haha other player you are the ultimate GOBLIN 👺👺👺")

def taken():
    print("TAKEN HEHEHAHA")
    
def check_for_win():
    global amount_taken
    amount_taken += 1
    if amount_taken >= 9:
        winn()
        turn_bar.config(text="TIE... you are BOTH GOBLINS 👺👺👺👺👺👺👺👺👺👺👺👺")
        
    for xo in ["X", "O"]:
        if top_left.cget("text") == xo:
            if top_middle.cget("text") == xo:
                if top_right.cget("text") == xo:
                    winn()
                    
        if middle_left.cget("text") == xo:
            if middle_middle.cget("text") == xo:
                if middle_right.cget("text") == xo:
                    winn()
                    
        if bottom_left.cget("text") == xo:
            if bottom_middle.cget("text") == xo:
                if bottom_right.cget("text") == xo:
                    winn()
                    
                    
                    
                    
        if top_left.cget("text") == xo:
            if top_middle.cget("text") == xo:
                if top_right.cget("text") == xo:
                    winn()
                    
        if middle_left.cget("text") == xo:
            if middle_middle.cget("text") == xo:
                if middle_right.cget("text") == xo:
                    winn()
                    
        if bottom_left.cget("text") == xo:
            if bottom_middle.cget("text") == xo:
                if bottom_right.cget("text") == xo:
                    winn()
                    
                    
                    
        if top_right.cget("text") == xo:
            if top_middle.cget("text") == xo:
                if top_left.cget("text") == xo:
                    winn()
                    
        if middle_right.cget("text") == xo:
            if middle_middle.cget("text") == xo:
                if middle_left.cget("text") == xo:
                    winn()
                    
        if bottom_right.cget("text") == xo:
            if bottom_middle.cget("text") == xo:
                if bottom_left.cget("text") == xo:
                    winn()
                    
        # diagonals
                    
        if top_left.cget("text") == xo:
            if middle_middle.cget("text") == xo:
                if bottom_right.cget("text") == xo:
                    winn()
                    
        if top_right.cget("text") == xo:
            if middle_middle.cget("text") == xo:
                if bottom_left.cget("text") == xo:
                    winn()          
    

# top leftt


def tl():
    global turn
    if turn == "P1":
        top_left.config(text="X", command=taken)
        turn = "P2"
        turn_bar.config(text="(O) Player 2s turn")
        
    else:
        top_left.config(text="O", command=taken)
        turn = "P1"
        turn_bar.config(text="(X) Player 1s turn")
        
    check_for_win()

top_left = tk.Button(win, text=" ", width=4, height=2, command=tl)
top_left.grid(row = 3, column=3, padx=1, pady=1)

def tm():
    global turn
    if turn == "P1":
        top_middle.config(text="X", command=taken)
        turn = "P2"
        turn_bar.config(text="(O) Player 2s turn")
        
    else:
        top_middle.config(text="O", command=taken)
        turn = "P1"
        turn_bar.config(text="(X) Player 1s turn")
        
    check_for_win()

top_middle = tk.Button(win, text=" ", width=4, height=2, command=tm)
top_middle.grid(row = 5, column=3, padx=1, pady=1)

def tr():
    global turn
    if turn == "P1":
        top_right.config(text="X", command=taken)
        turn = "P2"
        turn_bar.config(text="(O) Player 2s turn")
        
    else:
        top_right.config(text="O", command=taken)
        turn = "P1"
        turn_bar.config(text="(X) Player 1s turn")
        
    check_for_win()

top_right = tk.Button(win, text=" ", width=4, height=2, command=tr)
top_right.grid(row = 7, column=3, padx=1, pady=1)

# MIDDLE BELOW GOBLIN

def ml():
    global turn
    if turn == "P1":
        middle_left.config(text="X", command=taken)
        turn = "P2"
        turn_bar.config(text="(O) Player 2s turn")
        
    else:
        middle_left.config(text="O", command=taken)
        turn = "P1"
        turn_bar.config(text="(X) Player 1s turn")
        
    check_for_win()

middle_left = tk.Button(win, text=" ", width=4, height=2, command=ml)
middle_left.grid(row = 3, column=5, padx=1, pady=1)

def mm():
    global turn
    if turn == "P1":
        middle_middle.config(text="X", command=taken)
        turn = "P2"
        turn_bar.config(text="(O) Player 2s turn")
        
    else:
        middle_middle.config(text="O", command=taken)
        turn = "P1"
        turn_bar.config(text="(X) Player 1s turn")
        
    check_for_win()

middle_middle = tk.Button(win, text=" ", width=4, height=2, command=mm)
middle_middle.grid(row = 5, column=5, padx=1, pady=1)

def mr():
    global turn
    if turn == "P1":
        middle_right.config(text="X", command=taken)
        turn = "P2"
        turn_bar.config(text="(O) Player 2s turn")
        
    else:
        middle_right.config(text="O", command=taken)
        turn = "P1"
        turn_bar.config(text="(X) Player 1s turn")
        
    check_for_win()

middle_right = tk.Button(win, text=" ", width=4, height=2, command=mr)
middle_right.grid(row = 7, column=5, padx=1, pady=1)

# BOTTOM BELOW GOBLIN

def bl():
    global turn
    if turn == "P1":
        bottom_left.config(text="X", command=taken)
        turn = "P2"
        turn_bar.config(text="(O) Player 2s turn")
        
    else:
        bottom_left.config(text="O", command=taken)
        turn = "P1"
        turn_bar.config(text="(X) Player 1s turn")
        
    check_for_win()

bottom_left = tk.Button(win, text=" ", width=4, height=2, command=bl)
bottom_left.grid(row = 3, column=7, padx=1, pady=1)

def bm():
    global turn
    if turn == "P1":
        bottom_middle.config(text="X", command=taken)
        turn = "P2"
        turn_bar.config(text="(O) Player 2s turn")
        
    else:
        bottom_middle.config(text="O", command=taken)
        turn = "P1"
        turn_bar.config(text="(X) Player 1s turn")
        
    check_for_win()
    

bottom_middle = tk.Button(win, text=" ", width=4, height=2, command=bm)
bottom_middle.grid(row = 5, column=7, padx=1, pady=1)

def br():
    global turn
    if turn == "P1":
        bottom_right.config(text="X", command=taken)
        turn = "P2"
        turn_bar.config(text="(O) Player 2s turn")
        
    else:
        bottom_right.config(text="O", command=taken)
        turn = "P1"
        turn_bar.config(text="(X) Player 1s turn")
        
    check_for_win()

bottom_right = tk.Button(win, text=" ", width=4, height=2, command=br)
bottom_right.grid(row = 7, column=7, padx=1, pady=1)

win.mainloop()