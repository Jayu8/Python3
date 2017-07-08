"""
We usually dont  incorporate any argument checks
If somebody  calls our function with a negative argument or with a float argument ( in factorial function) our function would 
go into an endless loop. So we can do arguement checks with decorator.
"""
#The following program uses a decorator function to ensure that the argument passed to the function factorial is a positiveinteger: 

#Notes:
#here helper is just a inner function used internally to abstact details
# 'factorial' goes to 'f' arguement in 'argument_test_natural_number' and 'numbers(1,2,etc)' goes to 'x' arguement in 'helper'

def argument_test_natural_number(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not an integer")
    return helper
    
@argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

for i in range(1,10):
	print(i, factorial(i))

print(factorial(-1))

""" output:
(1, 1)
(2, 2)
(3, 6)
(4, 24)
(5, 120)
(6, 720)
(7, 5040)
(8, 40320)
(9, 362880)
Exception: Argument is not an integer
"""
