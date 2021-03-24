
a = [1, 3, 5, 7, 3, 18.1, 19, 39, 21]
print(a)
a.sort()
a.sort(reverse=True)
# a.remove(3)
print(a)

# Tìm index(ele), index(ele, start)
print("Vị trí đầu tiên tìm thấy trong mảng")
print(a.index(3))
print(a.index(3, 1))
print(a.index(3, 3))

# in và not in dùng kiểm tra tồn tại hay không tồn tại củ phần tử trong mảng
print(11 in a)
print(18.1 not in a)

print(a[2:])
print(a[2:-1])
print(a[:-2])
print(a[:-2])
print("S = 1 --> 6:" ,a[1:6])

# trong dãy từ [start:end) lấy có Vị trí thứ tự chia hết cho 3
print(a[1:8])
print(a[1:8:3])

print("Số phần tử", len(a))
print("S =", sum(a))
print("max =", max(a))
print("min =", min(a))
