import pandas as pd
import matplotlib.pyplot as plt


# # Define a dictionary containing employee data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# # Convert the dictionary into DataFrame
# df = pd.DataFrame(data)
#
# # converting and overwriting values in column
# df["Name"] = df["Name"].str.lower()

file = pd.read_csv('w.csv', index_col='Date/Time (LST)')
file['Temp (°C)'].plot(figsize=(18, 6))
# print(df)
#
# # making data frame from csv file
# data = pd.read_csv("nba.csv", index_col="Name")

#
# # retrieving row by loc method
# first = data.loc["Avery Bradley"]
# # second = data.loc["R.J. Hunter"]
#
# print(first, "\n\n\n", second)
#
# # making data frame from csv file
# data = pd.read_csv("nba.csv", index_col="Name")
#
# # retrieving columns by indexing operator
# first = data["Age"]
#
# print(first)



