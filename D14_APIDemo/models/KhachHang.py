from pydantic import BaseModel

class khach_hang(BaseModel):
    ma_so : int
    ho_ten: str
    doanh_so: float
    active: bool
    email: str