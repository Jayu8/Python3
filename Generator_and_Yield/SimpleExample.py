def isPrimeNumber(n):                           # LOGIC
    print "isPrimeNumber({}) call".format(n)
    if n==1:
        return False
    for x in range(2,n):                        #ALL NUMBERS
        if n % x == 0:
            return False
    return True



def primes (n=1):                              # DEFAULT VALUE = 1
    while(True):
        print "loop step ---------------- {}".format(n)
        if isPrimeNumber(n): yield n                    #INFINITE LOOP COMES OUT AFTER YIELD
        n += 1

for n in primes():                            #******* yield value always return to VARIABLE in FOR loop ('n' here) ******
    if n> 10:break
    print "wiriting result {}".format(n)      #INFINITE LOOP EXITS THE PROGRAM  AFTER BREAK
