from jinja2 import Environment, FileSystemLoader
# Khai báo thư mục chứa template
env = Environment(loader=FileSystemLoader("."))
# Load template
template = env.get_template("bangdiem.txt")

svdata = [
    {
        "hoten" : "Trần Anh Hùng",
        "maso" : 2020123654,
        "ketqua": [
            { "tenmon" : "Toán", "diem": 7 },
            { "tenmon" : "Anh văn", "diem": 4.7 },
        ]
    },
    {
        "hoten" : "Lê Kim Anh",
        "maso" : 2020123456,
        "ketqua": [
            { "tenmon" : "Toán", "diem": 9 },
            { "tenmon" : "Anh văn", "diem": 7 },
        ]
    }
]

for sv in svdata:
    result = template.render(info=sv)
    with open(f"sv_{sv['maso']}.html", "w",
              encoding="utf-8") as myfile:
        myfile.write(result)
