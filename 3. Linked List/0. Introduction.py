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
