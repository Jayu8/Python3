**Function names are references to functions and that we can assign multiple names to the same function:<br>**
```
def succ(x):
    return x + 1 
successor = succ
successor(10)
>>>11
succ(10)
>>>11
```
Here we can delete **either** "succ" **or** "successor" without deleting the function itself. <br>

**Functions inside Functions**<br>
```
def temperature(t):
    def celsius2fahrenheit(x):
        return 9 * x / 5 + 32    
    result = "It's " + str(celsius2fahrenheit(t)) + " degrees!"
    return result
print(temperature(20))
>>>It's 68.0 degrees!
```
**Functions as Parameters**<br>
**As every parameter of a function is a reference to an object** and **functions are objects as well** in python<br>
**We can pass functions - or better "references to functions" - as parameters to a function.**<br>
```
def foo(func):
    print("The function " + func.__name__ + " was passed to foo")
    res = 0
    for x in [1, 2, 2.5]:
        res += func(x)
    return res
print(foo(math.sin))
print(foo(math.cos))
>>> 
The function sin was passed to foo<br>
2.3492405557375347
The function cos was passed to foo<br>
-0.6769881462259364
```
**Functions returning Functions**<br>
**The output of a function is also a reference to an object.Therefore functions can return references to function objects**<br>
```
def f(x):
    def g(y):
        return y + x + 3 
    return g
nf1 = f(1)      #calls f returns g
nf2 = f(3)      #calls f returns g
print(nf1(1))   #calls g returns '5'
print(nf2(1))   #calls g returns '7
```


