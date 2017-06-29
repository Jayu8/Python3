#Using MAP with functions

from math import sin, cos, tan, pi

def map_functions(x, functions):
     """ map an iterable of functions on the the object x """
     res = []
     for func in functions:
         res.append(func(x))
     return res

family_of_functions = (sin, cos, tan)
print(map_functions(pi, family_of_functions)) 

# output: [1.2246467991473532e-16, -1.0, -1.2246467991473532e-16]

#LIST COMPREHENSIONS in python

def map_functions(x, functions):
     return [ func(x) for func in functions ]

