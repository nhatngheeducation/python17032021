import sqlite3

mydb = sqlite3.connect("amydb.db")

cursor = mydb.cursor()
sql_statement = "select sqlite_version();"
result = cursor.execute(sql_statement)
record = cursor.fetchall()
print(record)
mydb.close()