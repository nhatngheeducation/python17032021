import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database specified by db_file.
    :param db_file: database file
    :return: Connection object or None
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return connection


def create_table(connection, create_table_sql):
    """ create a table from the create_table_sql statement
    :param connection: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = connection.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)



def main():
    database = r"pythonsqlite.db"
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

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create Loai table
        create_table(conn, sql_create_table_loai)

        # create HangHoa table
        create_table(conn, sql_create_table_hang_hoa)

        # close connection
        conn.close()
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
