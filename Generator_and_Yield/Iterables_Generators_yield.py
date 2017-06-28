"""
Iterables

they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one.
You store it in memory
"""
>>> mylist = [x*x for x in range(3)]
>>> for i in mylist:
...    print(i)
0
1
4
"""
Generators

It is just the same except you used () instead of []. 
Generators are iterators, but you can only iterate over them once.
It's because they do not store all the values in memory, they generate the values on the fly:
BUT, you cannot perform for i in mygenerator a second time since generators can only be used once
They calculate 0, then forget about it and calculate 1, and end calculating 4, one by one.
"""
>>> mygenerator = (x*x for x in range(3))
>>> for i in mygenerator:
...    print(i)
0
1
4
"""
Yield

Yield is lazy, it puts off computation until you need it. 
A function with a yield in it doesn't actually execute at all when you call it. 
The iterator object it returns uses magic to maintain the function's internal context.
Each time you call next() on the iterator (as happens in a for-loop), execution inches forward to the next yield.
(Or return, which raises StopIteration and ends the series.)

"""
def squares_the_yield_way(n):             # Order of execution    
    for x in range(n):
        y = x * x
        yield y                           # 3rd,6th (includes above statements as well)
        
for square in squares_the_yield_way(4):   # 1st,5th
     print(square)                        # 2nd,4th  prints 0,1,4,9

print squares_the_yield_way(4)            # prints <generator object squares_the_yield_way at 0x000000000BB38240>
