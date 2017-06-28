>>> def f():
...   yield 1   # FREEZES goes to i and PRINTS 1 
...   yield 2   # COMES BACK HERE(CONTINUES EXECUTION) when it goes to 'g' in for loop 
...   yield 3   #
... 
>>> g = f()      # creating generator object
>>> for i in g:  # for every g the program continues execution where it left off
...   print i
... 
1
2
3

>>> for i in g:
...   print i
... 
>>> # This time nothing was printed as can only do once in generator
