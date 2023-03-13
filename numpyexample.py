import numpy as np
# x = [1,2,3]
# y = np.array([1,2,3])
# print(type(y))
# print(type(x))
#
# x = np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)
# print(x)
#
# a = np.array([20, 30, 40, 50])
# b = np.arange(4)
# print(a+b)
# print(a-b)
# print(type(a))

# index_arr = arr[[1, 1, 0, 3],
#                 [3, 2, 1, 0]]
# print ("\nElements at indices (1, 3), "
#     "(1, 2), (0, 1), (3, 0):\n", Index_arr)

# arr = np.array([[1, 2, 3, 4],
#                 [5, 2, 4, 2],
#                 [1, 2, 0, 1]])
#
# # newarr = arr.reshape(2, 2, 3)
# #
# # print("\nOriginal array:\n", arr)
# # print("Reshaped array:\n", newarr)
#
# temp = arr[[0, 1, 2], [3, 2, 1]]
# print("\nElements at indices :\n", temp)
#
# arr = np.array([[1, 5, 6],
#                 [4, 7, 2],
#                 [3, 1, 9]])
#
# # maximum element of array
# print("Largest element is:", arr.max())
# print("Row-wise maximum elements:",
#       arr.max(axis=0))
# print("Row-wise maximum elements:",
#       arr.max(axis=1))
#
# print ("Cumulative sum along each row:\n",
#                         arr.cumsum(axis = 1))
#
# a = np.array([[1, 4, 2],
#               [3, 4, 6],
#               [0, -1, 5]])
#
# # sorted array
# print("Array elements in sorted order:\n",
#       np.sort(a, axis=None))
#
# dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]
#
# # Values to be put in array
# values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),
#           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]
#
# # Creating array
# arr = np.array(values, dtype=dtypes)
# print("\nArray sorted by names:\n",
#       np.sort(arr, order='name'))

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

# vertical stacking
print("Vertical stacking:\n", np.vstack((a, b)))

# horizontal stacking
print("\nHorizontal stacking:\n", np.hstack((a, b)))

c = [5, 6]

# stacking columns
print("\nColumn stacking:\n", np.column_stack((a, b)))

# concatenation method
print("\nConcatenating to 2nd axis:\n", np.concatenate((a, b), 1))