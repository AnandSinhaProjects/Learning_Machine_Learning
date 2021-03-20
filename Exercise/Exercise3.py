import numpy as np

A = np.array([1,2,3,4])
B = A+4
c = A+B
s = np.linalg.norm(c)
print(s)