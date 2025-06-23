'''A linked list is a type of linear data structure similar to arrays. It is a collection of nodes that are linked with each other. A node contains two things first is data and second is a link that connects it with another node.In linked list each node contains character data and a link to another node. Our first node is where head points and we can access all the elements of the linked list using the head.
It contains a series of nodes that are stored at random locations in memory, allowing for efficient memory management.
 
Types of Linked Lists:
•	Singly Linked List: Each node points to the next node in the list.
•	Doubly Linked List: Each node has two pointers—one pointing to the next node and one pointing to the previous node.
•	Circular Linked List: The last node points back to the first node, forming a circle.
________________________________________
Advantages of Linked Lists:
1.	Dynamic Size: Linked lists do not have a fixed size. They grow and shrink as needed, unlike arrays that require a fixed size.
2.	Efficient Insertions/Deletions: Inserting or deleting nodes (especially at the beginning or middle) is faster than in arrays because there’s no need to shift elements.
3.	Memory Efficiency: Linked lists allocate memory dynamically for each element, unlike arrays, where memory must be pre-allocated.
4.	No Wasted Space: Since the memory allocation for nodes happens as elements are added, there is no unused space (which may happen in arrays when the array size is larger than needed).
________________________________________
Disadvantages of Linked Lists:
1.	Memory Overhead: Each node requires extra memory to store the pointer/reference to the next node. In the case of a doubly linked list, each node needs two pointers.
2.	Sequential Access: To access an element at a specific position, you must traverse the list from the start (or end in a doubly linked list), which can be slow (O(n) time complexity).
'''


#Singly Linked List in Python: Simple Notes
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
        self.next = None  # Pointer to the next node (initially None)

#Structure of the Singly Linked List:
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the list with an empty head

#Example Program:
class Node:
    def __init__(self, data):
        self.data = data  # Data part of the node
        self.next = None  # Pointer to the next node (initially None)

    def print_node(self):
        # Print the data of the current node and the next node's data (if exists)
        next_node_data = self.next.data if self.next else None  # Handle case if next is None
        print(f"Node data: {self.data}, Next node: {next_node_data}")
# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Link nodes
node1.next = node2
node2.next = node3

# Print the nodes
node1.print_node()  # Output: Node data: 10, Next node: 20
node2.print_node()  # Output: Node data: 20, Next node: 30
node3.print_node()  # Output: Node data: 30, Next node: None


