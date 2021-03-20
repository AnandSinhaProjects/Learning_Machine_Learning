""" Question -->
Write a function called operations that takes as input two positive integers h and w, makes two random matrices 
A and B, of size h x w, and returns A,B, and s, the sum of A and B.
 """
import numpy as np

def operations(h, w):
    A = np.random.rand(h,w)
    B = np.random.rand(h,w)
    s = A+B
    print(A, B, s)

operations(3, 3)


