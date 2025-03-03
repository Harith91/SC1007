class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item  # Store the item (integer)
        self.left = left  # Reference to the left child node
        self.right = right  # Reference to the right child node

def insertBSTNode(root = BTNode, value):
    """Recursive approach to insert a node into the BST"""
    # Write your code here #
    if root is None:
        return BTNode(value)
    
    if value == root.item:
        return root


    if value < root.item:
        root.left(insertBSTNode(root.left, value))
    else:
        root.left(insertBSTNode(root.right, value))
    

    return root

def insertBSTNode(root = BTNode, value):
    """Recursive approach to insert a node into the BST"""
    # Write your code here #
    if root is None:
        return root
    
    parent = None
    cur = root

    while cur is not None:
        parent = cur
        if value < cur.item:
            cur = cur.left
        elif value > cur.item:
            cur = cur.right
        else:
            return root  # Value already exists, return root unchanged    




def printTree(node, level=0, prefix="Root: "):
    """Prints the tree structure for better visualization"""
    if node is not None:
        print(" " * level + prefix + str(node.item))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")

def printBSTInOrder(node):
    """ Print BST items in sorted order using in-order traversal. """
    if node:
        print(printBSTInOrder(node.left))
        print(node.item, end = " ")
        print(printBSTInOrder(node.right))

def isBST(node, min_val = float("-inf"), max_val = float("inf")):
    # Write your code here #
    if node is not None:
        isBST(node.left, min_val, node.value) #Check left is !> parent
        isBST(node.right, node.value, max_val) #Check right is !< parent
    
    if node < min_val or node > max_val:
        return False


def removeBSTNode(node, value):
    # Write your code here #
    if node is None:
        return -1

    parent = None
    cur = node

    while cur.item!= value:
        if cur.item > value:
            cur = cur.right
        else:
            cur = cur.left

    if not cur.left and not cur.right: #Node has no children
        if parent.left == cur:
            parent.left = None
        else:
            parent.right = None
    
    elif not cur.left or not cur.right: # Node has 1 child
        if cur.left:
            child = cur.left
            parent.left = child
        else:
            child = cur.right
            parent.right = child
    
    else: #Node has 2 children
        successor = findMin(cur.right)
        cur.item = successor.item

        result = removeBSTNode(cur.right,successor.item)
        
    return 0

    





if __name__ == "__main__":
    root = None
    print("Binary Search Tree Insertion Program")
    print("===================================")
    
    while True:
        try:
            value = input("\nEnter a value to insert (-1 to quit): ")
            if not value:  
                continue  # Ignore empty inputs
                
            i = int(value)
            if i == -1:
                break
                
            root = insertBSTNode(root, i)
            print("\nCurrent BST structure:")
            printTree(root)
            
        except ValueError:
            print("Please enter a valid integer!")

    print("\nFinal BST structure:")
    printTree(root)
