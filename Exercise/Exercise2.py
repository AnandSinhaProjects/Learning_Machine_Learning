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

""" 
Output -->

[[0.33258851 0.25162376 0.20697785]
 [0.92599869 0.63357889 0.22677685]
 [0.83570922 0.81507417 0.2866905 ]] [[0.72564763 0.4759478  0.48936218]
 [0.1472687  0.90887003 0.92533503]
 [0.68539137 0.75784467 0.35834649]] [[1.05823614 0.72757156 0.69634003]
 [1.07326738 1.54244892 1.15211188]
 [1.5211006  1.57291884 0.645037  ]] """