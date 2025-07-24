from tkinter import *
 
win = Tk()
win.geometry("500x501")

leftbutton = Button(win, text="I burnt your milk.", bd='5.52', background='red', command=win.destroy)
rightbutton = Button(win, text="I'm gonna destroy this window it's full of bad influences like up button", bd='1.33', background='chartreuse', command=win.destroy)
topbutton = Button(win, text="Right button is rude :(", bd='4.06', background='aqua', command=win.destroy)
bottombutton = Button(win, text="what.", bd='19.31', background='blue', command=win.destroy)
# 14:58:19:4:9
leftbutton.pack(side='left')
rightbutton.pack(side='right')
topbutton.pack(side='top')
bottombutton.pack(side='bottom')

win.mainloop()