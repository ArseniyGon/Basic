import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


dt = pd.read_csv('advertising.csv')
print(dt.head())
print(dt.shape)

print(dt.isna().sum())
print(dt.isna().count())
print(dt.duplicated().sum())
#
# fig, axs = plt.subplots(3, figsize=(10, 5))
# plt1 = sns.boxplot(dt['TV'], ax=axs[0])
# plt2 = sns.boxplot(dt['Newspaper'], ax=axs[1])
# plt3 = sns.boxplot(dt['Radio'], ax=axs[2])
# plt.tight_layout()

# plt.show()

# sns.displot(dt['Sales'])

# sns.pairplot(dt, x_vars=['TV', 'Radio', 'Newspaper'], y_vars='Sales', height=4, aspect=1, kind='scatter')

# sns.heatmap(dt.corr(), annot = True)
# plt.show()

x = dt['TV'].array.reshape(-1, 1)
y = dt['Sales'].array.reshape(-1, 1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100)
slr = LinearRegression()
slr.fit(x_train, y_train)

print('Intercept: ', slr.intercept_)
print('Coefficient:', slr.coef_)

