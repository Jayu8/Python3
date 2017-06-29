# LAMBDA
sum = lambda x, y : x + y
>>>sum(3,4)
>>>7
# MAP
>>> C = [39.2, 36.5, 37.3, 38, 37.8] 
>>> F = list(map(lambda x: (float(9)/5)*x + 32, C))   # x means each element 
>>> print(F)
[102.56, 97.7, 99.14, 100.4, 100.03999999999999]
>>> C = list(map(lambda x: (float(5)/9)*(x-32), F))
>>> print(C)
[39.2, 36.5, 37.300000000000004, 38.00000000000001, 37.8]
#can be applied to two 
>>> a = [1,2,3,4]
>>> b = [17,12,11,10]
>>> c = [-1,-4,5,9]
>>> list(map(lambda x,y:x+y, a,b))
[18, 14, 14, 14]
# FILTER
>>> fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
>>> odd_numbers = list(filter(lambda x: x % 2, fibonacci))
>>> print(odd_numbers)
[1, 1, 3, 5, 13, 21, 55]
#REDUCE
>>> from functools import reduce
>>> f = lambda a,b: a if (a > b) else b
>>> reduce(f, [47,11,42,102,13])
102
