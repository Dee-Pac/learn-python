from threading import Thread, Lock, RLock, current_thread


###---------------------- Thread & Lock ----------------------###

class Counter:
    def __init__(self,counter=0):
        self.counter = counter
        self.lock = Lock()

    def count(self):
        with self.lock:
            # self.lock.acquire() # Alternate for with lock:
            print(current_thread().getName(),self.counter)
            for k in range(100000):
                self.counter +=1
            # self.lock.release()

# initiate counter object
obj = Counter()

# initiate threads
threads = []

# create 40 threads for count function
for k in range(40):
    new_thread = Thread(target = obj.count,args = ())
    threads.append(new_thread)

# start the threads
for thread in threads:
    thread.start()

# wait for completion of all threads
for thread in threads:
    thread.join()

# Without above join calls, the print could execute even before all the counter functions completed.
print(obj.counter)
