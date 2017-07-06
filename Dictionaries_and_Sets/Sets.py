"""
Element wise
"""
>>> x = set("A Python Tutorial")
>>> x
{'A', ' ', 'i', 'h', 'l', 'o', 'n', 'P', 'r', 'u', 't', 'a', 'y', 'T'}
"""
Word wise
"""
>>> x = set(["Perl", "Python", "Java"])
>>> x
{'Python', 'Java', 'Perl'}
"""
Duplicates Removed also tuple is used in  "value" as  immmutable allowed
"""
>>> cities = set(("Paris", "Lyon", "London","Berlin","Paris","Birmingham"))
>>> cities
{'Paris', 'Birmingham', 'Lyon', 'London', 'Berlin'}
"""
Cant make mutable in "value"
"""
>>> cities = set((["Python","Perl"], ["Paris", "Berlin", "London"]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
"""
Mutable sets not "value"
Though sets can't contain mutable objects, sets are mutable: 
"""
>>> cities = set(["Frankfurt", "Basel","Freiburg"])
>>> cities.add("Strasbourg")
>>> cities
{'Freiburg', 'Basel', 'Frankfurt', 'Strasbourg'}
"""
Frozen sets completly immutable
"""
>>> cities = frozenset(["Frankfurt", "Basel","Freiburg"])
>>> cities.add("Strasbourg")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'add'
"""
Set properties like unions , intersections are implemented
"""
