class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

def print_tree_in_order(node):
    if node is None:
        return
    print_tree_in_order(node.left)
    print(node.item, end=", ")
    print_tree_in_order(node.right)

def printTree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * level + prefix + str(node.item))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")

def mirrorTree(node: BTNode):
    if node is None:
        return

    mirrorTree(node.left)
    mirrorTree(node.right)
    
    temp = node.left
    node.left = node.right #swapping left n right child
    node.right = temp
# Write your code here #

def printsmaller(node, m):
    if node is None:
        return
    printsmaller(node.left,m)
    printsmaller(node.right, m)

    if node.item < m:
        print(node.item, end = " ")

def smallestval(node:BTNode):
    if node is None:
        return 1000000000 #will never be MIN, doesn't affect result if None
    
    v1 = smallestval(node.left)
    v2 = smallestval(node.right)

    value = node.item 
    value = min(v1,v2,value) #compare v1, v2 and current val to get smallest of three

    return value

def HasGGC(node:BTNode):
    if node is None:
        return 0 #will never be MAX, doesn't affect result if None
    height = 1
    h1 = HasGGC(node.left)
    h2 = HasGGC(node.right)

    height = max(h1 + 1,h2 + 1,height) #compare v1, v2 and current val to get largest of three

    if height >= 4:
        print(node.item, end = " ")

    return height



if __name__ == "__main__":
    root = BTNode(4)
    root.left = BTNode(5)
    root.right = BTNode(2)
    root.left.left = None
    root.left.right = BTNode(6)
    root.right.left = BTNode(3)
    root.right.right = BTNode(1)

    print("Original Tree Structure:")
    printTree(root)
    print("\nOriginal Tree (In-Order):")
    print_tree_in_order(root)
    print()

    mirrorTree(root)
    
    print("\nMirrored Tree Structure:")
    printTree(root)
    print("\nMirrored Tree (In-Order):")

    print_tree_in_order(root)
    print()

    print("numbers smaller than 4: ")
    printsmaller(root, 4)
    print()

    print("smallest num: ")
    print(smallestval(root))
    print()

    print("nodes with GGC: ")
    print(HasGGC(root))
    print()


