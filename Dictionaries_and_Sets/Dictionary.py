"""
English to germany dictionary
"""
en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"} #define
print(en_de)  # print dictionary
print(en_de["red"]) # print meaning of red in germany
"""
Keys cant be mutable
"""
>>> dic = { [1,2,3]:"abc"}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list objects are unhashable
"""
Tuples are okay
"""
>>> dic = { (1,2,3):"abc", 3.1415:"abc"}
>>> dic
{3.1415: 'abc', (1, 2, 3): 'abc'}
"""
pop in dictionary used with key pop("key"), in list were used as stack pop()
"""
Ex: dict.pop("red")
"""
List to Dictionary Conversion  - returns iterator
"""
>>> l1 = ["a","b","c"]
>>> l2 = [1,2,3]
>>> c = zip(l1,l2)
>>> z1 = list(c)
>>> z2 = list(c)
>>> print(z1)
[('a', 1), ('b', 2), ('c', 3)]
>>> print(z2)
[]
"""
Dictionary to List Conversion
"""
>>> w = {"house":"Haus", "cat":"", "red":"rot"}
>>> items_view = w.items()
>>> items = list(items_view)
>>> items
[('house', 'Haus'), ('cat', ''), ('red', 'rot')]
