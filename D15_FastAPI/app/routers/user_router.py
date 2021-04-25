from fastapi import APIRouter
import mysql.connector
from app.models.NguoiDungModel import NguoiDung

router = APIRouter()


@router.get("/user",  response_description="Get list user")
def get_all_user():
    mydb = mysql.connector.connect(
        host="sql6.freemysqlhosting.net",
        user="sql6407749",
        password="dMuLKDMrDB",
        database="sql6407749"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM nguoidung")
    myresult = mycursor.fetchall()
    users = []
    for nd in myresult:
        users.append(NguoiDung(
            HoTen = nd[3],
            Email = nd[4],
            Username = nd[1]
        ))

    return users