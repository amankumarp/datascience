import numpy as np
arr =np.array([1,2,3])
print(arr)
arr2=np.append(arr,[4,7])
print(arr2)
arr3=np.delete(arr2,1)
print(arr3)
arr4=np.concatenate((arr,np.array([3,4])),axis=0)
print(arr4)