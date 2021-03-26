try:
    my_file = open("./data.txt", "r", encoding="utf8")
    van_ban = my_file.read()
    print(van_ban)
    # print(my_file.readline())
    my_file.close()
except Exception as ex:
    print(ex)