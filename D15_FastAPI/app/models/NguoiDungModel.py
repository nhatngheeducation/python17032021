from pydantic import BaseModel


class NguoiDung(BaseModel):
    HoTen: str
    Email: str
    Username: str
