"""

sin = our_decorator(sin) instead of @our_decorator

"""
from math import sin, cos

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res = func(x)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

sin = our_decorator(sin)
cos = our_decorator(cos)

for f in [sin, cos]:
    f(3.1415)
    
"""
Before calling sin
9.265358966049026e-05
After calling sin
Before calling cos
-0.9999999957076562
After calling cos
"""
    
