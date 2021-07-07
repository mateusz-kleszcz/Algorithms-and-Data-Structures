class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.index = 1
        

def insert(root, node):
    parent = root

    while root is not None:
        root.index += 1
        if root.key < node.key:
            parent = root
            root = root.right
        elif root.key > node.key:
            parent = root
            root = root.left

    if parent.key > node.key:
        parent.left = node
    else:
        parent.right = node
    node.parent = parent


def findI(root, index):
    while True:
        leftVal = root.left.index if root.left is not None else 0
        if leftVal + 1 == index:
            return root.key
        if root.left is not None and root.left.index >= index:
            root = root.left
        else:
            index -= leftVal + 1
            root = root.right


def which(node):
    index = node.left.index + 1 if node.left is not None else 1

    while node.parent is not None:
        if node == node.parent.right:
            index += node.parent.left.index + 1
        node = node.parent

    return index

    
A = BSTNode(21)
insert(A, BSTNode(15))
insert(A, BSTNode(5))
insert(A, BSTNode(7))
insert(A, BSTNode(13))
insert(A, BSTNode(8))
insert(A, BSTNode(20))
insert(A, BSTNode(37))
insert(A, BSTNode(25))
insert(A, BSTNode(23))
insert(A, BSTNode(26))
insert(A, BSTNode(40))

for i in range(1, A.index + 1):
    print(findI(A, i))