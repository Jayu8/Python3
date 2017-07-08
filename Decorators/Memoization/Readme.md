Memoization is memorizing the calculation results of processed input such as the results of function calls.<br>
If the same input or a function call with the same parameters is used, the previously stored results can be used again <br>
and unnecessary calculation are avoided. <br>
In many cases a simple array is used for storing the results, but lots of other structures can be used as well,<br>
such as associative arrays, called hashes in Perl or dictionaries in Python. <br>

#here program is kept same instead of editing function itself

#using functions
```
def memoize(f):
    memo = {}
    def helper(x):            #1st,3rd
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    
@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)  # 2nd

print(fib(4))
```
#Using classes:
```
class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
	    self.memo[args] = self.fn(*args)
        return self.memo[args]

@Memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```
