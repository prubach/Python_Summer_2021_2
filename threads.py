import threading
import time


class MyThread(threading.Thread):
    def __init__(self, id, name, delay, counter, shared_list):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
        self.id = id
        self.counter = counter
        self.result = 0
        self.shared_list = shared_list

    def run(self):
        print('start thread: ' + self.name)
        while self.counter > 0:
            time.sleep(self.delay)
            print('{}: {}'.format(self.name, time.ctime(time.time())))
            self.counter -= 1
            self.result += self.id
            self.shared_list.append(self.name + '-' + str(self.counter))
        print('finished thread: ' + self.name)


    def get_result(self):
        return self.result

shared_list = []

thread1 = MyThread(1, 'Th1', 1, 5, shared_list)
thread2 = MyThread(2, 'Th2', 1.5, 5, shared_list)
thread3 = MyThread(3, 'Th3', 1.5, 5, shared_list)

# Sequentially
#thread1.run()
#thread2.run()

# Run in parallel
#thread1.start()
#thread2.start()

all_thread = [thread1, thread2, thread3]
for th in all_thread:
    th.start()
print('Threads started')


for th in all_thread:
    th.join()
for th in all_thread:
    print('{}: {}'.format(th.name, th.get_result()))
print(shared_list)
print('My program is finished')
