###Question

""" Write a function called randomization that takes as input a positive integer n, 
and returns A, a random n x 1 Numpy array. """

import numpy as np

n = int(input("n x 1 matrix where n = ? ---> "))
x = np.random.rand(n,1)

print(x)


"""
Output ->

n x 1 matrix where n = ? ---> 12
[[0.86381036]
 [0.77954276]
 [0.66877705]
 [0.33452177]
 [0.16267312]
 [0.06765608]
 [0.81522689]
 [0.9854236 ]
 [0.2366171 ]
 [0.75609717]
 [0.22736756]
 [0.65357186]] """