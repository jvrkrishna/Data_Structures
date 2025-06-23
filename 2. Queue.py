#Queue Data Structure
'''A queue is a useful data structure in programming. It operates similarly to a ticket queue outside a cinema hall, where the first person to enter the queue is the first one to receive a ticket.

A queue follows the First In, First Out (FIFO) principle, meaning the first item that enters the queue is the first one to leave.

FIFO Representation of Queue:
In the image above, since 1 was added to the queue before 2, it will be the first to be removed from the queue. This demonstrates the FIFO principle.

In programming terms:

Enqueue refers to adding items to the queue.

Dequeue refers to removing items from the queue.'''

#Queue Implementation in Python (Using List)
queue = []  # Initial empty queue

# Adding elements to the queue (enqueue)
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after enqueue operations:", queue)

# Removing elements from the queue (dequeue)
queue.pop(0)  # Remove the first element (FIFO behavior)
queue.pop(0)  # Remove the next element

print("Queue after dequeue operations:", queue)

#Checking if the Queue is Empty
queue = []  # Initial empty queue
print(len(queue) == 0)  # Returns True if the queue is empty
print(not queue)        # Also returns True if the queue is empty

#Displaying the Front Element of the Queue
queue.append(10)
queue.append(20)

# Displaying the front element (First element in the queue)
print("Front element of the queue:", queue[0])

#Queue Implementation in Python (Interactive)
#Here’s a simple interactive implementation where users can enqueue and dequeue elements:

queue = []  # Initial empty queue

# Enqueue operation
def enqueue():
    element = input("Enter the element to enqueue: ")
    queue.append(element)
    print("Queue after enqueue:", queue)

# Dequeue operation
def dequeue():
    if not queue:
        print("Queue is empty!")
    else:
        e = queue.pop(0)  # Remove the first element (FIFO)
        print(f"Removed element: {e}")
        print("Queue after dequeue:", queue)

# Main interactive loop
while True:
    print("Select an operation: 1. Enqueue  2. Dequeue  3. Quit")
    choice = int(input())
    
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        break
    else:
        print("Please select a valid operation!")
        
'''

🧱 Types of Queues in Python
1.	Queue (FIFO)
2.	LifoQueue (Stack behavior)
3.	PriorityQueue (Based on priority)
4.	Deque (Double-ended queue)

✅ Basic Queue Operations
Operation	          Description
enqueue()	          Add item to the rear of the queue
dequeue()	          Remove item from the front of queue
isEmpty()	          Check if the queue is empty
size()	              Returns the number of items
peek()	              View the front item without removing

when using collections.deque, you can append and pop from both the front and the rear of the queue. That's what makes deque (pronounced "deck") so powerful—it’s a double-ended queue.
'''

#🧠 Summary:
'''
| Operation    | Method         | Description           |
| ------------ | -------------- | --------------------- |
| Append right | `append()`     | Add to the end        |
| Append left  | `appendleft()` | Add to the front      |
| Pop right    | `pop()`        | Remove from the end   |
| Pop left     | `popleft()`    | Remove from the front |
'''

#🧱 1. Queue (FIFO - First In First Out)--From queue module.
from queue import Queue

q = Queue()
q.put(1)  # Enqueue
q.put(2)
q.put(3)

print(q.get())  # Dequeue -> 1
print(q.get())  # -> 2


#🧱 2. LifoQueue (Stack behavior - Last In First Out)--Also from queue module.
from queue import LifoQueue

q = LifoQueue()
q.put('A')  # Push
q.put('B')
q.put('C')

print(q.get())  # Pop -> 'C'
print(q.get())  # -> 'B'

#🧱 3. PriorityQueue (Based on priority)--From queue module. Smaller numbers = higher priority.
from queue import PriorityQueue

pq = PriorityQueue()
pq.put((2, "code"))      # (priority, value)
pq.put((1, "eat"))
pq.put((3, "sleep"))

print(pq.get())  # -> (1, 'eat')
print(pq.get())  # -> (2, 'code')

#🧱 4. Deque (Double-ended queue)--From collections module. Can add/remove from both ends.
from collections import deque

dq = deque()
dq.append(10)        # Add to right
dq.appendleft(5)     # Add to left
dq.append(15)

print(dq.pop())      # Remove from right -> 15
print(dq.popleft())  # Remove from left -> 5

#Another Example deque
#1. Using collections.deque 
from collections import deque

# Create a queue
queue = deque()

# Enqueue
queue.append("A")
queue.append("B")
queue.append("C")

print("Queue after enqueuing:", queue)

# Dequeue
print("Dequeued:", queue.popleft())
print("Queue after dequeuing:", queue)

# Peek
print("Front element:", queue[0])

# Check if empty
print("Is queue empty?", len(queue) == 0)
print("Is queue empty?", not queue)

