from collections import deque

customers = deque()

customers.append("Ananya")
customers.append("Karan")
customers.append("Priya")

print("Front of queue:", customers[0])

while customers:
    print("Serving:", customers.popleft())