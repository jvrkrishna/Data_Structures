'''
Stack: A stack is a linear data structure that follows the principle of Last In First Out (LIFO). This means the last element inserted inside the stack is removed first.
'''
#Common Stack Actions (Operations)
'''
Operation	Description
push()	       Adds an element to the top of the stack
pop()	       Removes and returns the top element
peek() / top() Returns the top element without removing it
is_empty()	   Checks if the stack is empty
size()	       Returns the number of elements in the stack
'''
#Working of Stack Data Structure
'''
The operations work as follows:
1.	A pointer called TOP is used to keep track of the top element in the stack.
2.	When initializing the stack, we set its value to -1 so that we can check if the stack is empty by comparing TOP == -1.
3.	On pushing an element, we increase the value of TOP and place the new element in the position pointed to by TOP.
4.	On popping an element, we return the element pointed to by TOP and reduce its value.
5.	Before pushing, we check if the stack is already full
6.	Before popping, we check if the stack is already empty
'''
# Stack implementation in python list
stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
stack.pop()
stack.pop()
print(stack)

#To know the stack is empty or not
stack=[]
print(len(stack))==0
print(not stack)

stack.append(10)
stack.append(20)
print(stack[-1])

##Stack implementation in python list
stack=[]
def push():
    element = input("Enter the element:")
    stack.append(element)
    print(stack)

def pop_element():
    if not stack:
        print("stack is empty!")
    else:
        e = stack.pop()
        print("removed element:",e)
        print(stack)

while True:
    print("Select the operation 1. push 2.pop 3.quit")
    choice = int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("Enter the correct operation!")
***************************************************************
# # Stack implementation in python list
# Creating a stack
def create_stack():
    stack = []
    return stack

print(create_stack())

# # Creating an empty stack
def check_empty(stack):
    return len(stack) == 0

print(check_empty([]))

# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: ",item)
stack=[]
push(stack, 1)         
push(stack, "hello")   
push(stack, 3.14)      
push(stack, True)  

# Removing an element from the stack
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()
print("popped item: ", pop(stack))
print("stack after popping an element: ", stack)
***************************************************************
'''Key Points
Python lists can be used as stacks but have slower performance for large data sets due to memory reallocation.

deque is more efficient for stack operations and is preferred for large-scale stack implementations.
'''
#Implementing a Stack Using collections.deque
from collections import deque

stack = deque()
print(stack)
print(not stack) #Is empty or not

stack.append(10)
stack.append(20)
stack.append(30)
print(stack)

print(stack.pop())

print(stack)

print(stack[0])

#Custom Stack Class in Python
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

    # Display the stack (top to bottom)
    def display(self):
        print("Stack (top to bottom):")
        for item in reversed(self.items):
            print(item)
            
# Create a stack
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()
# Output:
# Stack (top to bottom):
# 30
# 20
# 10

print("Top element:", s.peek())   # 30
print("Popped element:", s.pop()) # 30
print("Size:", s.size())          # 2
print("Is empty?", s.is_empty())  # False
***************************************************************
#Stack using queue.LifoQueue
from queue import LifoQueue

# Create a stack with max size 3
stack = LifoQueue(maxsize=3)

# Push elements
stack.put(1)
stack.put(2)
stack.put(3)

#stack.put(4,timeout=3)  # Blocks or raises if full (depending on parameters and timeout is used to give the result after 3 seconds)

# Check full
print("Is full?", stack.full())  # Output: True

# Size
print("Size:", stack.qsize())    # Output: 3

# Pop elements
print("Popped:", stack.get())    # Output: 3
print("Popped:", stack.get())    # Output: 2
print("Popped:", stack.get())    # Output: 1
print("Popped:", stack.get()) #in get()---timeout works when the error raises it is mandatory to give timeout otherwise the result is idle.

# Check if empty
print("Is empty?", stack.empty())  # Output: False
***************************************************************
'''
Summary: deque vs LifoQueue
Feature	              deque	                      LifoQueue
Performance	          Faster (O(1))	              Slightly slower
Thread-safe	          ❌ No	                    ✅ Yes
Max size control	  ❌ Manual check needed	    ✅ Built-in max size
Blocking behavior	  ❌ No	                    ✅ Supports blocking
'''