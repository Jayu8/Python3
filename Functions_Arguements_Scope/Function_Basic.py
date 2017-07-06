########Syntax:
def function-name(Parameter list):
    statements, i.e. the function body
########optional parameters
def Hello(name="everybody"):
    """ Greets a person """
    print("Hello " + name + "!")
Hello("Peter")
Hello()
The output looks like this =>
Hello Peter!
Hello everybody!
#########Docstring Syntax: FunctionName.__doc__ 
def Hello(name="everybody"):
    """ Greets a person """
    print("Hello " + name + "!")

print("The docstring of the function Hello: " + Hello.__doc__)
The output: 
The docstring of the function Hello:  Greets a person 
##########Keyword Arguements############################
def sumsub(a, b, c=0, d=0):
    return a - b + c - d

print(sumsub(12,4))
print(sumsub(42,15,d=10))   => print(sumsub(42,15,0,10))  here 'd'is keyword arguement
#########Arbitrary number of Arguements###############
#Sometimes cant tell how many parameters needed
# An arbitrary parameter number can be accomplished in Python with so-called tuple references.
#An asterisk "*" is used in front of the last parameter name to denote it as a tuple reference
def arithmetic_mean(first, *values):
    """ This function calculates the arithmetic mean of a non-empty
        arbitrary number of numerical values """

    return (first + sum(values)) / (1 + len(values))

print(arithmetic_mean(45,32,89,78))
print(arithmetic_mean(8989.8,78787.78,3453,78778.73))
#When we have to send a list
x = [3, 5, 9]
arithmetic_mean(*x)  #adding star works making it a tuple reference for the function
##########Arbitrary Number of Keyword Parameters#############
#It is also possible to pass an arbitrary number of keyword parameters to a function.Syntax: "**" 
>>> def f(**kwargs):
...     print(kwargs) 
>>> f()
{}
>>> f(de="German",en="English",fr="French")
{'fr': 'French', 'de': 'German', 'en': 'English'}
# Use case 2
>>> def f(a,b,x,y):
...     print(a,b,x,y)
>>> d = {'a':'append', 'b':'block','x':'extract','y':'yes'}
>>> f(**d)
('append', 'block', 'extract', 'yes')








