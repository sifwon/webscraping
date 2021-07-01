from tkinter import *
from PIL import ImageTk,Image
root =Tk()
root.title("photo viewer")

emiria = ImageTk.PhotoImage(Image.open("img/emiria.jpg")) my_label = Label(image=emiria)
my_label.grid(raw=0,column=0,columnspan=3)
button_exit=Button(root,text="Quit",command=root.quit)
button_exit.grid(raw=1,column=1)
root.mainloop()