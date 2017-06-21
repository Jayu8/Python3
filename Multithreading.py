import thread
import time

 # Define a function for the thread
def print_time( threadName, delay):
    count = 0
    while count < 5:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time())

 # Create two threads as follows
try:
    thread.start_new_thread( print_time, ("Thread-1", 1,)) #delay by 1s
    thread.start_new_thread( print_time, ("Thread-2", 2,))
except:
    print "Error: unable to start thread" 

#Main thread remains until threads-1 and 2  exit
while 1:
    pass

"""
Output:
Thread-1: Wed Jun 21 12:16:48 2017
Thread-2: Wed Jun 21 12:16:49 2017
Thread-1: Wed Jun 21 12:16:49 2017
Thread-1: Wed Jun 21 12:16:50 2017
Thread-2: Wed Jun 21 12:16:51 2017
Thread-1: Wed Jun 21 12:16:51 2017
Thread-1: Wed Jun 21 12:16:52 2017
Thread-2: Wed Jun 21 12:16:53 2017
Thread-2: Wed Jun 21 12:16:55 2017
Thread-2: Wed Jun 21 12:16:57 2017
"""
