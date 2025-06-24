'''A linked list is a type of linear data structure similar to arrays. It is a collection of nodes that are linked with each other. A node contains two things first is data and second is a link that connects it with another node.In linked list each node contains character data and a link to another node. Our first node is where head points and we can access all the elements of the linked list using the head.

It contains a series of nodes that are stored at random locations in memory, allowing for efficient memory management.
'''

#Types of Linked Lists:
'''
•Singly Linked List: Each node points to the next node in the list.
•Doubly Linked List: Each node has two pointers—one pointing to the next node and one pointing to the previous node.
•Circular Linked List: The last node points back to the first node, forming a circle.
'''

#Advantages of Linked Lists:
'''
1.Dynamic Size: Linked lists do not have a fixed size. They grow and shrink as needed, unlike arrays that require a fixed size.

2.Efficient Insertions/Deletions: Inserting or deleting nodes (especially at the beginning or middle or end) is faster than in arrays because there’s no need to shift elements.

3.Memory Efficiency: Linked lists allocate memory dynamically for each element, unlike arrays, where memory must be pre-allocated.

4.No Wasted Space: Since the memory allocation for nodes happens as elements are added, there is no unused space (which may happen in arrays when the array size is larger than needed).'''

#Disadvantages of Linked Lists:
'''
1.Memory Overhead: Each node requires extra memory to store the pointer/reference to the next node. In the case of a doubly linked list, each node needs two pointers.

2.Sequential Access: To access an element at a specific position, you must traverse the list from the start (or end in a doubly linked list), which can be slow (O(n) time complexity).
'''

#Singly Linked List in Python:
'''A singly linked list is a linear data structure where each element (called a node) points to the next node in the sequence. It’s a chain of nodes, where each node contains two parts:
Data: The actual data that the node holds.
Next: A reference (or pointer) to the next node in the list.

Basic Terminology:
Node: Each element in the list.
Head: The first node in the list.
Tail: The last node in the list (which points to None).
Next Pointer: Points to the next node, or None if it's the last node.
'''
#Structure of a Node:
class Node:
    def __init__(self, data):
        self.data = data  # Data part of the node
        self.ref = None  # Pointer to the ref node (initially None)
'''************************************************************************'''
#Structure of the Singly Linked List:
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the list with an empty head
'''************************************************************************'''
#Example Program:
class Node:
    def __init__(self, data):
        self.data = data  # Data part of the node
        self.ref = None  # Pointer to the ref node (initially None)

    def print_node(self):
        # Print the data of the current node and the ref node's data (if exists)
        ref_node_data = self.ref.data if self.ref else None  # Handle case if ref is None
        print(f"Node data: {self.data}, ref node: {ref_node_data}")
# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Link nodes
node1.ref = node2
node2.ref = node3

# Print the nodes
node1.print_node()  # Output: Node data: 10, ref node: 20
node2.print_node()  # Output: Node data: 20, ref node: 30
node3.print_node()  # Output: Node data: 30, ref node: None
'''************************************************************************'''
#1. insert_at_beginning:
# Structure of the Singly Linked List:
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the list with an empty head

    def insert_at_beginning(self, data):
        new_node = Node(data)  # Create a new node with the given data
        new_node.ref = self.head  # Make the new node's ref point to the current head
        self.head = new_node  # Update the head to the new node

    def print_list(self):
        current_node = self.head
        while current_node:
            current_node.print_node()
            current_node = current_node.ref

# Node definition
class Node:
    def __init__(self, data):
        self.data = data  # Data part of the node
        self.ref = None  # Pointer to the ref node (initially None)

    def print_node(self):
        # Print the data of the current node and the ref node's data (if exists)
        ref_node_data = self.ref.data if self.ref else None  # Handle case if ref is None
        print(f"Node data: {self.data}, ref node: {ref_node_data}")

linked_list = LinkedList()

# Inserting nodes at the beginning
linked_list.insert_at_beginning(30)
linked_list.insert_at_beginning(20)
linked_list.insert_at_beginning(10)

# Print the list
linked_list.print_list()

# Output:
# Node data: 10, ref node: 20
# Node data: 20, ref node: 30
# Node data: 30, ref node: None
'''************************************************************************'''
#2. insert_at_end:
# Structure of the Singly Linked List:
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the list with an empty head

    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:
            self.head = new_node  # If the list is empty, make the new node the head
            return
        last_node = self.head
        while last_node.ref:  # Traverse until the last node
            last_node = last_node.ref
        last_node.ref = new_node  # Point the last node's ref to the new node

    def print_list(self):
        current_node = self.head
        while current_node:
            current_node.print_node()
            current_node = current_node.ref

# Node definition
class Node:
    def __init__(self, data):
        self.data = data  # Data part of the node
        self.ref = None  # Pointer to the ref node (initially None)

    def print_node(self):
        # Print the data of the current node and the ref node's data (if exists)
        ref_node_data = self.ref.data if self.ref else None  # Handle case if ref is None
        print(f"Node data: {self.data}, ref node: {ref_node_data}")

# Example Program:
linked_list = LinkedList()

# Inserting nodes at the end
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)

# Print the list
linked_list.print_list()

# Output:
# Node data: 10, ref node: 20
# Node data: 20, ref node: 30
# Node data: 30, ref node: None

'''************************************************************************'''
#3. insert_at_middle:
# Structure of the Singly Linked List:
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the list with an empty head

    def insert_at_middle(self, data, position):
        new_node = Node(data)  # Create a new node with the given data
        if position == 0:  # If position is 0, insert at the beginning
            new_node.ref = self.head
            self.head = new_node
            return
        current_node = self.head
        current_position = 0
        # Traverse the list until the node just before the desired position
        while current_node and current_position < position - 1:
            current_node = current_node.ref
            current_position += 1
        if current_node:  # If the current node is valid (position exists in the list)
            new_node.ref = current_node.ref  # Point the new node's ref to the next node
            current_node.ref = new_node  # Update the current node's ref to point to the new node

    def print_list(self):
        current_node = self.head
        while current_node:
            current_node.print_node()
            current_node = current_node.ref

# Node definition
class Node:
    def __init__(self, data):
        self.data = data  # Data part of the node
        self.ref = None  # Pointer to the ref node (initially None)

    def print_node(self):
        # Print the data of the current node and the ref node's data (if exists)
        ref_node_data = self.ref.data if self.ref else None  # Handle case if ref is None
        print(f"Node data: {self.data}, ref node: {ref_node_data}")

# Example Program:
linked_list = LinkedList()

# Inserting nodes at the end
linked_list.insert_at_middle(10, 0)  # Insert at the beginning (head)
linked_list.insert_at_middle(20, 1)  # Insert at position 1
linked_list.insert_at_middle(30, 2)  # Insert at position 2

# Insert in the middle (at position 1, between 10 and 20)
linked_list.insert_at_middle(15, 1)

# Print the list
linked_list.print_list()

# Output:
# Node data: 10, ref node: 15
# Node data: 15, ref node: 20
# Node data: 20, ref node: 30
# Node data: 30, ref node: None
