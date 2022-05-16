import numpy as np
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print(arr1.shape, arr1.ndim, arr1.size, arr1.itemsize, arr1.dtype)
arr2 = np.zeros((2, 2))
print(arr2.shape, arr2.ndim, arr2.size, arr2.itemsize, arr2.dtype)
arr2 = arr2.astype(int)
print(arr2)