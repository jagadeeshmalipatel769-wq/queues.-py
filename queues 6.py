class PriorityQueue:
    def __init__(self):
        self.tasks = []

    def insert(self, name, priority):
        self.tasks.append((name, priority))

    def extract_max(self):
        max_index = 0
        for i in range(1, len(self.tasks)):
            if self.tasks[i][1] > self.tasks[max_index][1]:
                max_index = i
        return self.tasks.pop(max_index)

    def is_empty(self):
        return len(self.tasks) == 0


queue = PriorityQueue()

queue.insert("Sprained ankle", 2)
queue.insert("Chest pain", 9)
queue.insert("Minor cut", 1)
queue.insert("Broken arm", 6)

while not queue.is_empty():
    name, priority = queue.extract_max()
    print(f"Treating: {name} (priority {priority})")