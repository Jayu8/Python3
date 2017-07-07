"""
Recursion -Calls to itself
STACK(CALL funcion) and RETURN are very important for these find of problems.
Draw tree (left to right trace)
Try to realise mathematically (that is is it relying on past results?)
"""
def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)   # 1st
        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res	#2nd
print(factorial(5))
####

Stack (1st      Return (2nd)     
--                 1
res=2*fact(1)   res= 2*1  
res=3*fact(2)   res= 3*2*1
res=4*fact(3)   res= 4*3*2*1
res=5*fact(4)   res= 5*4*3*2*1

#### Math
fact(5)=5*fact(4) => fact(5)=5*f(4*fact(3)) and so on till initilaisation (return =1)

###########This Python script outputs the following results: 
factorial has been called with n = 5
factorial has been called with n = 4
factorial has been called with n = 3
factorial has been called with n = 2
factorial has been called with n = 1
intermediate result for  2  * factorial( 1 ):  2
intermediate result for  3  * factorial( 2 ):  6
intermediate result for  4  * factorial( 3 ):  24
intermediate result for  5  * factorial( 4 ):  120
120
