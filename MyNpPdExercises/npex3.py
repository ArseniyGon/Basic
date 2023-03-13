# Three lines to make our compiler able to draw:
# import sys
# import matplotlib
# import matplotlib.pyplot as plt
# from scipy import stats

# matplotlib.use('Agg')
#
# x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
# y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
#
#
# def some_value(z):
#     return 5 + z, 10 + z
#
#
# e, f = some_value(5)
# print(e)
# print(f)
#
# slope, intercept, r, p, std_err = stats.linregress(x, y)
#
#
# def myfunc(x):
#     return slope * x + intercept
#
#
# mymodel = list(map(myfunc, x))
#
# plt.scatter(x, y)
# plt.plot(x, mymodel)
# plt.show()
#
# # Two  lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()

#------------------------
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
# df = sb.load_dataset('tips')
# sb.regplot(x = "total_bill", y = "tip", data = df)
# sb.lmplot(x = "total_bill", y = "tip", data = df)
# plt.show()

df = sb.load_dataset('anscombe')
sb.lmplot(x = "x", y = "y", data = df.query("dataset == 'II'"), order=1)
plt.show()