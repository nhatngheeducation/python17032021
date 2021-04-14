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

# pip install pdfkit
# import pdfkit
# Install wkhtmltopdf
for sv in svdata:
    result = template.render(info=sv)
    filename = f"sv_{sv['maso']}"
    with open(f"{filename}.html", "w",
              encoding="utf-8") as myfile:
        myfile.write(result)
    # Convert html to pdf
    # pdfkit.from_file(f"{filename}.html", f"{filename}.pdf")