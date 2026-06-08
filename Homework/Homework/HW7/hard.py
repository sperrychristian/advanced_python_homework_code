'''
Hard: (Essay, 7 points)

3. Explain the process of deleting a node from a binary search tree in Python. Discuss how you would handle different cases, such as deleting a node with one, or two children. Additionally, explain any potential challenges or edge cases that may arise during the deletion process and how you would address them. 

'''

'''
I've included the code on how the process of deleting a node from a binary search tree would work in Python based on following the lecture videos and creating my own notes. I will reference the code in the following explanation. 

Deleting a node from a binary search tree carries the complexity of in many cases, needing to make changes to the remainder of the tree to keep the data structure in the format it should be in. The first step is locating the node to delete by traversing the tree.

The next step would be to identify if the value we need to delete is smaller or larger than the root. If it's smaller, the value will live on the left side of the binary search tree. If it's greater, the value will live on the right side of the binary search tree. We can use an if statement to direct the alogorithm down the appropriate side of the tree. This process naturally benefits from writing a recursive function that continually moves down the tree until the value being searched for is found. 

Once the program has found the key that needs to be deleted, it needs to determine if the node intended to be deleted has children or not. This is important because if the node DOES NOT have children, there would be no need to restructure the binary search tree. However if the tree does have two children, restructuring the tree is necessary. If the node has only one child, that child is returned directly to the parent, skipping over the deleted node.

# AI PROMPT: 'Break down for me what an in order successor is like I'm 12'

There is need to replace the deleted node with the next in order successor. This can be done using the minimum from the right side of the root being deleted or the maximum for the left. Either would produce a result that falls within the structural rules of a binary search tree. The in order successor will have at most just one child, so moving it from it's position to the deleted node won't produce the need to restructure the tree. 

In the example below, I chose to use the findMinimum function I had already created to determind the in order successor. (also included in the code) 

# AI PROMPT: 'What are some edge cases and challenges I should be aware of when it comes to deleting nodes from a binary search tree'

As far as edge cases and challenges that arise when deleting from a binary search tree go, there is one main issue that can arise I haven't yet discussed. Sometimes, tree are empty and that needs to be handled in the function. This is handled in the by using an if statement stating if the root is Null, return root and stop.

'''

class Node:

    # construcor to create a new node.
    def __init__(self, key):
        self.key = key
        # left child
        self.left = None # None is just a null value
        # right child
        self.right = None

#####################################################

# function to find a minimum value in a tree (non recursive)

def findMinimum(node): # non recursive

    # loopdown to find the leftmost leaf (this doesn't need recursion because we use the while loop to to push the pointer further down the binary search tree)
    while (node.left is not None):
        node = node.left

    return node

#####################################################

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