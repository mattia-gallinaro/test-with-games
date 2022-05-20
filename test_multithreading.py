from concurrent.futures import thread
import threading
import time

class myThread(threading.Thread):
    def __init__(self, threadID, name , delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        print ("Starting :" + self.name)
        threadlock.acquire()
        print_name(self.name, self.delay, 3)
        threadlock.release()


def print_name(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s : %s ", threadName, time.ctime(time.time()))
        counter -= 1

threadlock = threading.Lock()
threads = []

thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for i in threads:
    i.join()
print("Finished")
