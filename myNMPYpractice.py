import sys

import numpy as np
import random


a = np.array([1, 2, 3])
print(a)
print(type(a))

b = np.array([[1.5, 2, 3], [4, 5, 6]])
print(b)

b = np.array([[1.5, 2, 3], [4, 5, 6]], dtype=np.complex128)
print(b)

print("-----------------")

print(np.zeros((3, 5)))
print(np.ones((2, 2, 2)))
print(np.eye(5))
print(np.empty((3, 3)))
print(np.empty([4, 4]))
print(np.arange(10, 30, 5))
print(np.arange(0, 1, 0.1))
print(np.linspace(0, 2, 9))

print("-----------------")


def f1(i, j):
    return 4 * i + j


x = np.fromfunction(f1, (3, 5))
print(x)

y = np.fromfunction(f1, (3, 3))
print(y)

print(np.arange(0, 306, 1))

print("-----------------")

print(np.arange(0, 5000, 1))


a = np.array(([[0, 1, 2], [10, 12, 13]], [[100, 101, 102], [110, 112, 113]]))
print(a.shape)
print(a[1, ...])
print(a[:, :, 1])
print(a[..., 1])
print(a)
a.shape = (6, 2)
print(a)
print(a.reshape((3, 4), order='A'))
print(a.reshape((3, 4), order='C'))
print(a.reshape((3, 4), order='F'))


print(a)
a.resize(2, 6)
print(a)
print("_____________")
a = np.arange(12).reshape((2, 6))
print(a)

print(np.hsplit(a, 3)) # Разбить на 3 части

print(np.hsplit(a, (3, 4)))  # Разрезать a после третьего и четвёртого столбца

a = np.arange(10)
print(a)
z = np.random.choice(a, 10, p=[0.5, 0, 0, 0.1, 0.1, 0.1, 0.1, 0.1, 0, 0])
print(z)

z = np.random.random((3,3,3))
print(z)

k = np.random.random((10,10))
Zmin, Zmax = k.min(), k.max()
print(Zmin, Zmax)

print("------------")

z = np.ones((10, 10))
z[1:-1, 1:-1] = 0
print(z)
