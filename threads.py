import threading
import time


class MyThread(threading.Thread):
    def __init__(self, id, name, delay, counter):
        super().__init__(self)
        self.name = name
        self.delay = delay
        self.id = id
        self.counter = counter

    def run(self):
        print('start thread: ' + self.name)
        while self.counter > 0:
            time.sleep(self.delay)
            print('{}: {}'.format(self.name, time.ctime(time.time())))
            self.counter -= 1
        print('finished thread: ' + self.name)


thread1 = MyThread(1, 'Th1', 1, 5)
thread2 = MyThread(2, 'Th2', 1, 5)
