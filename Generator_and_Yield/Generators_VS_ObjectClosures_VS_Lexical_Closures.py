"""
Using Generators  
"""
from itertools import islice

def fib_gen():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

assert [1, 1, 2, 3, 5] == list(islice(fib_gen(), 5))
"""
Using Lexical Closures  (Functional Programming) function within a function 
"""
def ftake(fnext, last):
    return [fnext() for _ in xrange(last)]

def fib_gen2():
    def _():          #executed durinng fnext() call
        _.a, _.b = _.b, _.a + _.b
        return _.a
    _.a, _.b = 0, 1   #executed during init
    return _

assert [1,1,2,3,5] == ftake(fib_gen2(), 5)
"""
Using object closures 
"""
def ftake(fnext, last):                          # 4th fnext = instance of fibnext3 class; last=5 
    return [fnext() for _ in xrange(last)]       #5th for _ in xrange(last) gives 1 to 5.
                                                 #6th fnext() calls  __call__ in fibgen3 class this happens 5 times
                                                 #8th the values recieved are stored in a list
class fib_gen3:
    def __init__(self):                           #2nd __init__ and statements
        self.a, self.b = 1, 1

    def __call__(self):                           #7th this is called using fnext() which is instance of this class
        r = self.a         
        self.a, self.b = self.b, self.a + self.b
        return                                    #returns to fnext and stored  

# Last if not equal assertio error,if equal nothing        
assert [1,1,2,3,5] == ftake(fib_gen3(), 5)         #1st fib_gen3() ; 3rd  full function ftake(,) 
