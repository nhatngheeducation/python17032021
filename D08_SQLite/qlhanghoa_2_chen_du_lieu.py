# qlhanghoa_2_chen_du_lieu.py

import dbcommon
DbName = "QLHangHoa.db"

def them_moi_loai(connection, ten_loai):
    sql = f"INSERT INTO Loai(TenLoai) VALUES('{ten_loai}')"
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    return cursor.lastrowid # Trả về id vừa tăng


def them_hang_hoa(connection, hang_hoa_obj):
    sql = """
        INSERT INTO HangHoa(MaHH,TenHH,MoTa,DonGia,SKU,MaLoai)
        VALUES(?,?,?,?,?,?) 
    """
    cursor = connection.cursor()
    cursor.execute(sql, hang_hoa_obj)
    connection.commit()


conn = dbcommon.sql_connection(database_name=DbName)
ma_loai = them_moi_loai(conn, "Điện tử")
print("Vừa thêm loại có mã: ", ma_loai)
hh1 = ('HH0001','Sony 32s1','Tivi Sony 32" Full HD',
      11909, 'SKU0001', ma_loai)
hh2 = ('HH0002','Daikin 123','Máy lạnh Daikin 1HP Inverter',
      12999, 'SKU0010', ma_loai)
them_hang_hoa(conn, hh1)
them_hang_hoa(conn, hh2)
conn.close()
