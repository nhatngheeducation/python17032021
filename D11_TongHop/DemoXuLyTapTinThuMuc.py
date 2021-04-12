import os

print("Thu muc hien tai: ", os.getcwd())
listFolderFiles = os.listdir()
for item in listFolderFiles:
    if os.path.isdir(item):
        print("Thu muc: ", item)
    elif os.path.isfile(item):
        print("File: ", item)
    else:
        print("khac: ", item)

print(os.listdir(r"C:\Users\NN\Documents\python17032021"))