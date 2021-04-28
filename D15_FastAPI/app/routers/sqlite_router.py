from fastapi import APIRouter
from app.services.sqlite_service import *

router = APIRouter()

@router.get("/export_excel")
def export_hanghoa_to_excel():
    conn = sql_connection(r"data\QLHangHoa.db")
    # Lay data
    sql = "SELECT MaHH, TenHH, DonGia, SKU FROM HangHoa"
    result = query_data_by_statement(conn, sql)
    conn.close()

    # Xuat data xuống file excel

    # Cho phep download file
