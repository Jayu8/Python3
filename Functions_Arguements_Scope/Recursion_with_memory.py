#saved in fibo.py 
#Recursion normal
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
#Iteration
def fibi(n):
    old, new = 0, 1
    if n == 0:
        return 0
    for i in range(n-1):
        old, new = new, old + new
    return new
#Recursion with memory -- here in the 2nd statement memo is stored and used in 3rd statement when the same 'n' occurs 
memo = {0:0, 1:1}
def fibm(n):
    if not n in memo:                   #1st--This is always executed
        memo[n] = fibm(n-1) + fibm(n-2) #2nd-- WHOLE statemnet is kept in stack and fibm(n-1) is executed first
    return memo[n]                     #3rd--This returns already stored values (memory) already calculated

fibm(5) # call individually

#seperate python file
from timeit import Timer
from fibo import fib
t1 = Timer("fib(10)","from fibo import fib")
for i in range(1,41):
	s = "fibm(" + str(i) + ")"
	t1 = Timer(s,"from fibo import fibm")
	time1 = t1.timeit(3)                 #calls each function 3 times
	s = "fibi(" + str(i) + ")"
	t2 = Timer(s,"from fibo import fibi")
	time2 = t2.timeit(3)
	print("n=%2d, fib: %8.6f, fibi:  %7.6f, percent: %10.2f" % (i, time1, time2, time1/time2))
