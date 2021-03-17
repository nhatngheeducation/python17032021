# Python khai giảng 17/03/2021

## Buổi 1 (17/03/2021)
* Hướng dẫn cài đặt
* Nhập xuất đơn giản với input, print
* Chuyển đổi kiểu dữ liệu: int(), float()
* Toán tử số học, toán tử luận lý
* Ghi chú với #, """...""", '''...'''
* Rẻ nhánh if ... elif ... else

### Chú ý 1: Python không có toán tử 3 ngôn, thay bằng 
```
    x = <giá trị True> if <biểu thức điều kiện> else <giá trị khi False>
```
### Chú ý 2: Python không có lệnh switch ... case mà tự xây dựng dictionary
```
	thang_dict = {
		1: 31, 3: 31, 4 : 30
	}
	print(f"So ngay thang 3 la {thang_dict.get(3)}")
```