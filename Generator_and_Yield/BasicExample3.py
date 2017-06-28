

def coroutine():
     i = -1
     while True:
         i += 1
         val = (yield i)
         print("Received %s" % val)

sequence = coroutine()

sequence.next()
>>0                 # from yield

sequence.next()        #********NEXT sends NONE  into VAL******
>>Received None        # from val
>>1                    #from yield

sequence.send('hello') #******SEND sends VALUE('hello')  into VAL*****
>>Received hello       # from yield
>>2                    # from val

sequence.close()
