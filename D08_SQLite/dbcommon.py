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