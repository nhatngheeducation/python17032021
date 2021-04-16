import pandas
df = pandas.read_csv('hrdata.csv', index_col='Phone',
                     parse_dates=['BirthDate'])
print(df)
for item in df:
    print(item)
    print(df[item])

# Ghi xuống file csv
df.to_csv("hrdata_edited.csv")