from fastapi import APIRouter
from app.services.sqlite_service import *
from openpyxl import Workbook
from openpyxl.styles import numbers
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/export_excel")
def export_hanghoa_to_excel():
    conn = sql_connection(r"data\QLHangHoa.db")
    # Lay data
    sql = "SELECT MaHH, TenHH, DonGia, SKU FROM HangHoa"
    result = query_data_by_statement(conn, sql)
    conn.close()

    # Xuat data xuống file excel
    workbook = Workbook()
    sheet = workbook.active
    sheet["A1"] = "Mã hàng hóa"
    sheet.cell(row=1, column=2, value="Tên hàng hóa")
    sheet.cell(row=1, column=3, value="Đơn giá")
    sheet.cell(row=1, column=4, value="SKU")
    rowIndex = 2
    for item in result:
        sheet.cell(row=rowIndex, column=1, value=item[0])
        sheet.cell(row=rowIndex, column=2, value=item[1])
        sheet.cell(row=rowIndex, column=3, value=item[2])
        sheet.cell(row=rowIndex, column=3).number_format = numbers.FORMAT_TEXT
        sheet.cell(row=rowIndex, column=4, value=item[3])
        rowIndex = rowIndex + 1

    excel_file_name = "hanghoa.xlsx"
    workbook.save(filename=excel_file_name)
    workbook.close()
    # Cho phep download file
    return FileResponse(path=excel_file_name,
        filename=excel_file_name,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
