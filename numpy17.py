import numpy as np

num = np.array([[10,20,30],
                [40,50,60],
                [70,80,90]])


index = np.where(num > 25)


print(index)