'''
Queue Data Structure

A queue is a useful data structure in programming. It is similar to the ticket queue outside a cinema hall, where the first person entering the queue is the first person who gets the ticket.

Queue follows the First In First Out (FIFO) rule - the item that goes in first is the item that comes out first.
FIFO Representation of Queue
In the above image, since 1 was kept in the queue before 2, it is the first to be removed from the queue as well. It follows the FIFO rule.

In programming terms, putting items in the queue is called enqueue, and removing items from the queue is called dequeue.
'''

# Queue implementation in python list
queue=[]
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)
queue.pop()
queue.pop()
print(queue)

#To know the queue is empty or not
queue=[]
print(len(queue))==0
print(not queue)

queue.append(10)
queue.append(20)
print(queue[-1])

##queue implementation in python list
queue=[]
def enqueue():
    element = input("Enter the element:")
    queue.append(element)
    print(queue)

def dequeue():
    if not queue:
        print("queue is empty!")
    else:
        e = queue.pop()
        print("removed element:",e)
        print(queue)

while True:
    print("Select the operation 1. enqueue 2.dequeue 3.quit")
    choice = int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        break
    else:
        print("Enter the correct operation!")
        
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

