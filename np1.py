import numpy as np

# x = np.zeros([5, 5])
# print(x)

y = np.matrix('1 2 3; 4 5 6; 7 8 9')

# print(y)
diag=np.diag(y)
# print(diag)

x = np.eye(3)
# print(x)

k = np.matrix('1 2 3; 4 5 6; 7 8 9')

# print(k.transpose())
# print((k.T).T)

A = np.matrix('1 2 3; 4 5 6')
B = np.matrix('7 8 9; 10, 11, 12')
C = (A + B).T
D = A.T + B.T
# print(D

a = np.matrix('1 2; 4 5')
det = np.linalg.det(a)
# print(det)



# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(x)

# Index values can be negative.
# arr = x[np.array([1, 3, -3])]
# print(arr)
a = np.array([[1 ,2 ],[3 ,4 ],[5 ,6 ]])
# print(a[[0 ,1, 2],[1,0, 0]])

b = np.array([[5, 6],[4, 5],[16, 4]])
sumrow = b.sum(-1)
print(sumrow)
print(b[sumrow%10==0])