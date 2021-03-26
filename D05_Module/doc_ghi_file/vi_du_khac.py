ten_file = "data_price.csv"
with open(ten_file, "w") as my_file:
    my_file.write("Gio,Mua vao, Ban ra\n")
    my_file.write("10:20,29000,30100\n")
    my_file.write("10:25,29000,30100\n")
    my_file.write("10:30,29100,31100\n")

with open(ten_file, "r") as my_file:
    lines = my_file.readlines()
    print(lines)