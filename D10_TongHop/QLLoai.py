from tkinter import *
from functools import partial


def openThemLoai():
    mhThemLoai = Toplevel(root)
    mhThemLoai.title("Them loai")
    Label(mhThemLoai, text="Ten loai").grid(row=0, column=0)
    tenloai = StringVar()
    Entry(mhThemLoai, textvariable=tenloai).grid(row=0, column=1)
    Button(mhThemLoai, text="Them loai").grid(row=0, column=2)


root = Tk()
root.title("Quan ly Hang hoa")
root.geometry("350x300")

# Xu ly menu
xulyThemLoai = partial(openThemLoai)

# Menu
menubar = Menu(root)
mnuHeThong = Menu(menubar, tearoff=0)
mnuHeThong.add_command(label="Them loai", command=xulyThemLoai)
menubar.add_cascade(label="Quan ly Loai", menu=mnuHeThong)

root.config(menu=menubar)


root.mainloop()

