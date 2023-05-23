import threading
import queue
import time
import random


class Task:
    def __init__(self, priority, timesleep):
        self.timesleep = timesleep
        self.priority = priority

    def __repr__(self):
        time.sleep(self.timesleep)
        return f'Task(priority={self.priority}). sleep({self.timesleep})'

    def __lt__(self, other):
        return self.priority < other.priority


class Producer(threading.Thread):
    def __init__(self, queue, count):
        super().__init__()
        self.queue = queue
        self.count = count
        print('Producer: Running')

    def run(self):
        for _ in range(self.count):
            sleeptime = random.random()
            priority = random.randint(0, 6)
            task = Task(priority, sleeptime)
            self.queue.put((priority, task))
        consumer = Consumer(self.queue, self.count)
        consumer.start()
        consumer.join()
        print('Producer: Done')


class Consumer(threading.Thread):
    def __init__(self, queue, count):
        super().__init__()
        self.queue = queue
        self.tasks = 0
        self.count = count
        print('Consumer: Running')

    def run(self):
        while True:
            try:
                priority, task = self.queue.get()
            except queue.Empty:
                continue
            print(f'>running {task}')
            self.queue.task_done()
            self.tasks += 1
            if self.tasks == self.count:
                print('Consumer: Done')
                break


def main():
    priority_queue = queue.PriorityQueue()
    producer = Producer(priority_queue, 10)
    producer.start()
    priority_queue.join()
    producer.join()


if __name__ == '__main__':
    main()
