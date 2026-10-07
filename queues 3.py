class CircularQueue:
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
            print("Queue overflow")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.arr[self.rear] = value
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow")
            return None
        value = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return value


queue = CircularQueue(5)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())

queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)

print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())