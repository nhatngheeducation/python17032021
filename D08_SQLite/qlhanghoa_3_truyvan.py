import dbcommon
DbName = "QLHangHoa.db"

def query_data_by_statement(conn, query_statement):
    cursor = conn.cursor()
    cursor.execute(query_statement)
    result = cursor.fetchall()

    for row in result:
        print(row)

conn = dbcommon.sql_connection(DbName)
query_data_by_statement(conn, "SELECT * FROM Loai")
query_data_by_statement(conn, "SELECT * FROM HangHoa")
conn.close()