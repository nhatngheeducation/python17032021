# Tinh diem chuan thi vao 1 truong DH
marks = [
    20, 21, 20, 21, 22, 23, 20,
    17, 16, 15, 20, 21, 23, 21,
    20, 21, 24, 27, 20, 28, 26,
    25, 24, 23, 23, 20, 21, 24,
    22, 14, 13, 12, 14, 15, 16
]
qty = 10 # Số lượng thí sinh cần thi

counts = {} # Dictionary [điểm] = <số lượng TS đạt điểm>
for mark in marks:
    #counts[mark] = counts.get(mark, 0) + 1
    counts[mark] = marks.count(mark)

print("Thống kê số lượng TS theo điểm:")
print(counts)

count_items = counts.items()
print(type(count_items))
count_items = sorted(count_items, reverse=True)
print(count_items)

# TODO: Di tu cao xuong thap, lay du chi tieu thi dung lai
acc = 0
thresh = 0
for mark, count in count_items:
    if acc + count > qty:
        break
    acc += count
    thresh = mark

print(thresh, acc)
