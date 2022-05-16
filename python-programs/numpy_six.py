import numpy as np
arr1 = np.array([[1, 2], [3, 4], [5, 6]])
arr2 = np.array([2, 2])

# broadcasting
print(arr1 + arr2)
print([[2], [3]] + arr2)