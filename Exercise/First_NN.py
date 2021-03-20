import numpy as np


x1 = np.random.rand(2,1)
x2 = np.random.rand(2,1)
x1t = np.transpose(x1)
z = np.matmul(x1t, x2)
h = np.tanh(z)
print(h)

""" return np.tanh(x1.T @ x2)
or even:
return np.tanh(np.dot(x1.T, x2)) """