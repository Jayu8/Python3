A function with yield, when called, returns a Generator object.<br>
Generators are iterators because they implement the iterator protocol, so you can iterate over them.<br>
As the generator object implements __iter__ and __next__ and as such can be used in for loops like any object that supports iteration.<br> 

In Python's Generators, the execution of the code is frozen at the point of the yield.<br>
When the generator is called  execution resumes and then freezes at the next yield.<br>

By "frozen" we mean that all local state is retained,<br>
including the current bindings of local variables, the instruction pointer, and the internal evaluation stack: enough information is saved so that the next time .next() is invoked, the function can proceed exactly as if the yield statement were just another external call
