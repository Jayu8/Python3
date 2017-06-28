>>> def f():
...   yield 1
...   yield 2
...   yield 3
... 
>>> g = f()
>>> for i in g:
...   print i
... 
1
2
3
>>> for i in g:
...   print i
... 
>>> # Note that this time nothing was printed
