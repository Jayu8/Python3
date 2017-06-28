class Bank():                      # let's create a bank, building ATMs
    crisis = False
    def create_atm(self):
        while not self.crisis:
           yield "$100"
           
>>> hsbc = Bank()                           # when everything's ok the ATM gives you as much as you want
>>> corner_street_atm = hsbc.create_atm()   # Catch hold of function
>>> print(corner_street_atm.next())
$100
>>> print(corner_street_atm.next())
$100
>>> print([corner_street_atm.next() for cash in range(5)])
['$100', '$100', '$100', '$100', '$100']


>>> hsbc.crisis = True                     # crisis in bank--> no more money!
>>> print(corner_street_atm.next())
<type 'exceptions.StopIteration'>

>>> wall_street_atm = hsbc.create_atm()    # Build a new ATM  -->  still problem 
>>> print(wall_street_atm.next())
<type 'exceptions.StopIteration'>

>>> hsbc.crisis = False                     # Remove crisis from bank --> ATM remains empty
>>> print(corner_street_atm.next())
<type 'exceptions.StopIteration'>

>>> brand_new_atm = hsbc.create_atm()       # build a new  ATM again  -->to get back in business
>>> for cash in brand_new_atm:
...    print cash
$100
$100
$100
$100
$100
$100
$100
$100
$100
...
