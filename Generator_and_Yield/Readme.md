A function with yield, when called, returns a Generator.<br>
Generators are iterators because they implement the iterator protocol, so you can iterate over them.<br>
A generator can also be sent information, making it conceptually a coroutine.<br>
You can delegate from one generator to another in both directions with yield from.<br>

The idea for generators comes from other languages with varying implementations. <br>
In Python's Generators, the execution of the code is frozen at the point of the yield.<br>
When the generator is called  execution resumes and then freezes at the next yield.<br>

yield provides an easy way of implementing the iterator protocol, defined by the following two methods:<br>
__iter__ and __next__ <br>
Both of those methods make an object an iterator that you could type-check with the Iterator Abstract Base Class from the collections module.
