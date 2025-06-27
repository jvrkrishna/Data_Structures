# Circular Linked List in Python:
'''-->Single Linked list    
-->last node will have address of first node   
-->collection of nodes connected in circular form.'''

#Basic Terminology:
'''Node: Each element in the list.
Head: The first node in the list (which points to the next node in the sequence).
Tail: The last node in the list (which points back to the head).
next Pointer: Points to the next node in the list, or the head if it's the last node in a circular singly linked list.
prev Pointer: In a doubly circular linked list, the previous node pointer that points to the previous node, or the tail if it's the first node.'''

#Characteristics of a Circular Linked List:
'''
1. The last node points to the first node instead of None (circular nature).
2. It doesn't have a clear end, making traversal a bit different (it keeps looping).
3. There’s no "None" at the end of the list.
4. Can be used in applications where the data needs to be looped (e.g., circular buffers, round-robin scheduling).
'''

# Structure of a Node for Circular Linked List:
class Node:
    def __init__(self, data):
        self.data = data  # Data part of the node
        self.next = None  # Pointer to the next node (initially None)

n = Node(10)
print(n.__dict__)

'''***********************************************************************************'''

# Structure of Circular Linked List:
class CircularLinkedList:
    def __init__(self):
        self.head = None  # The head will point to the first node
        self.tail = None  # The tail will point to the last node

    def is_empty(self):
        return self.head is None  # Check if the list is empty
    
c=CircularLinkedList()
print(c.__dict__)

'''***********************************************************************************'''

# Structure of a Node for Circular Linked List:
class Node:
    def __init__(self, data):
        self.data = data  # Data part of the node
        self.next = None  # Pointer to the next node (initially None)

n = Node(10)
print(n.__dict__)

# Structure of Circular Linked List:
class CircularLinkedList:
    def __init__(self):
        self.head = None  # The head will point to the first node
        self.tail = None  # The tail will point to the last node

    def is_empty(self):
        return self.head is None  # Check if the list is empty
    
    # Add a node to the list (as an example)
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head  # Points to itself (circular)
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head  # Points back to the head (circular)

# Example usage:
circular_list = CircularLinkedList()
circular_list.append(10)
circular_list.append(20)
circular_list.append(30)

# Printing out the circular list structure
print(circular_list.__dict__)


'''***********************************************************************************'''
# 1. insert_at_beginning:
'''🧠 Concept:
To insert a new node at the beginning:
1. Create a new node.
2. Set its next to point to the current head.
3. Update tail's next to point to the new node (keeping the circular property).
4. Update head to point to the new node.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Address of next node

class CircularLinkedList:
    def __init__(self):
        self.head = None  # The head points to the first node
        self.tail = None  # The tail points to the last node

    def insert_at_beginning(self, data):
        new_node = Node(data)  # Step 1: Create new node

        if self.head is None:  # Empty list case
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head  # Circular link (points to itself)
        else:  # Non-empty list case
            new_node.next = self.head  # Step 2: Link new node to current head
            self.head = new_node        # Step 3: Update head to new node
            self.tail.next = self.head  # Step 4: Update tail’s next to point to the new head (circular property)

    def display(self):
        if self.head is None:
            print("Circular Linked List is Empty")
        else:
            temp = self.head
            while True:
                print(temp.data, "-->", end=" ")
                temp = temp.next
                if temp == self.head:  # Stop when we loop back to the head
                    break
            print("(Back to head)")

# Create Circular Linked List and nodes
C = CircularLinkedList()

# Existing nodes (creating a circular list)
n = Node(10)
C.head = n
C.tail = n
n.next = C.head  # Circular reference to itself

n1 = Node(20)
n.next = n1
C.tail = n1
n1.next = C.head  # Tail points back to head

n2 = Node(30)
n1.next = n2
C.tail = n2
n2.next = C.head  # Tail points back to head

print("Before Insertion at Beginning:")
C.display()

# Insert new node at beginning
C.insert_at_beginning(5)

print("After Insertion at Beginning:")
C.display()

'''***********************************************************************************'''
#🧠 2. Inserting at the End in Circular Linked List:
'''
1. Create a new node.
2. If the list is empty (head is None), set head and tail to the new node.
3. Otherwise, traverse to the last node (tail).
4. Set last_node.next = new_node.
5. Update tail to the new node (tail now points to the new last node).
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Address of next node

