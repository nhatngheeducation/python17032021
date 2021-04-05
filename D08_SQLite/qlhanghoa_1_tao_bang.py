# qlhanghoa_1_tao_bang.py
import dbcommon

DbName = "QLHangHoa.db"
sql_create_table_loai = """
    CREATE TABLE Loai(
        MaLoai integer PRIMARY KEY,
        TenLoai varchar(40)
    )        
    """
sql_create_table_hang_hoa = """
    CREATE TABLE HangHoa(
        MaHH char(6) PRIMARY KEY,
        TenHH varchar(40), 
        MoTa varchar(55),
        DonGia decimal(10,2),
        SKU varchar(15) NULL,
        MaLoai interger NULL,
        FOREIGN KEY (MaLoai) REFERENCES Loai(MaLoai)
    )        
    """

connection = dbcommon.sql_connection(DbName)
dbcommon.create_table(connection, sql_create_table_loai)
dbcommon.create_table(connection, sql_create_table_hang_hoa)

if(connection):
    connection.close()