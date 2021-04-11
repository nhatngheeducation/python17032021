from tkinter import *
from tkinter import ttk
import dbcommon
import common
from functools import partial
db_name="pythonsqlite.db"


def openManHinhThemHangHoa(mainScreen):
    def ham_xu_ly_them_hang_hoa(cboLoai):
        print(type(cboLoai))
        print("Loai dang chon: ", cboLoai.get())

    mhThemHangHoa = Toplevel(mainScreen)
    common.setWidgetCenter(mhThemHangHoa, 350, 300)

    mhThemHangHoa.title("Thêm hàng hóa")

    Label(mhThemHangHoa, text="Mã hàng hóa").grid(row=0, column=0)
    mahh = StringVar()
    Entry(mhThemHangHoa, textvariable=mahh).grid(row=0, column=1)

    Label(mhThemHangHoa, text="Tên hàng hóa").grid(row=1, column=0)
    tenhh = StringVar()
    Entry(mhThemHangHoa, textvariable=tenhh).grid(row=1, column=1)

    Label(mhThemHangHoa, text="Mô tả").grid(row=2, column=0)
    mota = StringVar()
    Entry(mhThemHangHoa, textvariable=mota).grid(row=2, column=1)
    # Text(mhThemHangHoa, height=5, textva =mota).grid(row=2, column=1)

    Label(mhThemHangHoa, text="Đơn giá").grid(row=3, column=0)
    dongia = IntVar()
    Entry(mhThemHangHoa, textvariable=dongia).grid(row=3, column=1)

    Label(mhThemHangHoa, text="SKU").grid(row=4, column=0)
    sku = StringVar()
    Entry(mhThemHangHoa, textvariable=sku).grid(row=4, column=1)

    # ComboBox Thành phố
    maloai = StringVar
    dsLoai = []
    sql = f"SELECT * FROM Loai ORDER BY TenLoai"
    conn = dbcommon.sql_connection(db_name)
    result = dbcommon.query_data(conn, sql)
    conn.close()
    for loai in result:
        dsLoai.append((loai[0], loai[1]))
    Label(mhThemHangHoa, text="Loại").grid(row=5, column=0)
    cboLoai = ttk.Combobox(mhThemHangHoa,
                               values=dsLoai).grid(row=5, column=1)
    processInsertpro = partial(ham_xu_ly_them_hang_hoa, cboLoai)


    Button(mhThemHangHoa, text="Thêm hàng hóa",
           command=processInsertpro).grid(row=6, column=1)

    mhThemHangHoa.mainloop()