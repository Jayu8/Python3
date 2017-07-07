**Function names are references to functions and that we can assign multiple names to the same function:<br>**
>>> def succ(x):<br>
     return x + 1 <br>
>>> successor = succ<br>
>>> successor(10)<br>
11<br>
>>> succ(10)<br>
11<br>
The next important fact is that we can delete **either** "succ" **or** "successor" without deleting the function itself. <br>
**Functions inside Functions**<br>
def temperature(t):<br>
    def celsius2fahrenheit(x):<br>
        return 9 * x / 5 + 32<br>
        
    result = "It's " + str(celsius2fahrenheit(t)) + " degrees!" <br>
    return result<br>
print(temperature(20))<br>
>>It's 68.0 degrees!<br>
**Functions as Parameters**<br>

**As every parameter of a function is a reference to an object** and **functions are objects as well** in python<br>
**We can pass functions - or better "references to functions" - as parameters to a function.**<br>

def foo(func):<br>
    print("The function " + func.__name__ + " was passed to foo")<br>
    res = 0<br>
    for x in [1, 2, 2.5]:<br>
        res += func(x)<br>
    return res<br>
print(foo(math.sin))<br>
print(foo(math.cos))<br>
>>> <br>
The function sin was passed to foo<br>
2.3492405557375347<br>
The function cos was passed to foo<br>
-0.6769881462259364<br>

**Functions returning Functions**<br>
**The output of a function is also a reference to an object.Therefore functions can return references to function objects**<br>
def f(x):<br>
    def g(y):<br>
        return y + x + 3 <br>
    return g<br><br>
nf1 = f(1)      #calls f returns g<br>
nf2 = f(3)      #calls f returns g<br>
print(nf1(1))   #calls g returns '5'<br>
print(nf2(1))   #calls g returns '7'<br>


