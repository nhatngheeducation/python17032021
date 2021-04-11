from tkinter import *
from tkinter import ttk, messagebox
import dbcommon
import common
from functools import partial
db_name="pythonsqlite.db"


def openThemLoai(root):
    mhThemLoai = Toplevel(root)

    def xu_ly_them_loai(ten_loai):
        try:
            sql = f"SELECT * FROM Loai WHERE TenLoai='{ten_loai.get()}'"
            conn = dbcommon.sql_connection(db_name)
            result = dbcommon.query_data(conn, sql)
            print(result)
            if len(result) > 0:
                messagebox.showwarning(title="Thông báo",
                    message=f"Đã có loại {ten_loai.get()}")
            else:
                sqlInsert=f"INSERT INTO Loai(TenLoai) VALUES('{ten_loai.get()}')"
                idloai = dbcommon.insert_and_get_inserted_id(conn, sqlInsert)
                message=f"Đã thêm loại ({idloai}, {ten_loai.get()})."\
                    + "\n Tiếp tục không?"
                traloi=messagebox.askyesno("Hỏi", message)
                if traloi == True:
                    ten_loai.set("")
                else:
                    mhThemLoai.destroy()
        except Exception as e:
            print(e)
        finally:
            if conn:
                conn.close()


    common.setWidgetCenter(mhThemLoai, 250, 80)
    mhThemLoai.title("Thêm loại")
    Label(mhThemLoai, text="Tên loại").grid(row=0, column=0)
    tenloai = StringVar()
    Entry(mhThemLoai, textvariable=tenloai).grid(row=0, column=1)

    actionThemLoai = partial(xu_ly_them_loai, tenloai)
    Button(mhThemLoai, text="Thêm loại",
           command=actionThemLoai).grid(row=0, column=2)