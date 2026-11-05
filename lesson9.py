#Demo 1A
import _thread
import time

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % ( threadName, time.ctime(time.time()) ))

try:
    _thread.start_new_thread ( print_time, ("Thread-1", 2, ) )
    _thread.start_new_thread ( print_time, ("Thread-2", 4, ) )
except:
    print("Error: unable to start thread")
c = input("Type something to quit\n")


#Demo 1B
import time
from threading import Thread
def sleeper(i):
    print("thread %d sleeps for 5 seconds" % i)
    time.sleep(5)
    print( "thread %d woke up" % i)

for i in range(10):
    t = Thread(target=sleeper, args=(i,))
    t.start()


#Demo 1C
import threading
import datetime

class myThread (threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter 

    def printDate(self, threadName, counter):
        datefields = []
        today = datetime.date.today()
        datefields.append(today)
        print("%s[%d]: %s" % ( threadName, counter, datefields[0] ))

    def run(self):
        print("Starting " + self.name)
        myThread.printDate(0, self.name, self.counter)
        print("Exiting " + self.name)

thread1 = myThread("Thread", 1)
thread2 = myThread("Thread", 2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exiting the program!!")


#Demo 2
import threading
import datetime
class myThread (threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        threadLock.acquire()        #acquire lock to synchronize thread
        myThread.print_date(0,self.name, self.counter)
        threadLock.release()        #release lock for the next thread
        print("Exiting " + self.name)
    def print_date(self,threadName,counter):
        datefields = []
        today = datetime.date.today()
        datefields.append(today)
        print("%s[%d]: %s" % ( threadName, counter, datefields[0] ))

threadLock = threading.Lock()
threads = []

thread1 = myThread("Thread", 1)
thread2 = myThread("Thread", 2)
thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()
print("Exiting the Program!!!")