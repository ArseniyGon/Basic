import html5lib as html5lib
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# website ="https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table"
# df_list = pd.read_html(website, flavor='html5lib')
# df = df_list[2]
# print(df.info())

# data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
# 		'Height': [5.1, 6.2, 5.1, 5.2],
# 		'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
# df = pd.DataFrame(data)
# print(df)
# print(df['Height']==5.1)
# print(df[(df['Height']==5.1)])


x = ['А', 'Б', 'В']
y = [10, 50, 30]

# sns.barplot(x=x, y=y)
# df = pd.DataFrame({'Name': ['Bob', 'Tom', 'Alice'], 'Age': [10, 50, 30]}, index=['Index 1', 'Index 2', 'Index 3'])
# sns.barplot(df, x='Name', y='Age')
# sns.barplot(data=df, x='Name', y='Age', palette='hls')
df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
print(df[:5])
sns.regplot(df[:20], x='A', y='B')
plt.show()