class CircularLinkedList:
    def __init__(self):
        self.head = None  # The head points to the first node
        self.tail = None  # The tail points to the last node

    def insert_at_end(self, data):
        new_node = Node(data)  # Step 1: Create new node

        if self.head is None:  # Step 2: If the list is empty, set head and tail to new node
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head  # Circular link (points to itself)
        else:  # Step 3 & 4: Traverse to last node and insert new node
            self.tail.next = new_node  # Link current tail to new node
            self.tail = new_node        # Update tail to new node
            self.tail.next = self.head  # Step 5: Make the tail's next point back to head (circular property)

    def display(self):
        if self.head is None:
            print("Circular Linked List is Empty")
        else:
            temp = self.head
            while True:
                print(temp.data, "-->", end=" ")
                temp = temp.next
                if temp == self.head:  # Stop when we loop back to the head
                    break
            print("(Back to head)")

# Create Circular Linked List and add initial nodes
C = CircularLinkedList()

# Manually link initial nodes
n = Node(10)
C.head = n
C.tail = n
n.next = C.head  # Circular reference to itself

n1 = Node(20)
n.next = n1
C.tail = n1
n1.next = C.head  # Tail points back to head

n2 = Node(30)
n1.next = n2
C.tail = n2
n2.next = C.head  # Tail points back to head

print("Before Insertion at End:")
C.display()

# Insert at end
C.insert_at_end(40)

print("After Insertion at End:")
C.display()

'''************************************************************************'''
# 🧠 3. Inserting at Position in Circular Linked List:
'''
1. Create a new node.
2. Traverse the list to the node just before the desired position.
3. Adjust the links to insert the new node at that position, maintaining the circular property.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None  # The head points to the first node
        self.tail = None  # The tail points to the last node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head  # Circular link (points to itself)
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head  # Tail points back to head

    def insert_at_position(self, position, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head  # Circular link (points to itself)
            return

        if position == 1:  # Inserting at the beginning (same as insert_at_beginning)
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head  # Circular link to the head
            return

        temp = self.head
        count = 1

        # Traverse to the node just before the desired position
        while count < position - 1 and temp.next != self.head:
            temp = temp.next
            count += 1

        # Insert at the desired position
        new_node.next = temp.next
        temp.next = new_node

        # If inserting at the last position, update the tail
        if new_node.next == self.head:
            self.tail = new_node

    def display(self):
        if self.head is None:
            print("Circular Linked List is Empty")
        else:
            temp = self.head
            while True:
                print(temp.data, "-->", end=" ")
                temp = temp.next
                if temp == self.head:  # Stop when we loop back to the head
                    break
            print("(Back to head)")

# Example usage:
C = CircularLinkedList()
C.insert_at_end(10)
C.insert_at_end(20)
C.insert_at_end(30)

print("Before insertion at position:")
C.display()

C.insert_at_position(2, 15)  # Insert 15 at position 2 (after 10)

print("After insertion at position 2:")
C.display()

C.insert_at_position(1, 5)  # Insert 5 at the beginning

print("After insertion at position 1:")
C.display()

C.insert_at_position(5, 40)  # Insert 40 at the end

print("After insertion at position 5:")
C.display()

#******************************************************************************
#🧠Deleting at the End in Circular Linked List:
'''
1. If the list is empty (head is None), do nothing or print a message.
2. If the list has only one node:
   - Set head and tail to None.
3. Otherwise:
   - Traverse to the second-last node (node before tail).
   - Set second_last.next = head.
   - Update tail to second_last.
'''
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def delete_at_end(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        if self.head == self.tail:
            self.head = self.tail = None  # Only one node
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next  # Traverse to second last node
            temp.next = self.head
            self.tail = temp  # Update tail

    def display(self):
        if self.head is None:
            print("Circular Linked List is Empty")
        else:
            temp = self.head
            while True:
                print(temp.data, "-->", end=" ")
                temp = temp.next
                if temp == self.head:
                    break
            print("(Back to head)")
# Create list with manual insertions
C = CircularLinkedList()
C.insert_at_end(10)
C.insert_at_end(20)
C.insert_at_end(30)
C.insert_at_end(40)

print("Before Deletion at End:")
C.display()

C.delete_at_end()

print("After Deletion at End:")
C.display()
