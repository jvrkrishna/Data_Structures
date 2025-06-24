#Doubly Linked List in Python:
'''A Doubly Linked List is a linear data structure in which each element (node) has two pointers:
One pointer that points to the next node (like in a singly linked list).
Another pointer that points to the previous node, allowing traversal in both directions.

Each node contains three parts:
Data: The actual data stored in the node.
Next: A pointer/reference to the next node in the sequence.
Prev: A pointer/reference to the previous node in the sequence.'''

#Basic Terminology:
'''
Node: Each element in the list.
Head: The first node in the list.
Tail: The last node in the list (which points to None in both next and prev).
Next Pointer: Points to the next node in the sequence or None if it's the last node.
Prev Pointer: Points to the previous node in the sequence or None if it's the first node.
'''
#Structure of a Node:
class Node:
    def __init__(self, data):
        self.data = data  # Data part of the node
        self.next = None  # Address of next node (pointer to the next node)
        self.prev = None  # Address of previous node (pointer to the previous node)
n=Node(10)
print(n.__dict__)

#Structure of Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty
        self.tail = None  # Initially, the list is empty

    # Insertion, deletion, and other operations can be added here.

        
s=DoublyLinkedList()
print(s.__dict__)
#****************************************************************************************

#Creation of Doubly Linked List:
'''In a doubly linked list, each node has two pointers:
One pointing to the next node.
One pointing to the previous node.'''
# Creation of Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data  # Data part of the node
        self.next = None  # Pointer to the next node (initially None)
        self.prev = None  # Pointer to the previous node (initially None)

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    def display(self):
        if self.head is None:
            print("Doubly Linked List is Empty")
        else:
            temp = self.head  # Preserve self.head
            while temp:
                print(temp.data, "<-->", end=" ")
                temp = temp.next
            print("None")  # End of the list

# Creating nodes and linking them
dll = DoublyLinkedList()

# Creating the first node
n = Node(10)
dll.head = n  # Head of the list is the first node

# Creating the second node
n1 = Node(20)
n.next = n1  # Link 10 <--> 20
n1.prev = n  # Set previous of 20 to 10

# Creating the third node
n2 = Node(30)
n1.next = n2  # Link 20 <--> 30
n2.prev = n1  # Set previous of 30 to 20

# Display the doubly linked list
dll.display()

'''************************************************************************'''
#1. insert_at_beginning:
'''
To insert a new node at the beginning of a doubly linked list:
1. Create a new node.
2. Set its next pointer to point to the current head.
3. Set the prev pointer of the current head node to the new node (if it exists).
4. Update the head to point to the new node.'''
#1. insert_at_beginning for Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    def insert_at_beginning(self, data):
        # Step 1: Create a new node
        new_node = Node(data)

        # Step 2: Make the new node's next point to the current head
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node  # Update the previous pointer of the old head

        # Step 3: Set the new node as the head of the list
        self.head = new_node

    def display(self):
        if self.head is None:
            print("Doubly Linked List is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "<-->", end=" ")
                temp = temp.next
            print("None")

# Create Doubly Linked List and nodes
dll = DoublyLinkedList()

# Existing nodes
n = Node(10)
dll.head = n

n1 = Node(20)
n.next = n1
n1.prev = n

n2 = Node(30)
n1.next = n2
n2.prev = n1

print("Before Insertion at Beginning:")
dll.display()

# Insert new node at the beginning
dll.insert_at_beginning(5)

print("After Insertion at Beginning:")
dll.display()

'''************************************************************************'''
#🧠 2.  Inserting at the End:
'''
1. Create a new node with the provided data.
2. If the list is empty (i.e., the head is None), set the head to the new node.
3. Otherwise, traverse the list until the last node.
4. Update the last node's next pointer to point to the new node.
5. Set the prev pointer of the new node to point to the last node.'''
# 2. Inserting at the End in Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to next node
        self.prev = None  # Pointer to previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    def insert_at_end(self, data):
        # Step 1: Create a new node
        new_node = Node(data)

        # Step 2: If the list is empty, set the new node as head
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:  # Traverse to the last node
                temp = temp.next
            # Step 3: Update the last node's next pointer
            temp.next = new_node
            # Step 4: Set new node's prev pointer to the last node
            new_node.prev = temp

    def display(self):
        if self.head is None:
            print("Doubly Linked List is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "<-->", end=" ")
                temp = temp.next
            print("None")

# Create Doubly Linked List and add initial nodes
dll = DoublyLinkedList()

# Manually link initial nodes
n = Node(10)
dll.head = n

n1 = Node(20)
n.next = n1
n1.prev = n

n2 = Node(30)
n1.next = n2
n2.prev = n1

print("Before Insertion at End:")
dll.display()

# Insert at end
dll.insert_at_end(40)

print("After Insertion at End:")
dll.display()

'''************************************************************************'''
#🧠 3.  Inserting at Position:
'''
1. Create a new node.
2. Traverse the list to the node just before the desired position.
3. Adjust the links:
    i. Set the next pointer of the node before the desired position to point to the new node.
    ii. Set the prev pointer of the node after the new node to point back to the new node.
    iii. Set the prev pointer of the new node to the node before it and the next pointer of the new node to the node after it.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to next node
        self.prev = None  # Pointer to previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    def insert_at_end(self, data):
        # Create a new node
        new_node = Node(data)
        
        if self.head is None:  # If the list is empty
            self.head = new_node
        else:
            temp = self.head
            while temp.next:  # Traverse to the last node
                temp = temp.next
            # Update the last node's next pointer
            temp.next = new_node
            # Update new node's prev pointer
            new_node.prev = temp

    def insert_at_position(self, position, data):
        # Step 1: Create a new node
        new_node = Node(data)

        if position == 1:  # Insert at the beginning (position 1)
            # Point the new node's next to the current head
            new_node.next = self.head
            if self.head:  # If the list is not empty
                self.head.prev = new_node
            # Update head to new node
            self.head = new_node
            return

        temp = self.head
        # Step 2: Traverse to the node just before the desired position
        for _ in range(position - 2):
            if temp is None:
                print("Position is out of bounds!")
                return
            temp = temp.next
        
        # Step 3: Adjust the links to insert at the desired position
        new_node.next = temp.next  # New node's next points to temp's next
        if temp.next:  # If the new node is not inserted at the end
            temp.next.prev = new_node  # Update the previous pointer of the next node
        new_node.prev = temp  # New node's prev points to temp
        temp.next = new_node  # Temp node's next points to the new node

    def display(self):
        if self.head is None:
            print("Doubly Linked List is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "<-->", end=" ")
                temp = temp.next
            print("None")

# Example usage:
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)

print("Before insertion at position:")
dll.display()

dll.insert_at_position(2, 15)  # Insert 15 at position 2

print("After insertion at position 2:")
dll.display()

dll.insert_at_position(1, 5)  # Insert 5 at position 1 (beginning)

print("After insertion at position 1:")
dll.display()

dll.insert_at_position(5, 40)  # Insert 40 at position 5 (end)

print("After insertion at position 5:")
dll.display()
