import numpy as np

a = np.array([[100, 1, 2, 100, 4], [10, 6, 7, 8, 9]])

print(a.max())
print(a.max(0))
print(a.max(1))