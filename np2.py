import numpy as np


data = [1, 2, 3, 4, 5]

arr = np.array(data)

print(arr)
print(arr.shape)
print(arr.dtype)
print(arr.ndim)

arr2 = np.array([1, 2, 3, 4, 5])

print(arr2)
print(arr2.shape)
print(arr2.dtype)
print(arr2.ndim)

arr3 = np.array([1, 2, 3, 4, 5], dtype=np.float64)

print(arr3)
print(arr3.shape)
print(arr3.dtype)
print(arr3.ndim)
print(len(arr3))
print(arr3.ndim)

arr3 = arr3.astype(np.int64)
print(arr3)
print(arr3.dtype)

arr4 = np.arange(0, 20, 1.5)
print(arr4)

arr5 = np.linspace(0, 2, 50)
print(arr5)

print(" -- ")

random_arr = np.random.random((5,))
print(random_arr)

random_arr2 = np.random.random_sample((5,))
print(random_arr2)

random_arr3 = (10 - - 5)* np.random.random_sample(5,) - 5
print(random_arr3)


arr6 = np.array([1, 2, 3, 4, 5])
arr6 = np.sqrt(arr6)
print(arr6)

print(np.sin(arr6))
print(np.cos(arr6))
print(np.log(arr6))
print(np.exp(arr6))

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])
print(a)
print(b)

c = a + b
print(c)
print(a * b)

print(a - b)
print(a / b)
print("  -  -  ")

arr7 = np.array([1, 2, 3, 4, 5])
arr7 = arr7 * 2
print(arr7)

arr8 = np.array([1, 2, 3, 4, 5])
arr8 = arr8 ** 2
print(arr8)

sl = [1, 2, 3, 4, 5]
sl = sl * 2
print(sl)

arr9 = np.random.randint(-5, 10, 10)
print(arr9)

print(arr.max())
print(arr9.min())
print(arr9.mean())
print(arr9.std())
print(np.median(arr9))

print(arr9 < 2)

np.insert(arr9, 2, -20)
print(arr9)

np.delete(arr9, 2)
print(arr9)

np.sort(arr9)
print(arr9)

ar1 = np.array([0, 0, 0])
arr9 = np.concatenate((arr9, ar1))
print(arr9)

np.array_split(arr9, 3)
print(arr9)

print(" - -- ")

ar2 = np.array([1, -2, 3, -4, 5])
ar2[0] = 0
print(ar2[2])
print(ar2[0:2])
print(ar2[::-1])
print(ar2[ar2 < 2])
print(ar2[(ar2 < 2) & (ar2 > 0)])
print(ar2[(ar2 > 4) | (ar2 < 0)])
ar2[1:4] = 0
print(ar2)

print(" - - - - ")

mx = np.array([(1,2,3,), (4,5,6)], dtype=np.float64)
print(mx)

print(" - - - - ")

mx = np.array([(1,2,3,), (4,5,6), (7, 8, 9)])
print(mx)

print(" - - - - ")

a3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(a3d)

mx = np.array([(1,2,3,), (4,5,6), (7, 8, 9)])
print(mx.shape)
print(mx.ndim)
print(mx.size)
print(mx.reshape(1, 9))


print(" - - - - ")

mx = np.array([(1,2,3,), (4,5,6), (7, 8, 9), (10, 11, 12)])
print(mx.reshape(2, 6))

print(" - - - - ")
mx2 = np.random.random((2, 2))
print(mx2)

print(" - - - - ")
mx = np.resize(mx, (2,2))
print(mx)
print(" - - - - ")
nmx = np.arange(16).reshape(2,8)
print(nmx)

print(" - - - - ")

print(np.zeros((2,3)))
print(np.ones((3,3)))
print(np.eye(5))
print(np.full((3, 3), 9))
print(np.empty((3, 2)))
print(" - - - - ")
mx3 = np.array([(1, 2), (3, 4)])
print(mx3)
mx4 = np.array([(5, 6), (7, 8)])
print(mx4)
print(" - - - - ")

print(mx3+mx4)



Z = np.random.random((3, 3, 3))
print(Z)

Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()

print(Zmin, Zmax)

Z = np.ones((10,10))
Z[1:-1, 1:-1] = 0
print(Z)


0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
0.3 == 3 * 0.1
print(np.nan)

Z = np.diag(np.arange(1, 5))
print(Z)


Z = np.zeros((8,8), dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)

print(np.unravel_index(100, (6, 7, 8)))
j = np.array((6, 7, 8))
print(j)
