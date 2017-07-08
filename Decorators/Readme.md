Decorator in Python is a callable Python object that is used to modify a function, method or class definition. <br>
The original object, the one which is going to be modified, is passed to a decorator as an argument. <br>
The decorator returns a modified object, e.g. a modified function, which is bound to the name used in the definition.<br>
``` Simple example
def our_decorator(func):  #Takes function
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper  #Function wrapper     =>our_decorator(func)((function_wrapper(x)))  
def foo(x):
    print("Hi, foo has been called with " + str(x))
print("We call foo before decoration:")
foo("Hi")                                #Normal function
print("We now decorate foo with f:")
foo = our_decorator(foo)                #Decorated function ## Important reference to 'function_wrapper'
print("We call foo after decoration:")
foo()   # 'foo' goes to 'func' in 'our_decorator' and '42' goes in 'x' in  'function_wrapper'  func(x)
```
output:
```
We call foo before decoration:
Hi, foo has been called with Hi
We now decorate foo with f:
We call foo after decoration:
Before calling foo
Hi, foo has been called with 42
After calling foo
```
**The Usual Syntax for Decorators in Python:**  **@our_decorator** instead of **foo = our_decorator(foo)**<br>
**This line has to be directly positioned in front of the decorated function<br>** This is a proper example compared to above
```
def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))
foo("Hi")
```
**We can decorate every other function** which takes **one parameter(for this case)** by placing @our_decorator infront of that function  <br>
It is also possible to **decorate third party functions**, e.g. functions we import from a module by **foo = our_decorator(foo)** instead of **@our_decorator**
