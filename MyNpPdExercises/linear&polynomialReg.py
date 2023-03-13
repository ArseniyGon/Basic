import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

# Linear Regression

# Create the arrays that represent the values of the x and y axis:
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Execute a method that returns some important key values of Linear Regression:
slope, intercept, r, p, std_err = stats.linregress(x, y)


# Create a function that uses the slope and intercept values to return a new value.
# This new value represents where on the y-axis the corresponding x value will be placed:
def myfunc(x):
    return slope * x + intercept


# Run each value of the x array through the function. This will result in a new array with new values for the y-axis:
mymodel = list(map(myfunc, x))

# Draw the original scatter plot:
plt.scatter(x, y)
# Draw the line of linear regression:
plt.plot(x, mymodel)
# Display the diagram:
plt.show()


# Polynomial Regression

# Create the arrays that represent the values of the x and y-axis:
x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

# NumPy has a method that lets us make a polynomial model:
mymodel_p = np.poly1d(np.polyfit(x, y, 3))

# Then specify how the line will display, we start at position 1, and end at position 22:
myline_p = np.linspace(1, 22, 100)

# Draw the original scatter plot:
plt.scatter(x, y)
# Draw the line of polynomial regression:
plt.plot(myline_p, mymodel_p(myline_p))
# Display the diagram:
plt.show()

#R-Squared
#It is important to know how well the relationship between the values of the x- and y-axis is,
# if there are no relationship the polynomial regression can not be used to predict anything.
#The relationship is measured with a value called the r-squared.
#The r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.
#Python and the Sklearn module will compute this value for you, all you have to do is feed it with the x and y arrays:
#print(r2_score(y, mymodel(x)))


X = sm.add_constant(x)
model = sm.OLS(y, X).fit()
print(model.summary())

