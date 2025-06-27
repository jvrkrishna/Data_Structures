'''A tree is a hierarchical data structure consisting of nodes connected by edges. Each tree has a root node, which serves as the starting point for traversing the tree. A tree structure is made up of parent and child relationships where each parent node can have multiple child nodes, but each child node has only one parent (except for the root node, which has no parent).'''

#Key Terminology:
'''
Node: A single element in the tree, typically consisting of data and references (or pointers) to its children.
Root: The topmost node in a tree (the starting point).
Child: A node that is a descendant of another node.
Parent: A node that has children.
Leaf: A node with no children (a node at the bottom of the tree).
Edge: The connection between two nodes.
Subtree: A tree formed from any node and its descendants.'''

#Example Program
#**********************************************************************************
#🌳 Tree Data Structure in Python:
'''
1. Each node has:
   - data
   - list of children (for general trees)
2. Tree is formed by linking nodes in a hierarchical way.
3. The root node is the starting point of the tree.
'''

# Define the Node class
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []  # A list to hold child nodes

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):
        print("  " * level + f"- {self.data}")
        for child in self.children:
            child.display(level + 1)
# Create root node
root = TreeNode("Electronics")

# Create child nodes
laptop = TreeNode("Laptop")
tv = TreeNode("TV")
phone = TreeNode("Smartphone")

# Add children to root
root.add_child(laptop)
root.add_child(tv)
root.add_child(phone)

# Add children to laptop
laptop.add_child(TreeNode("Dell"))
laptop.add_child(TreeNode("HP"))

# Add children to TV
tv.add_child(TreeNode("Samsung"))
tv.add_child(TreeNode("Sony"))

# Add children to Smartphone
phone.add_child(TreeNode("iPhone"))
phone.add_child(TreeNode("OnePlus"))

# Display the tree
root.display()

#Characteristics :
#1. Hierarchical Structure
'''A tree consists of nodes connected by edges, with one node designated as the root.
Each node can have zero or more children (except the leaf nodes, which have no children).
The structure resembles a hierarchy where each node is a "parent" to its children, and it can be thought of as a generalization of a linked list.'''

#2. Nodes and Edges
'''
Node: Contains a value (data) and references (pointers) to its child nodes. If we have n nodes then edges are n-1.

Edge: The connection between two nodes, representing the relationship between a parent node and its child node.

          A
        / | \
       B  C  D
      / \     |
     E   F    G
Nodes:
Node A has the value A and has three child nodes: B, C, and D.
Node B has two child nodes: E and F.
Node C is a leaf node with no children.
Node D has one child node: G.

Nodes E, F, and G are leaf nodes with no children.

Edges:
There are 6 edges:
Edge from A to B
Edge from A to C
Edge from A to D
Edge from B to E
Edge from B to F
Edge from D to G

Tree Representation:
In this example, there are 7 nodes and 6 edges, which confirms the rule: if a tree has n nodes, it has n-1 edges.
'''

#3. Root Node
'''The tree starts at the root node. The root is the only node with no parent. Every other node has exactly one parent.

          A  <-- Root node
        / | \
       B  C  D
      / \     |
     E   F    G
Root Node: Node A is the root. It has no parent.

Children of the Root: Nodes B, C, and D are direct children of the root node A.

Other Nodes: Nodes E, F, and G are descendants of the root but are not directly connected to it. They are further down the hierarchy.
'''

#4. Parent and Child
'''Parent: A node that has one or more child nodes.
Child: A node that is a descendant of a parent node.

A node can have multiple children, but it has only one parent (except for the root node).

          A  <-- Parent node (root)
        / | \
       B  C  D  <-- Parent nodes
      / \     |
     E   F    G  <-- Child nodes
Parent Nodes:
A is the root node and also a parent node to B, C, and D.
B is a parent to E and F.
D is a parent to G.

Child Nodes:
B, C, and D are children of node A.
E and F are children of node B.
G is a child of node D.
'''

