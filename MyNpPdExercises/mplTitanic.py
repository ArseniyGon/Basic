import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('train.csv')
# print(df)
# print(df.info())
# print(df.columns)

df.drop(columns=['Cabin', 'Embarked', 'Ticket', 'Name'], inplace=True)
# # print(df.columns)
df.rename(columns={'Pclass': 'Cabin Class', 'SibSp': 'With Siblings', 'Parch': 'Prnt w Child'},
          inplace=True)
# # print(df.columns)
df.replace({'Survived': {1: 'Yes', 0: 'No'}}, inplace=True)
df.replace({'Sex': {'male': 'Male', 'female': 'Female'}}, inplace=True)
df.replace({'Cabin Class': {1: '1st', 2: '2nd', 3: '3rd'}}, inplace=True)
#
s = df['Survived']
c = df['Cabin Class']
sex = df['Sex']
age = df['Age']
ws = df['With Siblings']
wc = df['Prnt w Child']
f = df['Fare']
# # print(df)

# print(age.hasnans)
# print(s.hasnans)
# print(c.hasnans)
# print(sex.hasnans)
# print(ws.hasnans)
# print(wc.hasnans)
# print(f.hasnans)

# df.fillna(age.mean(), inplace=True)
# print(age.head(50))

df.fillna(age.mean().astype(int), inplace=True)
# print(age.head(50))   #can't round off


np.ct_c = df.groupby(c)['PassengerId'].count()
# print(np.ct_c)
np.ct_sex = df.groupby(sex)['PassengerId'].count()
# print(np.ct_sex)
np.ct_ws = df.groupby(ws)['PassengerId'].count()
# print(np.ct_ws)
#
np.ct_wc = df.groupby(wc)['PassengerId'].count()
#
np.ct_s = df.groupby(s)

print(np.ct_s)
np.ct_c_sex_s = df.groupby(c)[['Sex', 'Survived']].value_counts().sort_index()
# print(np.ct_c_sex_s)
np.ct_c_sex_f = df.groupby(['Cabin Class', 'Sex'])['Fare'].median().round(2).sort_values(ascending=False)
# print(np.ct_c_sex_f)

# plt.show()

fig, axes = plt.subplots(nrows=2, ncols=2)

x1 = np.ct_c.plot.bar(ax=axes[0,0])

x2 = np.ct_sex.plot.pie(ax=axes[0,1], autopct='%1.0f%%')
x3 = np.ct_c_sex_f.plot.bar(ax=axes[1,0], x='Frequency', y='Count')
x4 = np.ct_c_sex_s.plot.bar(ax=axes[1,1])

plt.show()