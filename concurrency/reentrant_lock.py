###---------------------- RE-ENTRANT CODE ----------------------###

# A Re-entrant code is fully atomic in the sense - it does not modify any object outside of its scope.

def pow(num):
    return num*num

# Non Re-entrant code
# Not thread safe without an explicit lock
k = 10
def pow1(num):
    global k 
    k +=1
    return num*num

###---------------------- RE-ENTRANT LOCK ----------------------###

# Ability of a thread to re-acquire lock in something it already had (locked)

from threading import *

lock = Lock()
k = lock.acquire()
print("first locked {}".format(k))
k = lock.acquire(timeout=0)
print("second locked {}".format(k))
lock.release()

# first locked True
# second locked False

from threading import *

lock = RLock()
k = lock.acquire()
print("first locked {}".format(k))
k = lock.acquire()
print("second locked {}".format(k))
lock.release()

# first locked True
# second locked True
