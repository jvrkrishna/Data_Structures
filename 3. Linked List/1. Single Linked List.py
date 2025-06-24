#Singly Linked List in Python:
'''A singly linked list is a linear data structure where each element (called a node) points to the next node in the sequence. It’s a chain of nodes, where each node contains two parts:
Data: The actual data that the node holds.
next: A nexterence (or pointer) to the next node in the list.

Basic Terminology:
Node: Each element in the list.
Head: The first node in the list.
Tail: The last node in the list (which points to None).
next Pointer: Points to the next node, or None if it's the last node.
'''
#Structure of a Node:
class Node:
    def __init__(self, data):
        self.data = data # Data part of the node
        self.next = None  # Address of next node (# Pointer to the next node (initially None))

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp = self.head  # Preserve self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
            print("None")  # End of the list

# Creating nodes and linking them
L = SingleLinkedList()
n = Node(10)
L.head = n

n1 = Node(20)  # Link 10 -> 20
n.next = n1

n2 = Node(30) # Link 20 -> 30
n1.next = n2

# Display the list
L.display()

'''************************************************************************'''
#1. insert_at_beginning:
'''🧠 Concept:
To insert a new node at the beginning:
1. Create a new node.
2. Set its next to point to the current head.
3. Update head to point to the new node.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Address of next node

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)       # Step 1: Create new node ---Here created data|None
        new_node.next = self.head   # Step 2: Link new node to current head
        self.head = new_node        # Step 3: Update head to new node

    def display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
            print("None")

# Create Linked List and nodes
L = SingleLinkedList()

# Existing nodes
n = Node(10)
L.head = n

n1 = Node(20)
n.next = n1

n2 = Node(30)
n1.next = n2

print("Before Insertion at Beginning:")
L.display()

# Insert new node at beginning
L.insert_at_beginning(5)

print("After Insertion at Beginning:")
L.display()


'''************************************************************************'''
#🧠 2.  Inserting at the End:
'''
1. Create a new node.
2. If the list is empty (head is None), set head to the new node.
3. Otherwise, traverse to the last node.
4. Set last_node.next = new_node.'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Address of next node

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data) # Step 1: Create new node ---Here created data|None
        if self.head is None: #Step 2
            self.head = new_node 
        else:
            temp = self.head
            while temp.next:  # Traverse to last node
                temp = temp.next
            temp.next = new_node  # Link last node to new node

    def display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
            print("None")

# Create Linked List and add initial nodes
L = SingleLinkedList()

# Manually link initial nodes
n = Node(10)
L.head = n

n1 = Node(20)
n.next = n1

n2 = Node(30)
n1.next = n2

print("Before Insertion at End:")
L.display()

# Insert at end
L.insert_at_end(40)

print("After Insertion at End:")
L.display()


'''************************************************************************'''
#🧠 3.  Inserting at Position:
'''
1. Create a new node.
2. traverse the list to the node just before the desired position.
3. Adjust the links to insert the new node at that position.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert_at_position(self, position, data):
        new_node = Node(data)
        temp = self.head
        for i in range(position - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
            print("None")

# Example usage:
L = SingleLinkedList()
L.insert_at_end(10)
L.insert_at_end(20)
L.insert_at_end(30)

print("Before insertion at position:")
L.display()

L.insert_at_position(2, 15)  # Insert 15 at position 1

print("After insertion at position 2:")
L.display()