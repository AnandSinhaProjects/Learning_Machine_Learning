""" 
Question

Write a function called norm that takes as input two Numpy column arrays A and B, 
adds them, and returns s, the L2 norm of their sum.
 """

import numpy as np

A = np.array([1,2,3,4])
B = A+4
c = A+B
s = np.linalg.norm(c)
print(s)

""" Output -->

18.547236990991408 """