#Stack: A stack is a linear data structure that follows the principle of Last In First Out (LIFO). This means the last element inserted inside the stack is removed first.
'''
Common Stack Actions (Operations)
Operation	Description
push()	       Adds an element to the top of the stack
pop()	       Removes and returns the top element
peek() / top()	       Returns the top element without removing it
is_empty()	       Checks if the stack is empty
size()	        Returns the number of elements in the stack
 
Working of Stack Data Structure
The operations work as follows:
1.	A pointer called TOP is used to keep track of the top element in the stack.
2.	When initializing the stack, we set its value to -1 so that we can check if the stack is empty by comparing TOP == -1.
3.	On pushing an element, we increase the value of TOP and place the new element in the position pointed to by TOP.
4.	On popping an element, we return the element pointed to by TOP and reduce its value.
5.	Before pushing, we check if the stack is already full
6.	Before popping, we check if the stack is already empty
 
# Stack: A stack is a linear data structure that follows the principle of Last In First Out (LIFO). 
# This means the last element inserted inside the stack is removed first.

# Common Stack Operations:
Operation   | Description
------------|---------------------------------------------------
push()      | Adds an element to the top of the stack
pop()       | Removes and returns the top element
peek()      | Returns the top element without removing it
is_empty()  | Checks if the stack is empty
size()      | Returns the number of elements in the stack

# Working of Stack Data Structure:
The operations work as follows:
1. A pointer called TOP is used to keep track of the top element in the stack. 
   In Python, this can be represented using a simple index, as lists dynamically grow.
2. When initializing the stack, we usually start with an empty stack (or TOP set to -1 if we were using a fixed-size array).
3. On pushing an element, we add it to the list and increase the index (TOP) or simply append to the list.
4. On popping an element, we remove the last element of the list, which is the element pointed to by TOP.
5. For stack operations with a fixed capacity, we would check if the stack is full before pushing a new element. 
   (However, Python's list doesn’t have this limitation by default.)
6. Before popping, we check if the stack is empty (to prevent underflow).
'''

# Stack implementation in Python using list

# Create a stack (empty list)
stack = []

# Push elements onto the stack
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after pushing elements:", stack)

# Pop elements from the stack
stack.pop()
stack.pop()
print("Stack after popping 2 elements:", stack)

# Check if the stack is empty
stack = []
print("Is the stack empty? (len method):", len(stack)==0)
print("Is the stack empty? (not method):", not stack)

#To know the length of the stack
stack=[10,20]
print("Length of the stack:",len(stack))

# Peek the top element
if stack:
    print("Top element in the stack:", stack[-1])
else:
    print("Stack is empty, no top element.")

# --------------------------------------------------------
# Function-based Stack Implementation
def push(stack, item):
    stack.append(item)
    print(f"Pushed item: {item}")
    print("Current stack:", stack)

def pop(stack):
    if not stack:
        print("Stack is empty, cannot pop.")
        return None
    item = stack.pop()
    print(f"Popped item: {item}")
    print("Current stack:", stack)
    return item

def check_empty(stack):
    return len(stack) == 0

