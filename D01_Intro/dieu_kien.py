toan = float(input("Nhap diem Toan"))

if toan < 0:
    print("Bạn nhap so am")
elif toan > 10:
    print("Diem lon hon 10")
else:
    print("Nhap hop le")
    xep_loai = None

    if toan >= 9:
        xep_loai = "Xuất sắc"
    elif toan >= 8.5:
        xep_loai = "Giỏi"
    elif toan >= 7:
        xep_loai = "Khá"
    elif toan >= 5:
        xep_loai = "Trung bình"
    else:
        xep_loai = "Yếu"

    print("Toán " + toan + " : " + xep_loai)
    print(f"Toán {toan} : {xep_loai}")