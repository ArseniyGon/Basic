import numpy as np

#In the following example, one element of specified column from each row of ndarray object is selected.
# Hence, the row index contains all row numbers, and the column index specifies the element to be selected.
x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0, 1, 2], [0, 1, 0]]
print(y)

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]])
print('Our array is:')
print(x)
print('\n')

rows = np.array([[0, 0], [4, 4]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print('The corner elements of this array are:')
print(y)
print(x[[[0, 0], [4, 4]], [[0, 2], [0, 2]]])

x = np.array([[0,  1,  2], [3,  4,  5], [6,  7,  8], [9, 10, 11]])
print('Our array is:')
print(x)
print('\n')

z = x[1:4, 1:3]
print('After slicing, our array becomes:')
print(z)
print('\n')

y = x[1:, [1, 2]]
print('Slicing using advanced index for column:')
print(y)
print('\n')

x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])

print('Our array is:')
print(x)
print('\n')

# Boolean Indexing
print('The items greater than 5 are:')
print(x[x > 5])

# ~  Do not include
a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print(a[~np.isnan(a)])

a = np.array([1, 2+6j, 5, 3.5+5j])
print(a[np.iscomplex(a)])




