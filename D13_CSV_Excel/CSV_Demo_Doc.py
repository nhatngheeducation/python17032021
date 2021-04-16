import csv

with open(r'.\data\DS-63-TINH-THANH.csv',
          encoding='utf-8') as file:
    rows = csv.reader(file)
    # print(type(rows))
    for row in rows:
        print(row)
        print(row[0], row[1])

with open(r'.\data\DS-63-TINH-THANH.csv',
              encoding='utf-8') as file:
    # Mo dang dict
    my_dict = csv.DictReader(file)
    print(type(my_dict))
    for item in my_dict:
        print(item)
        print(item['\ufeffSTT'], item["Tỉnh thành"])
