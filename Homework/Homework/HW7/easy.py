'''
Easy: (3 points)

Write a Python function to insert a value into a binary search tree. The function should take the root of the tree and the value to be inserted as parameters.
'''

# build the class needed for each node 

class Node:

    # constructor
    def __init__(self, key):
        self.key = key
        # right and left children
        self.left = None
        self.right = None

def insertValue(root, key):

    # if the tree is empty, return a new node
    if root is None:
        return Node(key)
    
    # otherwise recur down the tree
    if key < root.key:
        root.left = insertValue(root.left, key)
    elif (key > root.key):
        root.right = insertValue(root.right, key)
        
    return root

# NO AI PROMPTS USED TO SOLVE THIS PROBLEM 
