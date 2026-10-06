import numpy as np


num = np.array([[20,30,40],
                [50,60,80],
                [20,80,10]])

count = np.sum(num > 50)


print("the number of elements which are greater: ",count)