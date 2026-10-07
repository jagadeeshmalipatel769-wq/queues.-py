class BoundedQueue:
    def __init__(self, capacity):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def enqueue(self, value):
        if self.is_full():
            print(f"Queue overflow, cannot enqueue {value}")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.arr[self.rear] = value
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow, cannot dequeue")
            return None
        value = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return value


queue = BoundedQueue(3)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
queue.dequeue()