# Interactive Stack Operations
def stack_operations():
    stack = []  # Create an empty stack

    while True:
        print("\nSelect the operation:")
        print("1. Push 2. Pop 3. Check if empty 4. Quit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            element = input("Enter the element to push: ")
            push(stack, element)
        elif choice == '2':
            pop(stack)
        elif choice == '3':
            if check_empty(stack):
                print("The stack is empty.")
            else:
                print("The stack is not empty.")
        elif choice == '4':
            print("Exiting stack operations.")
            break
        else:
            print("Invalid input! Please enter a valid operation.")

# Start the stack operations
stack_operations()

# --------------------------------------------------------
# Alternative Stack Operations with Object-Oriented Approach (Optional)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed item: {item}")
        print("Current stack:", self.stack)

    def pop(self):
        if self.is_empty():
            print("Stack is empty, cannot pop.")
            return None
        item = self.stack.pop()
        print(f"Popped item: {item}")
        print("Current stack:", self.stack)
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty, no top element.")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example using the Stack class
stack_obj = Stack()
stack_obj.push(1)
stack_obj.push("hello")
stack_obj.push(3.14)
stack_obj.push(True)

print(f"Top element: {stack_obj.peek()}")
print(f"Stack size: {stack_obj.size()}")

stack_obj.pop()
stack_obj.pop()

print(f"Stack after popping two elements: {stack_obj.stack}")

# -------------------------------------------------------------
# Custom Stack Class in Python
class Stack:
    def __init__(self):
        self.items = []

    # Push an item onto the stack
    def push(self, item):
        self.items.append(item)

    # Pop the top item from the stack
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    # Peek at the top item without removing it
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    # Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Return the size of the stack
    def size(self):
        return len(self.items)

    # Display the stack from top to bottom
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack (top to bottom):")
            for item in reversed(self.items):  # Start from the top element
                print(item)

# Create a stack instance
s = Stack()

# Push elements onto the stack
s.push(10)
s.push(20)
s.push(30)

# Display the stack
s.display()

# Output:
# Stack (top to bottom):
# 30
# 20
# 10

# Peek at the top element
print("Top element:", s.peek())   # Should return 30

# Pop an element from the stack
print("Popped element:", s.pop()) # Should return 30

# Display the stack after popping
s.display()

# Output:
# Stack (top to bottom):
# 20
# 10

# Check the size of the stack
print("Size of stack:", s.size())          # Should return 2

# Check if the stack is empty
print("Is the stack empty?", s.is_empty())  # Should return False
#********************************************************************

# Key Points:
# - Python lists can be used as stacks but have slower performance for large data sets due to memory reallocation.
# - `deque` from the collections module is more efficient for stack operations and is preferred for large-scale stack implementations.

# Implementing a Stack Using collections.deque
from collections import deque

# Create a deque as a stack
stack = deque()
print("Initial stack:", stack)
print("Is the stack empty?", not stack)  # Check if the stack is empty

# Pushing elements onto the stack
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after pushing elements:", stack)

# Popping the top element from the stack
print("Popped element:", stack.pop())
print("Stack after popping an element:", stack)

# Peeking at the top element (accessing the top element without removing it)
# Deque doesn't have a direct peek method, so we use stack[0] for the top element
print("Top element (peek):", stack[0])

'''
deque stack operations:

I clarified the use of deque for the stack. deque.append() is used to push elements onto the stack, and deque.pop() removes and returns the top element.

I also used stack[0] for peeking at the top element in deque. However, deque doesn't have a built-in peek() method, so stack[0] is used to access the top element, as deque is designed to perform fast operations from both ends.

Stack class enhancements:

The display() method now clearly shows the stack from top to bottom.

The is_empty() method and other helper methods like size() and peek() are more consistent with standard stack operations.

I added a check in the display() method to ensure that it correctly handles the case when the stack is empty.
'''

#***************************************************************
'''The implementation of a stack using LifoQueue from Python’s queue module is a great alternative when you need thread-safe stack operations. I see you're using a maxsize of 3 for the stack, which adds the concept of limiting the size of the stack.

Refinement and Explanation of Code:
Here’s an updated version of your code with some minor improvements and additional explanations:

Timeout in put(): You have correctly mentioned that timeout works for put() when the queue is full. I’ll add an example to show how it works.

Thread-Safety: The LifoQueue is thread-safe, meaning it can be used safely in multi-threaded applications.

Check Empty After All Elements are Popped: You checked for an empty stack after popping all the elements, but the LifoQueue behaves differently if you attempt to pop from an empty queue without timeout or error handling.'''

#Updated Code with Explanations:
# Stack using LifoQueue (from queue module)
from queue import LifoQueue

# Create a stack with a maximum size of 3
stack = LifoQueue(maxsize=3)

# Push elements onto the stack
stack.put(1)
stack.put(2)
stack.put(3)

# Uncomment the following line to see how it behaves when trying to push onto a full stack.
# stack.put(4, timeout=3)  # This will block or raise an error after 3 seconds if the stack is full.

# Check if the stack is full
print("Is full?", stack.full())  # Output: True, because we've added 3 items, and the max size is 3

# Get the size of the stack
print("Size:", stack.qsize())    # Output: 3

# Pop elements from the stack
print("Popped:", stack.get())    # Output: 3 (last pushed element)
print("Popped:", stack.get())    # Output: 2
print("Popped:", stack.get())    # Output: 1

# Uncomment the following line to see what happens when trying to pop from an empty stack:
# print("Popped:", stack.get())  # This will block until an item is added (use timeout to avoid blocking)

# Check if the stack is empty
print("Is empty?", stack.empty())  # Output: True, since all elements have been popped

# Example of handling timeout (if you want to add an element but stack is full)
try:
    stack.put(4, timeout=3)  # Will raise queue.Full if the timeout is reached
    print("Pushed 4 onto stack")
except Exception as e:
    print("Error:", e)  # Will print "Error: Full"

#***************************************************************
'''
Summary: deque vs LifoQueue
Feature               deque                       LifoQueue
Performance           Faster (O(1))               Slightly slower
Thread-safe           ❌ No                      ✅ Yes
Max size control      ❌ Manual check needed     ✅ Built-in max size
Blocking behavior     ❌ No                      ✅ Supports blocking
'''

