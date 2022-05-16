'''
indexing
slicing
iteration
'''
import numpy as np
arr1 = np.arange(24).reshape(6, 4)
arr2 = arr1[2:4, 1:3] # slicing
print(arr1)
print(arr2)
print(arr1[1, 1]) # indexing
# both arr1[1, 1] and arr1[1][1] works the same

# printing
for item in np.nditer(arr2) :
    print(item, end=',')