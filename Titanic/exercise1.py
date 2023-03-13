import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier


dataset = pd.read_csv('train.csv')
print(dataset.head())

x = dataset.iloc[:, 2:]
y = dataset.iloc[:, 1:2]

print(x.head())
print(y.head())

count = ['Name', 'Ticket', 'Cabin', 'Embarked']
x.drop(count, inplace=True, axis=1)
print(x)

x = np.array(x)
y = np.array(y)

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])],
                       remainder='passthrough')
x = np.array(ct.fit_transform(x))

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x)
x = imputer.transform(x)
print(x)

print("-----")

sc = StandardScaler()

x[:, 2:] = sc.fit_transform(x[:, 2:])

print(x)

print("-----")

gbc = GradientBoostingClassifier(learning_rate=0.5, max_depth=5, n_estimators=150)
gbc.fit(x, y)

x_test = pd.read_csv('test.csv', index_col=0)

count = ['Name', 'Ticket', 'Cabin', 'Embarked']
x_test.drop(count, inplace=True, axis=1)
x_test = np.array(x_test)
print(x_test)

X_test = pd.read_csv('test.csv', index_col=0)

count = ['Name', 'Ticket', 'Cabin', 'Embarked']
X_test.drop(count, inplace=True, axis=1)

X_test = np.array(X_test)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])],
                       remainder='passthrough')
X_test = np.array(ct.fit_transform(X_test))

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X_test)
X_test = imputer.transform(X_test)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_test[:, 2:] = sc.fit_transform(X_test[:, 2:])

gbc_predict = gbc.predict(X_test)

np.savetxt('my_gbc_predict.csv', gbc_predict, delimiter=",", header='Survived')



