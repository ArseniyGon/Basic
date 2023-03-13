import numpy as np
import pandas as pd

data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}

df = pd.DataFrame(data)
print(df)

data = {'Name': ['Jai', 'Princi', 'Guarav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}
df = pd.DataFrame(data)
print(df[['Name', 'Qualification']])

data = pd.read_csv('nba.csv', index_col="Name")
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]
print(first, "\n\n\n", second)

print("------")

data = pd.read_csv("nba.csv", index_col="Name")
first = data["Age"]
print(first)

print("------")

data = pd.read_csv('nba.csv', index_col="Name")
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]

row2 = data.iloc[3]
print(row2)

print("------")

dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score':[30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}

df = pd.DataFrame(dict)
x = df.drop(["Second Score"], axis = 1, inplace = False)
print(df)
print(x)

print(df.loc[1])
print(df.iloc[2])
print(df.loc[1] == df.iloc[2])


print("------")

# ser=pd.Series(range(1,20,3), index=[x for x in 'abcdefg'])
# print(ser)

# ser=np.arange(10,15)
# serobj=pd.Series(data=ser*5,index=ser)
# print(serobj)


