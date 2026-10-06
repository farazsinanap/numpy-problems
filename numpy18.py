import numpy as np

num = np.array([20,50,30,40,10])

ascend = np.sort(num)
descend = ascend[::-1]



print("ascending order: ",ascend)
print("descending order: ",descend)