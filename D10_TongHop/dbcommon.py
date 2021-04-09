# File dbcommon.py
import sqlite3


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


# Truy vân lấy dữ liệu
def query_data(conn, query_statement):
    cursor = conn.cursor()
    cursor.execute(query_statement)
    return cursor.fetchall()


# Thêm mới và trả về mã vừa thêm
def insert_and_get_inserted_id(conn, query_statement):
    cursor = conn.cursor()
    cursor.execute(query_statement)
    conn.commit()
    return cursor.lastrowid