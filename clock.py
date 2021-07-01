from tkinter import *
from time import strftime
root=Tk()
root.title("Clock")
def time():
    clock=strftime("%H:%M:%s %p")
    lavel.config=(text=clock)
    lavel.after(1000,time)
lavel=Lavel(root,font=("Impact",80,"bold"),bg="white,fg="black")
lavel.pack(anchor="center")
time()
root.mainloop()