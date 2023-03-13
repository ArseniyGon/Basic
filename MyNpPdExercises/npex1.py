import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

SMALL_SIZE = 13
MEDIUM_SIZE = 14
BIGGER_SIZE = 16

plt.rc('font', size=SMALL_SIZE)
plt.rc('axes', titlesize=SMALL_SIZE)
plt.rc('axes', labelsize=MEDIUM_SIZE)
plt.rc('xtick', labelsize=MEDIUM_SIZE)
plt.rc('ytick', labelsize=MEDIUM_SIZE)
plt.rc('legend', fontsize=SMALL_SIZE)

titanic_data = pd.read_csv('train.csv')
#
# print(titanic_data.head(5))
#
# print(titanic_data.info())

n_titanic_data = titanic_data.drop(['Cabin', 'Ticket', 'Name', 'Fare', 'PassengerId'], axis=1)

# print(n_titanic_data.head())
#
# print(n_titanic_data.info())

descript = n_titanic_data.copy()

descript.loc[:, 'Embarked'].replace(['C', 'S', 'Q'], ['Cherbourg', 'Southampton', 'Queenstown'], inplace=True)

descript.loc[:, 'Survived'].replace([0, 1], ['No', 'Yes'], inplace=True)
print('_____')
gr=pd.DataFrame()
gr['{} No'.format('Embarked')] = descript.groupby('Embarked').size()
# print(gr['{} No'.format('Embarked')].divide(2))
# print(np.round(gr['{} No'.format('Embarked')].divide(2)))
print(gr['{} No'.format('Embarked')].sum())
gr['Embarked Ratio'] = np.round(gr['Embarked No'].divide(gr['Embarked No'].sum())*100,0)

# gr['{} No'.format('Embarked')].plot(kind='pie', autopct='%1.1f%%', title='{} Counts'.format('Embarked'), figsize=(16,8))
# plt.show()

print(gr)

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
# print(df.groupby('Team').size()['Points'].agg(np.size))
# df.groupby('Team').size().plot(kind='pie', autopct='%1.1f%%', title='{} Counts'.format('Embarked'), figsize=(16,8))
# plt.show()
grouped = df.groupby('Team')
print(grouped['Points'].agg([np.sum, np.mean, np.std]))
# df[]


def create_plot(df, col_name):
    new_gr = pd.DataFrame()
    new_gr['{} No'.format(col_name)] = df.groupby(col_name).size()
    new_gr['Embarked Ratio'] = np.round(gr['{} No'.format(col_name)].divide(gr['{} No'.format(col_name)].sum()) * 100)
    new_gr['{} No'.format(col_name)].plot(kind='pie', autopct='%1.0f%%', title='{} Counts'.format(col_name), figsize=(16,8))
    plt.show()

create_plot(descript, 'Embarked')