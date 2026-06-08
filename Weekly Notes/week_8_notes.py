# binary search trees

# operations can be done much faster in a tree than they can in a list data structure

# bst - binary search tree
# a binary tree has nodes and children, this is also reffered to as inner nodes inside of the tree, or leaf nodes if they're on the outside of the tree and don't have children of their own, the root node is the original node\

# similiar to starting to count from index 0 in a list, you start from the root of the nodes in a binary tree (the root is the parent of all other nodes)

# in a binary search tree, every child node on the left must be smaller than the root and the child notes on the right must be greater than the root node

# binary search trees following an order log n operational flow in practice

# binary serach trees naturally pair with recursion, solving the subset is the same process we would use to solve the superset 

# deleting is almost identicle to a find, just once it's deleted we need to adjust the tree so their is no missing node in the middle of the tree

# to handle deleting, we can bring the max of the left subtree up to the empty slot, OR we can bring up the mininmum on the right subtree

# BINARY SEARCH TREE NODES CANNOT HAVE THREE CHILDREN. 


########################################################################

# how to build a binary search tree in python

# the entire structure of a binary search tree are contained in the nodes 

class Node:

    # construcor to create a new node.
    def __init__(self, key):
        self.key = key
        # left child
        self.left = None # None is just a null value
        # right child
        self.right = None

# THE LEFT AND RIGHT CHILDREN IN A BINARY SEARCH TREE WILL ALWAYS EITHER BE A NULL OR A NODE

# function to add a node
def insert(node, key):

    # if the tree is empty, return a new node 
    if node is None:
        return Node(key)
    
    # otherwise, RECUR down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    # return the unchanged node pointer
    return node

    # because of recursion, this will work if the tree is size one or the tree is size one million!

#####################################################

# function to find a minimum value in a tree

def findMinimum(node): # non recursive

    # loopdown to find the leftmost leaf (this doesn't need recursion because we use the while loop to to push the pointer further down the binary search tree)
    while (node.left is not None):
        node = node.left

    return node

# function to find minimum using recursion
def findMinRecursive(node):

    # base case 
    if node.left == None:
        return node
    
    # if we haven't reached the null value in node.left yet, then the function should recur down the tree
    return findMinRecursive(node.left)

# funcrion to find maximum using recursion (structured the exact same as finding the minimum!)

def findMaxRecursive(node):

    # base case 
    if node.right == None:
        return node
    return findMaxRecursive(node.right)

# function to find a node - also recursive
def findKey(root, search_key):
    
    if search_key < root.key:
        if root.left is None:
            return str(search_key) + ' Not Found'
        return findKey(root.left, search_key)
    elif search_key > root.key:
        if root.right is None:
            return str(search_key) + ' Not Found'
        return findKey(root.right, search_key)
    else:
        return root.key + ' Is Found'
    
# this function deletes the key and returns the new root - this one is longer because we have to restructure the tree when the function is called
def deleteNode(root, key):

    # base case 
    if root is None:
        return root
    
    # if the key to be deleted is smaller than the roots key, then it lies in the left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)

    # if the key to ge deleted is greater than the roots key, then it lies in the right subtree
    elif (key > root.key):
        root.right = deleteNode(root.right, key)

    # if the key is the same as the same as the root key, this is the key to be deleted 
    else:

        # handle node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        
        if root.right is None:
            temp = root.left
            root = None
            return temp
        
        # handle node with two children 
        # get the smallest on the right of the subtree or inorder successor
        temp = findMinimum(root.right)

        # copy the inorder successor to this node 
        root.key = temp.key

        # delete the inorder successor 
        root.right = deleteNode(root.right, temp.key)

    return root

# function to print a tree in order 
def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(root.key, end=' ')
        inOrder(root.right)

# function to manage preorder
def preOrder(root):
    if root is not None:
        print(root.key, end=' ')
        preOrder(root.left)
        preOrder(root.right)

# function to manage postorder
def postOrder(root):
    if root is not None:
        postOrder(root.left)
        postOrder(root.right)
        print(root.key, end = ' ')
        
# building a tree takes more compute power than building a list, but it's much faster to search through a tree than a list 






