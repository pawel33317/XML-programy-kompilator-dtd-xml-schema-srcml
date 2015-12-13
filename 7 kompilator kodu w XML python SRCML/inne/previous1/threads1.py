import threading,time
message = 0

class producent(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        global message
        print "Start producenta"
        while self.counter: 
            message+=10
            time.sleep(2)
            self.counter -=1
        print "Koniec producenta"

class konsument(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        global message
        print "Start konsumenta"
        while self.counter: 
            print message
            time.sleep(1)
            self.counter -=1
        print "Koniec konsumenta"

# Create new threads
thread1 = producent(1, "Thread-1", 4)
thread2 = konsument(2, "Thread-2", 4)

# Start new Threads
thread1.start()
thread2.start()

print "Exiting Main Thread"
