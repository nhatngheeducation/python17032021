import pandas

excelFile = ".\data\FinancialSample.xlsx"

# data = pandas.read_excel(excelFile, sheet_name=0)
data = pandas.read_excel(excelFile, header=None, skiprows=5)
print(data)
print("Số lượng dòng cột: ", data.shape)

# Thong ke
print(data.describe())

# Xuat file
data.to_excel("result.xlsx")

row_header = data.head()
print(row_header)