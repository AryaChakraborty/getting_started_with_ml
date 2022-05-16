import numpy as np
arr1 = np.random.randint(low=1, high=100, size=24).reshape((6, 4))
print(arr1)
print(arr1[(arr1>50) & (arr1%2!=0)])

# plotting graphs
import matplotlib.pyplot as plt
x = np.linspace(-30, 30, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()