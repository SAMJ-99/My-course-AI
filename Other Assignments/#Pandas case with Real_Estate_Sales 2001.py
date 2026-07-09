#Pandas case with Real_Estate_Sales 2001 2022

import pandas as pd

df = pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=",")

print(df)

#Printing datatype
print("df - data types" , df.dtypes)

print()

df_index_col = pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=",")

#Selecting Town column using .iloc
Town_column = df_index_col.iloc[:,3]
print("#Selecting Town column using .iloc")
print(Town_column)
print()

#Selecting Address column using .iloc
Address_column = df_index_col.iloc[:,4]
print("#Selecting Address column using .iloc")
print(Address_column)
print()

