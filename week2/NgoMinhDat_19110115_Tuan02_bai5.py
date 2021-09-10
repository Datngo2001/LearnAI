import numpy as np

def sapxep(arr, xeptang):
    arr.sort()
    if xeptang:
        return np.flip(arr)
    return arr 

arr = np.array([1,4,5,7,2,4,67])
arr = sapxep(arr,True)
print(np.flip(arr))