#5. Leaf Nodes
'''A leaf node is a node that has no children. These are the terminal nodes in a tree.

          A  <-- Root node
        / | \
       B  C  D
      / \     |
     E   F    G  <-- Leaf nodes
Leaf Nodes: Nodes E, F, and G are leaf nodes because they have no children.

Non-Leaf Nodes: Nodes A, B, C, and D are non-leaf nodes (internal nodes) because they have at least one child.
'''

#6. Depth
'''The depth of a node is the number of edges from the root to that node.
The depth of the root node is zero.

          A  <-- Root node
        / | \
       B  C  D
      / \     |
     E   F    G  <-- Leaf nodes
The depth of node A (root) is 0.

The depth of nodes B, C, and D is 1 because they are one edge away from the root.
'''

#7. Height
'''The height of a node is the length of the longest path from that node to a leaf node.

The height of the tree is the height of the root node.
          A
        / | \
       B  C  D
      / \     |
     E   F    G
1. The heights of the nodes are as follows:
2. E, F, G are leaf nodes, so their heights are 0.
3. B has two children (E and F), and the maximum height of these     children is max(0, 0) + 1 = 1.
4. C is a leaf node, so its height is 0.
5. D has one child (G), so its height is max(0) + 1 = 1.
6. The height of A (root node) is max(height(B), height(C), height(D)) + 1 = max(1, 0, 1) + 1 = 2.

Thus, the height of the tree is 2.
'''

#8. Subtree
'''A subtree is a tree that consists of a node and all its descendants.

          A  <-- Root node
        / | \
       B  C  D
      / \     |
     E   F    G  <-- Leaf nodes
     
The subtree rooted at node B includes:
        B
       / \
      E   F
      
The subtree rooted at node D includes:
    D
   /
  G
  
The subtree rooted at node E is just:
E
'''

#9. Levels
'''The level of a node refers to its distance from the root, i.e., its depth + 1.

All nodes at the same level are at an equal distance from the root.

          A  <-- Level 0 (Root node)
        / | \
       B  C  D  <-- Level 1
      / \     |
     E   F    G  <-- Level 2
     
Level 0: The root node A is at level 0.
Level 1: Nodes B, C, and D are at level 1 because they are directly connected to the root.
Level 2: Nodes E, F, and G are at level 2 because they are one step away from the nodes at level 1.

Level vs Depth:
Depth: The number of edges from the root to a node.
Level: The depth of the node plus 1.

For example:
The depth of node A is 0, and the level of node A is 0 + 1 = 1.
The depth of nodes B, C, and D is 1, and the level of these nodes is 1 + 1 = 2.
'''

#10. Degree of a node:
''' if a node(x) has three childrens then 3 is the degree of a node''' 
'''
          A
        / | \
       B  C  D
      / \     |
     E   F    G  
       
Node A has 3 children: B, C, and D. So, the degree of A is 3.
Node B has 2 children: E and F. So, the degree of B is 2.
Node C has 0 children (leaf node). So, the degree of C is 0.
Node D has 1 child: G. So, the degree of D is 1.
Node E, F, and G are leaf nodes, each with 0 children, so their degree is 0.
'''

#11. Degree of a tree:
''' If a node has highest degree of node then that node is Degree of a tree. To find of degree of tree we have to find out the degree of nodes to all nodes.'''
'''
          A
        / | \
       B  C  D
      / \     |
     E   F    G  
       
Degree of node A: 3 (children B, C, D)
Degree of node B: 2 (children E, F)
Degree of node C: 0 (leaf node)
Degree of node D: 1 (child G)
Degree of node E, F, G: 0 (leaf nodes)

Finally Degree of node is A.
'''

#General Tree:
'''A General Tree is a tree in which each node can have any number of children, including none. There is no restriction on the number of children for each node.'''

#Binary Tree:
'''A Binary Tree is a more specific type of tree where each node has at most two children. The children are usually referred to as the left child and the right child.
Each node in a binary tree can have 0, 1, or 2 children, but not more than two.'''