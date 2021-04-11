from tkinter import *
from functools import partial
import ManHinhThemHangHoa as mhThemHangHoa
import ManHinhThemLoai as mhThemLoai
import common


root = Tk()
root.title("Quản lý Hàng hóa App")
common.setWidgetCenter(root, 450, 300)

# Xu ly menu
xulyThemLoai = partial(mhThemLoai.openThemLoai, root)
xulyThemHangHoa = partial(mhThemHangHoa.openManHinhThemHangHoa,root)

# Menu
menubar = Menu(root)
mnuHeThong = Menu(menubar, tearoff=0)
mnuHeThong.add_command(label="Thêm loại", command=xulyThemLoai)
menubar.add_cascade(label="Quản lý Loại", menu=mnuHeThong)

mnuHangHoa = Menu(menubar, tearoff=0)
mnuHangHoa.add_command(label="Thêm hàng hóa", command=xulyThemHangHoa)
menubar.add_cascade(label="Quản lý Hàng hóa", menu=mnuHangHoa)

root.config(menu=menubar)


root.mainloop()

