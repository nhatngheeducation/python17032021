import sqlite3

database_name = "database_name"


def sql_connection(database_name):
    try:
        db = sqlite3.connect(database_name)
        return db
    except Exception as e:
        print(e)
        return None


def create_table(connection, create_table_sql):
    try:
        cursor = connection.cursor()
        result = cursor.execute(create_table_sql)
        connection.commit()
    except Exception as ex:
        print(ex)


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


def query_data_by_statement(conn, query_statement):
    cursor = conn.cursor()
    cursor.execute(query_statement)
    return cursor.fetchall()
