from collections import deque
import time
import threading


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, value):
        self.buffer.appendleft(value)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


pq = Queue()


def place_orders(orders):
    for order in orders:
        print("Now serving: ", order)
        pq.enqueue(order)
        time.sleep(0.5)


def serve_orders():
    time.sleep(1)
    while 1:
        if not pq.is_empty():
            order = pq.dequeue()
            print("Now serving the order: ", order)
            time.sleep(2)
        else:
            print("No more orders!")
            break


orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
t1 = threading.Thread(target=place_orders, args=(orders, ))
t2 = threading.Thread(target=serve_orders)

t1.start()
t2.start()
