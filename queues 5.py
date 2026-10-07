class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert_front(self, value):
        new_node = Node(value)
        new_node.next = self.front
        if self.front is not None:
            self.front.prev = new_node
        else:
            self.rear = new_node
        self.front = new_node

    def insert_rear(self, value):
        new_node = Node(value)
        new_node.prev = self.rear
        if self.rear is not None:
            self.rear.next = new_node
        else:
            self.front = new_node
        self.rear = new_node

    def display(self):
        current = self.front
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


deque = Deque()

deque.insert_rear(10)
deque.insert_rear(20)
deque.insert_front(5)
deque.insert_rear(30)

deque.display()