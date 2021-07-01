from tkinter import *
import webbrowser

def callback(url):
    webbrowser.open_new(url)

win = Tk()
link = Label(win,text="rezerosite",width=60,height=40,cursor="hand1")
link.pack()
link.bind("<Button-1>",lambda e:callback("https:gogoanime.movie/"))
win.mainloop()