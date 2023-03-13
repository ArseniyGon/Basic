import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold, cross_val_score


x = np.array([[1, 2], [3, 4], [5, 6], [7, 10]])
y = np.array([3, 7, 11, 15])

kfold = KFold(n_splits=3)
for train, test in kfold.split(x):
    x_train, x_test = x[train], x[test]
    y_train, y_test = y[train], y[test]
    model = LinearRegression().fit(x_train, y_train)

    print('Train', x_train, y_train)
    print('Test', x_test, test)


model = LinearRegression()
score = cross_val_score(model, x, y, cv=2)
print(score.mean(), score.std())
print(score)

