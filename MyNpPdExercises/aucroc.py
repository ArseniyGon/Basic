import pandas as pd
import numpy
from sklearn import linear_model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, \
    roc_auc_score, roc_curve, r2_score, mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt

x = numpy.array([100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]).reshape(-1, 1)
y = numpy.array([1500, 2000, 2500, 3000, 3100, 4000, 4500, 5000, 5500, 6000, 6501])

linr = linear_model.LinearRegression()
linr.fit(x, y)

y_pred = linr.predict(x)
r2 = r2_score(y, y_pred)
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
print(mae)
print(r2)
print(mse)