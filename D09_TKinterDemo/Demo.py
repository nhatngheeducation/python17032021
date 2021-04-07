# https://tkdocs.com/tutorial/
from tkinter import *
from functools import partial


def check_login(username, password):
    print("Username: ", username.get())
    print("password: ", password.get())


def thay_doi_gioi_tinh(gioitinh, textfield):
    print("Gioi tinh dang chon: ", gioitinh.get())
    textfield.set("Giới tính: " + gioitinh.get())


root = Tk()
root.title("Demo Login form")
root.geometry("350x300")
lblUser = Label(root,text="User Name").grid(row=0, column=0)
lblPass = Label(root,text="Password").grid(row=1, column=0)
username = StringVar()
txtUser = Entry(root, textvariable=username).grid(row=0, column=1)
password = StringVar()
txtPass = Entry(root, textvariable=password).grid(row=1, column=1)

# from functools import partial
xulylogin = partial(check_login, username, password)

loginButton = Button(root, text="Login",
    command=xulylogin).grid(row=3,column=1)

gioitinh = StringVar()
xu_ly_chon_gt = partial(thay_doi_gioi_tinh,
                        gioitinh, username)
chkGioiTinh = Checkbutton(root, text="Nam", variable=gioitinh,
            onvalue="Nam", offvalue="Nu",
            command=xu_ly_chon_gt).grid(row=4,column=3)

# Radio: lấy 1 giá trị trong nhóm
gender = IntVar()
Radiobutton(root, text="Male", variable=gender,
            value=0).grid(row=4,column=0)
Radiobutton(root, text="Female", variable=gender,
            value=1).grid(row=4,column=1)

# ComboBox Thành phố
thanhpho = StringVar()
dsThanhPho = ('HCM', 'Ha Noi', "Can Tho",
                         'Da Nang')
from tkinter import ttk
cboThanhPho = ttk.Combobox(root,
    textvariable=thanhpho,
    values=dsThanhPho).grid(row=5,column=1)

# List box
dsNghe = ['Bác sĩ', 'Công nhân', 'Giám đốc', 'Học viên']
nghe = StringVar(value=dsNghe)
lstNghe = Listbox(root,
    listvariable=nghe).grid(row=6,column=1)

# Define hàm bấm menu
def clickMenuAction(message):
    print(f"Click {message}")
    from tkinter import messagebox
    # messagebox.showinfo(title="Thông báo",
    #         message=f"Bạn vừa click menu {message}")
    answer = messagebox.askokcancel("Hỏi",
        message="Bạn chắc Thoát không?")
    if answer == True:
        root.quit()

clickMenuNew = partial(clickMenuAction, "Menu New")
clickMenuOpen = partial(clickMenuAction, "Menu OPEN")



# Menu
menubar = Menu(root)
mnuHeThong = Menu(menubar, tearoff=0)
mnuHeThong.add_command(label="New",command=clickMenuNew)
mnuHeThong.add_command(label="Open",command=clickMenuOpen)
mnuHeThong.add_command(label="Save")
mnuHeThong.add_separator()
mnuHeThong.add_command(label="Exit", command=root.destroy)
mnuHeThong.add_command(label="Thoat", command=root.quit)
menubar.add_cascade(label="He Thong", menu=mnuHeThong)

root.config(menu=menubar)
# Run
root.mainloop()


