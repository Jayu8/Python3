"""
It tests the invariants in a code
The goal of using assertions is to let developers find the likely root cause of a bug more quickly. 
An assertion error should never be raised unless there’s a bug in your program.
assert is equivalent to:
if __debug__:
   if not <expression>: raise AssertionError
"""


# Asserts
a = 5
# checks if a = 5
assert(a == 5)
# uncommenting the below code will throw assertion error
#assert(a == 6)

def KelvinToFahrenheit(Temperature):
  assert (Temperature >= 0),"Colder than absolute zero!"
  return ((Temperature-273)*1.8)+32
print KelvinToFahrenheit(273)
print int(KelvinToFahrenheit(505.78))
