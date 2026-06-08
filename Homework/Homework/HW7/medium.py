'''
Medium: (5 points)

2. Implement a Python function to search for a value in a binary search tree. The method should take the root of the tree and the value to be searched as parameters. It should return True if the value is found in the tree, and False otherwise.
'''

class Node:

    # construcor to create a new node.
    def __init__(self, key):
        self.key = key
        # left child
        self.left = None # None is just a null value
        # right child
        self.right = None

def searchValue(root, key):

    # base case
    if root is None:
        return False
    
    # return true if found in the tree
    if key == root.key:
        return True
    
    # recursion to keep the search going on both sides of the root!
    if key > root.key:
        return searchValue(root.right, key)
    if key < root.key:
        return searchValue(root.left, key)
    
# THE FOLLOWING AI PROMPT WAS USED AFTER COMPLETING THIS PROBLEM WITH NO HELP: 'Check this function for accuracy, it should return true if a value lives within a binary search tree and false if it does not' *** pasted in the code I had already written above ***

    