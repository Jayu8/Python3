**All the terms here orifinated from functional programming language** <br>
**LAMBDA**<br>
**Syntax:** lambda argument_list: expression <br>

The lambda operator or lambda function is a way to create small anonymous functions, i.e. functions without a name.<br>
These functions are throw-away functions, i.e. they are just needed where they have been created.<br>
Lambda functions are mainly used in combination with the functions filter(), map() and reduce().<br>


**MAP**<br>
**Syntax:** map(func, seq)    <br>
The first argument func is the name of a function and the second a sequence (e.g. a list) <br>
seq. map() applies the function func to all the elements of the sequence seq. <br>

**FILTER**<br>
**Syntax:** filter(function, sequence)<br>
The function filter(f,l) needs a function f as its first argument. f has to return a Boolean value, i.e. either True or False.<br>
This function will be applied to every element of the list l.<br>
Only if f returns True will the element be produced by the iterator, which is the return value of filter<br>

**REDUCE**<br>
**Syntax:** reduce(func, seq)   <br>
If seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) works like this:<br>
At first the first two elements of seq will be applied to func, i.e. func(s1,s2) <br>
The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ] <br>
In the next step func will be applied on the previous result and the third element of the list, i.e. func(func(s1, s2),s3)<br>
The list looks like this now: [ func(func(s1, s2),s3), ... , sn ] <br>
Continue like this until just one element is left and return this element as the result of reduce()<br>
