import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pandas as pd


x = pd.DataFrame([1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22])
y = pd.DataFrame([100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100])

lin = LinearRegression()

lin.fit(x, y)
poly = PolynomialFeatures(degree = 4)
X_poly = poly.fit_transform(x)

poly.fit(X_poly, y)
lin2 = LinearRegression()
lin2.fit(X_poly, y)

plt.scatter(x, y, color='blue')

plt.plot(x, lin.predict(x), color='red')
plt.title('Linear Regression')
plt.xlabel('Temperature')
plt.ylabel('Pressure')


plt.scatter(x, y, color='blue')

plt.plot(x, lin2.predict(poly.fit_transform(x)), color='red')
plt.title('Polynomial Regression')
plt.xlabel('Temperature')
plt.ylabel('Pressure')

plt.show()