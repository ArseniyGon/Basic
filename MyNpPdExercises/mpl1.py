import numpy as np
import matplotlib.pyplot as plt

# x = np.array([4, 5, 6, 7, 8])
# y = np.array([1, 2, -6, 0, 4])
# plt.plot(x, y)
# plt.show()

# a = np.array([1, 1, 5, 5, 1])
# b = np.array([1, 5, 5, 1, 1])
# plt.plot(a, b)
# plt.show()

# y = np.arange(0, 5, 1)
# x = np.array([a*a for a in y])
# y2 = [0, 1, 2, 3]
# x2 = [i+1 for i in y2]
# plt.plot(x, y, x2, y2, '--')
# plt.grid()
# plt.show()

# y = np.arange(0, 5, 1)
# x = np.array([a*a for a in y])
# y2 = [0, 1, 2, 3]
# x2 = [i+1 for i in y2]
# lines = plt.plot(x, y, 'r--o', x2, y2, 'm:s', marker='+')
# print(lines)
# plt.setp(lines, linestyle='-.')
# plt.grid()
# plt.show()

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.cos(x)
plt.plot(x, y)
plt.fill_between(x, y)

plt.grid()
plt.show()







