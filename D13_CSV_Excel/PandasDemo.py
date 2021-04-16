import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'price': [3, 7, 1]
}

myvar = pd.DataFrame(mydataset)
print(myvar)
with pd.ExcelWriter("Pandas_data.xlsx") as file:
    myvar.to_excel(file)
