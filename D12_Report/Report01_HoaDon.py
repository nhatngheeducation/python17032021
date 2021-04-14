# Data cho report lấy từ quá trình xử lý trước đó

# pip install Jinja2
from jinja2 import Template
# Ví dụ 1: Template đơn giản chuỗi
template = Template('Hello {{ name }}. Call {{ phone }}!')
result = template.render(name='John Doe', phone="0909123456")
print(result)

# Ví dụ 2: Xuất hóa đơn
data_hoadon ={
    "hoten": "Nguyễn Văn Tèo",
    "dienthoai": "0909123789",
    "hanghoa":[
        { "ten":"Bia Sài Gòn", "gia":19500 },
        { "ten":"Tivi Sony 32", "gia":9190500 }
    ]
}
hoadon_template = """
        HÓA ĐƠN
- Người mua: {{ hoadon.hoten }}.
- Số điện thoại: {{ hoadon.dienthoai }}.
    DANH SÁCH HÀNG MUA 
{% for item in hoadon.hanghoa %}
    +  {{ item.ten }} - {{ item.gia }} đ.
    {# Comment #}
{% endfor %}
"""
hoadon_template = Template(hoadon_template)
print(hoadon_template.render(hoadon=data_hoadon))