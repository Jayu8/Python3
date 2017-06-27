#Basic
for element in [1, 2, 3]:
    print(element)
"""
Behind the scenes, the for statement calls iter() on the container object. 
The function returns an iterator object that defines the method __next__() which accesses elements in the container one at a time. 
When there are no more elements, __next__() raises a StopIteration exception which tells the for loop to terminate. 
"""
s = 'cat'      # s is an ITERABLE
                   # s is a str object that is immutable
                   # s has no state
                   # s has a __getitem__() method 

t = iter(s)     # t is an ITERATOR    ****this was called internally in above example
                   # t has state (it starts by pointing at the "c"
                   # t has a next() method and an __iter__() method

next(t)        # the next() function returns the next value and advances the state
'c'
next(t)        # the next() function returns the next value and advances
'a'
next(t)        # the next() function returns the next value and advances
't'
 next(t)        # next() raises StopIteration to signal that iteration is complete
Traceback (most recent call last):
...
StopIteration

iter(t) is t   # the iterator is self-iterable
""""
An iterable is a object which has a __iter__() method.
It can possibly iterated over several times, such as list()s and tuple()s.It returns an iterator object
An iterator is the object which iterates. 
It is returned by an __iter__() method, returns itself via its own __iter__() method and has a __next()__ method.
Iteration is the process of calling this __next__() until it raises StopIteration
"""
