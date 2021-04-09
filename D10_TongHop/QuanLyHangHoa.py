from tkinter import *
from tkinter import messagebox
from functools import partial
import dbcommon

db_name="pythonsqlite.db"


# Man hinh them loai
def openThemLoai():
    def xu_ly_them_loai(ten_loai):
        sql = f"SELECT * FROM Loai WHERE TenLoai='{ten_loai}'"
        conn = dbcommon.sql_connection(db_name)
        result = dbcommon.query_data(conn, sql)
        if len(result) > 0:
            messagebox.showwarning(title="Thông báo",
                message=f"Đã có loại {ten_loai}")
        else:
            sqlInsert=f"INSERT INTO Loai(TenLoai) VALUES('{ten_loai}')"
        conn.close()

    mhThemLoai = Toplevel(root)
    mhThemLoai.geometry("250x200")
    mhThemLoai.title("Thêm loại")
    Label(mhThemLoai, text="Tên loại").grid(row=0, column=0)
    tenloai = StringVar()
    Entry(mhThemLoai, textvariable=tenloai).grid(row=0, column=1)

    actionThemLoai = partial(xu_ly_them_loai, tenloai)
    Button(mhThemLoai, text="Thêm loại",
           command=actionThemLoai).grid(row=0, column=2)


root = Tk()
root.title("Quan ly Hang hoa")
# Canh giua man hinh
root_width = 450
root_height = 300
root.geometry(f"{root_width}x{root_height}") # widthxheight
paddingWidth = int((root.winfo_screenwidth() - root_width)/2)
paddingHeight = int((root.winfo_screenheight() - root_height)/2)
root.geometry("+{}+{}".format(paddingWidth, paddingHeight))

# Xu ly menu
xulyThemLoai = partial(openThemLoai)

# Menu
menubar = Menu(root)
mnuHeThong = Menu(menubar, tearoff=0)
mnuHeThong.add_command(label="Them loai", command=xulyThemLoai)
menubar.add_cascade(label="Quan ly Loai", menu=mnuHeThong)

root.config(menu=menubar)


root.mainloop()

