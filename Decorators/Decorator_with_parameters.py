We define two decorators in the following code: 

def evening_greeting(func):
    def function_wrapper(x):
        print("Good evening, " + func.__name__ + " returns:")
        func(x)
    return function_wrapper

def morning_greeting(func):
    def function_wrapper(x):
        print("Good morning, " + func.__name__ + " returns:")
        func(x)
    return function_wrapper

@greeting("Good  Morning")  ########if evening must define a new decorator########### 
def foo(x):
    print(42)
    
foo("hi")

These two decorators are nearly the same, except for the greeting. 
We want to add a parameter to the decorator to be capable of customizing the greeting, when we do the decoration.
We have to wrap another function around our previous decorator function to accomplish this.

def greeting(expr):
    def greeting_decorator(func):
        def function_wrapper(x):
            print(expr + ", " + func.__name__ + " returns:")
            func(x)
        return function_wrapper
    return greeting_decorator

@greeting("Good  Morning")   ######just change parameter to "Good  Evening"
def foo(x):
    print(42)

###### define usinng the normal way instead of  '@'######
greeting2 = greeting("καλημερα")
foo = greeting2(foo)
foo("Hi")
