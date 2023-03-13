import matplotlib.pyplot as plt
import numpy
import pandas as pd


x = pd.DataFrame([0, 2, 4])
y = pd.DataFrame([-2, -1, 0])

# plt.plot(x+5, y)
plt.plot(x, y)
# plt.plot(x, y+5)
plt.plot(5*x, y)
plt.plot(x, 2*x+5)
plt.show()