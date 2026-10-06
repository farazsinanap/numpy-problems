import numpy as np

num = np.array([[1,0,-1],
                [0,-2,7],
                [6,-7,3]])

num[num < 0] = 0



print(num)