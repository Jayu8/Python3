"""
Conditions:
All functions must have same no of parameters as the decorator function.
The decorator must be placed in front of all these functions if it has to be modified
"""

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res=func(x)
        print("After calling " + func.__name__)
        print(res)
    return function_wrapper

@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))
    return x + 1

@our_decorator
def succ(n):
    print("Hi, foo has been called with " + str(n))
    return n + 1

foo(10)
succ(11)

output
"""
Before calling foo
Hi, foo has been called with 10
After calling foo
11
Before calling succ
Hi, foo has been called with 11
After calling succ
12
"""
