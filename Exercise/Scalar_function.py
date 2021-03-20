""" 
Question -->
Let's start with writing a scalar function scalar_function, which will apply the following operation with input x and y.

f(x,y)={x⋅y, if x≤y
        x/y, else.} 
 
Note that x and y are scalars. """

def scalar_function(x, y):
    """
    Returns the f(x,y) defined in the problem statement.
    """
    if x <= y:
        return x*y
    else:
        return x/y
