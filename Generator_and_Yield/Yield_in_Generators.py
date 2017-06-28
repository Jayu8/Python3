def func():
     yield 'I am'
     yield 'a generator!'
 
>>> type(func)                 # A function with yield is still a function
<type 'function'>

>>> gen = func()
>>> type(gen)                  # but it returns a generator
<type 'generator'>

>>> hasattr(gen, '__iter__')   # that's an iterable
True
>>> hasattr(gen, 'next')       # and with .next (.__next__ in Python 3)
True                           # implements the iterator protocol.


The generator type is a sub-type of iterator:
>>> import collections, types
>>> issubclass(types.GeneratorType, collections.Iterator)
True

And if necessary, we can type-check like this:
>>> isinstance(gen, types.GeneratorType)
True
>>> isinstance(gen, collections.Iterator)
True

A feature of an Iterator is that once exhausted, you can't reuse or reset it:
>>> list(gen)
['I am', 'a generator!']
>>> list(gen)
[]
You'll have to make another if you want to use its functionality again 
>>> list(func())
['I am', 'a generator!']
One can yield data programmatically, for example:
def func(an_iterable):
    for item in an_iterable:
        yield item
        
The above simple generator is also equivalent to the below :
def func(an_iterable):
    yield from an_iterable
