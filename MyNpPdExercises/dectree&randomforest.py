import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, confusion_matrix
from sklearn.model_selection import GridSearchCV
import warnings
warnings.filterwarnings("ignore")

data = {'feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'feature2': [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
        'target': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
        }

df = pd.DataFrame(data)
col = df.columns
# Разделение признаков(характеристик) от целевой переменной(зависимой переменной)
xtrain, xtest, ytrain, ytest = train_test_split(df[['feature1', 'feature2']], df['target'], test_size=0.5,
                                                random_state=1)

param_grid = {'penalty': ['l1', 'l2', 'elasticnet', None],
              'C': [0.1, 1, 10],
              'solver': ['lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga']
              }
param_grid_rf = {'n_estimators': [1,2,3,4,5]}

param_grid_dt={'criterion':['gini', 'entropy', 'log_loss'],
               'splitter':['best', 'random'],
               'max_depth':[1,2,3,4,5]}

random_forest = RandomForestClassifier()
grid_search_rf = GridSearchCV(random_forest, param_grid=param_grid_rf, cv=2)
grid_search_rf.fit(xtrain, ytrain)
# print('Best Parameters of rf:', grid_search_rf.best_params_)
random_forest.fit(xtrain, ytrain)
importances = random_forest.feature_importances_
indices = np.argsort(importances)[::-1]
ar_f = []
for f, idx in enumerate(indices):
    ar_f.append([round(importances[idx], 2), col[idx]])
print("Значимость признака:")
ar_f.sort(reverse=True)
rf_pred = random_forest.predict(xtest)

des_tree = DecisionTreeClassifier()
grid_search_dt = GridSearchCV(des_tree, param_grid=param_grid_dt, cv=2)
grid_search_dt.fit(xtrain, ytrain)

print(importances)
print(indices)
print(ar_f)

# print('Best Parameters of dt:', grid_search_dt.best_params_)
des_tree.fit(xtrain, ytrain)
ds_pred = des_tree.predict(xtest)

logr = LogisticRegression()
gridSearch_logr = GridSearchCV(logr, param_grid=param_grid, cv=2)
gridSearch_logr.fit(xtrain, ytrain)
# print('Best Parameters:', gridSearch_logr.best_params_)
logr.fit(xtrain, ytrain)
logr_pred = logr.predict(xtest)

rf_acc = accuracy_score(ytest, rf_pred)
ds_acc = accuracy_score(ytest, ds_pred)
logr_acc = accuracy_score(ytest, logr_pred)

# print(rf_acc)
# print(ds_acc)
# print(logr_acc)

