import openpyxl as openpyxl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


# df = pd.DataFrame(np.random.rand(20, 4),columns=['a','b','c','d'])
# df.plot.bar(stacked=True)
# plt.show()

# df = pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':
# np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])
# df.plot.hist(bins=20)
# plt.show()

df = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

# print(df.info())
df.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
# print(df.head())
# print(df.columns)
df.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
# print(df.columns)
# df.columns.append['Total']



# df["NaN_Column"] = np.nan
# df["None_Column"] = None
# print(df['Total'])
df = df.set_index('Country')
# print(df.head())
years = list(range(1980, 2014))
# df["Total"] = df[years].count()
print(years)
print(df.loc[['Switzerland'], years])
df['Total'] = df[years].sum(axis=1)
df.loc['Switzerland', years].plot()
plt.title('Immigration from Switzerland')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
# plt.show()
ind_pak_ban = df.loc[['India', 'Pakistan', 'Bangladesh'], years]
# print(ind_pak_ban.head())
print(ind_pak_ban.T)
ind_pak_ban.T.plot()
# plt.show()
# cont = df.groupby('Continent', axis=0).sum()
# print(cont.T)
# print(df[years].sum())
print('!!!!!!!')
print(df['Total'])
