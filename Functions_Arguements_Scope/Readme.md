Parameters are inside functions or procedures     def fun(a, b) -> parameters <br>
Arguments are used in procedure calls, i.e. the values passed to the function at run-time. x=fun(a,b) -> arguements <br>
**How the arguments from a function call are passed to the parameters of the function?**<br>
** 1.Call by Value (does not affect arguements when changed in function) <br>
2.Call by reference (affects argements as memory is referenced) ** <br>
Python uses Call by reference initially to save memory <br>
and switches to call by value when the arguement is about to be modified in the function <br>
To avoid things happening in function to reflect in the caller arguements use shallow or deep copy <br><br>

Variable arguements that is * and * * are used in both function calls and functions
