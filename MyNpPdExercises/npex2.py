import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# x = np.array(["Small", "Medium", "Large"])
# y = np.array([4, 3, 2])
#
# myexplode = [0.1, 0, 0]
# plt.boxplot(y)
# plt.show()

# A = np.arange(10)
# print(A[np.logical_and(A != 5, A != 0)])

# fig = plt.figure(figsize=(10, 6))
# x = np.array([1, 3, 5, 7])
# y = np.array([2, 4, 6, 8])
# axes = fig.add_axes([0,0,1,1]) # создаем прямоуголник для построение графиков в виде списка [left, bottom, width, height]
#
# axes.plot(x, x**2, 'r') # добавить первую кривую на холст красного цвета
# axes.plot(x, x**3, 'b*--') # добавить вторую крикую на холст синего цвета с маркерами другого типа
#
# axes.set_xlabel('x') # добавить название оси Х
# axes.set_ylabel('y') # добавить название оси Y
# axes.set_title('Hello proglib') # добавить название всего графика
# axes.legend([r'$x^2$', r'$x^3$'], loc=0) # добавить легенду
#
# plt.show() # вывести график на экран
#------------------------------------------------
# fig = plt.figure()
#
# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # основной график
# axes2 = fig.add_axes([0.2, 0.5, 0.3, 0.5]) # внутренный график. Его размер меньше, цифры показывают долю от figsize
#
# # Основной график
# axes1.plot(x, x**2, 'r')
# axes1.set_xlabel('x')
# axes1.set_ylabel('y')
# axes1.set_title('Я внешний график')
#
# # Вложенный график
# axes2.plot(x**2, x, 'b')
# axes2.set_xlabel('y')
# axes2.set_ylabel('x')
# axes2.set_title('Я внутренний график')
#
# plt.show()
#------------------------------------------------

# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# ax1.plot([1,2,3])
# ax2 = fig.add_subplot(221, facecolor='y')
# ax2.plot([1,2,3])
#
# plt.show()

#------------------------------------------------

# fig, a = plt.subplots(2, 2)
#
# x = np.arange(1,5)
# print(x[3])
# a[0][0].plot(x)
# plt.show()


df = pd.read_csv("https://www.w3schools.com/python/pandas/data.csv.txt")
# print(df.describe())
#
d=df['Duration']
c=df['Calories']
p=df['Pulse']
m=df['Maxpulse']
#
# fig,a =  plt.subplots(2,2)
# a[0][0].plot(d)
# a[0][0].set_title('Duration')
# a[0][1].plot(c)
# a[0][1].set_title('Calories')
# a[1][0].plot(p)
# a[1][0].set_title('Pulse')
# a[1][1].plot(m)
# a[1][1].set_title('Maxpulse')
# plt.show()
#---------------------------
# a1 = plt.subplot2grid((3,3),(0,0),colspan = 2)
# a2 = plt.subplot2grid((3,3),(0,2), rowspan = 3)
# a3 = plt.subplot2grid((3,3),(1,0),rowspan = 1, colspan = 2)
#
# x = np.arange(1,10)
# a2.plot(x, x*x)
# a2.set_title('square')
# a1.plot(x, np.exp(x))
# a1.set_title('exp')
# a3.plot(x, np.log(x))
# a3.set_title('log')
# plt.tight_layout()
# plt.show()

#-------------------------
fig, axes = plt.subplots(1, 2, figsize=(10,4))
x = np.arange(1,5)
axes[0].plot(d)
axes[0].plot(c)
axes[0].set_title("Duration & Calories")
axes[1].plot (p)
axes[1].plot(m)
axes[1].set_yscale("log")
axes[1].set_title("Pulse & Max Pulse")
axes[0].set_xlabel("x axis")
axes[0].set_ylabel("y axis")
axes[0].xaxis.labelpad = 10
axes[1].set_xlabel("x axis")
axes[1].set_ylabel("y axis")
plt.show()