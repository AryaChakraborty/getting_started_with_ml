'''
operations in numpy
'''

import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([0, 1, 2, 3, 4])
# element-wise operations
print(arr1 - arr2)
print(arr1>3)
# dot product
arr3 = np.array([1, 2, 3, 4, 5, 6]).reshape((2, 3))
arr4 = np.array([5, 6, 7, 8, 9, 10]).reshape((3, 2))
print(arr3.dot(arr4)) # matrix multiplication
print(arr4.min()) # axis = 0 is applicable within brackets
print(arr4.min(axis = 1))
print(arr4.sum(axis = 0))
print(arr4.mean())
print(arr4.std()) # standard deviation
print(arr4.ravel()) # rolls out the array

# the above whether methods, below will be functions
print(np.sin(arr4))
print(np.median(arr4))


# lets take new array
arr5 = np.array([[1, 2], [3, 4], [5, 6]])
arr5 = arr5.transpose()
print(arr5)

# stacking array horizontally
# arr5 is transposed
arr6 = np.array([[3, 4, 5], [5, 6, 7]])
print(arr5)
print(arr6)
print(np.hstack((arr5, arr6)))

# stacking array vertically
print(np.vstack((arr5, arr6)))

# fancy indexing
arr7 = np.arange(24).reshape((6, 4))
print(arr7)
print(arr7[[0, 2, 3]])