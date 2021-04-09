from tkinter import *
from functools import partial

root = Tk()
root.title("Quan ly Loai")
root.geometry("350x300")
Label(root,text="Ten loai").grid(row=0, column=0)
tenloai = StringVar()
Entry(root, textvariable=tenloai).grid(row=0, column=1)
Button(root, text="Them loai").grid(row=0,column=2)


root.mainloop()

