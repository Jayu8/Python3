from random import random, randint, choice

def our_decorator(func):
    def function_wrapper(*args, **kwargs):
        print("Before calling " + func.__name__)
        res = func(*args, **kwargs)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

for f in [random, randint, choice]:
    f = our_decorator(f)

random = our_decorator(random) 
randint = our_decorator(randint)
choice = our_decorator(choice)
random()
randint(3, 8)
choice([4, 5, 6])

"""
The result looks as expected:  
Before calling random
0.16420183945821654
After calling random
Before calling randint
8
After calling randint
Before calling choice
5
After calling choice
"""
