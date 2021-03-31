import re
template_sodt = "^0[978]\d{8}$"
#   [abc]: hoặc a, hoặc b, hoặc c
#   {m,n}: lặp từ m đến n lần
#   {m}: lặp chính xác
#   *: lặp từ 0 đến n
#   +: lặp từ 1 lần đến n lần
#   .   đại diện 1 kí tự

so_dt = input("Nhap so dien thoai: ")
result = re.search(template_sodt, so_dt)
if result != None:
    print("Hợp lệ")
    print(result)

pattern_email = "^[a-z]+(\.[a-z0-9]{2,})*@gmail.com$"
while True:
    gmail = input("Nhập địa chỉ gmail: ")
    test_match = re.search(pattern_email, gmail)
    if test_match != None:
        break


