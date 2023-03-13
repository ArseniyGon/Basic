import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier


# Create a data frame
data = {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 5, 4, 5]}
data1 = {'x': [10, 20, 30, 40, 50], 'y': [2, 4, 5, 4, 5]}
df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)

# Create a linear regression object
reg = LinearRegression()

# Fit the linear regression model
reg.fit(df[['x']], df['y'])

# Print the intercept and coefficient
# print(reg.intercept_)
# print(reg.coef_)

# Predict the y values using the model
y_pred = reg.predict(df1[['x']])

# Print the predicted y values
# print(y_pred)



# Create a data frame
data = {'age': [25, 35, 45, 20, 30, 50],
        'income': [50000, 70000, 90000, 40000, 60000, 80000],
        'label': ['low', 'medium', 'high', 'low', 'medium', 'high']}
# data1 = {'age': [25, 35, 45, 20, 30, 50],
#         'income': [50000, 70000, 90000, 40000, 60000, 80000],
#         'label': ['low', 'medium', 'high', 'low', 'medium', 'high']}
df = pd.DataFrame(data)
# df1 = pd.DataFrame(data1)

reg = LinearRegression()

label_map = {'low': 0, 'medium': 1, 'high': 2}

# Use the map() function to replace string values with integer values
df['label'] = df['label'].map(label_map)

# Fit the linear regression model
reg.fit(df[['age', 'income']], df['label'])


pred = reg.predict([[40, 75000]])
# Create a KNN classifier object
knn = KNeighborsClassifier(n_neighbors=3)

# Fit the KNN model
knn.fit(df[['age', 'income']], df['label'])

# Make a prediction
prediction = knn.predict([[40, 75000]])

# Print the prediction
print(prediction)
print(pred)

