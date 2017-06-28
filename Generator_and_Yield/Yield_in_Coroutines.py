"""
Coroutines are computer program components that generalize subroutines for non-preemptive multitasking,
by allowing multiple entry points for suspending and resuming execution at certain locations.
Coroutines are well-suited for implementing more familiar program components such as 
cooperative tasks, exceptions, event loops, iterators, infinite lists and pipes.
"""
When subroutines are invoked, execution begins at the start, and once a subroutine exits, it is finished; 
an instance of a subroutine only returns once, and does not hold state between invocations. 
coroutines can exit by calling other coroutines, 
which may later return to the point where they were invoked in the original coroutine;it is not exiting but calling another coroutine
EX: PRODUCER AND COMNSUMER PROBLEM
"""


def bank_account(deposited, interest_rate):
    while True:                                             #infinite loop ,comes out only when yield is executed.
        calculated_interest = interest_rate * deposited 
        received = yield calculated_interest             #yield is calculated and returned. 
        if received:                                     #recieved comes into picture when send is used 
            deposited += received                        # after this statement goes to while true

my_account = bank_account(1000, .05) # calling function
first_year_interest = next(my_account)
print first_year_interest
next_year_interest = my_account.send(first_year_interest + 1000)  # send function goes to recieved variable
print next_year_interest
