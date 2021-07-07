class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def insert(root, node):
    parent = root

    while root is not None:
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


def minimum(root):
    while root.left is not None:
        root = root.left

    return root


def nextNode(node):
    key = node.key
    if node.right is not None:
        node = node.right
        return minimum(node)
    else:
        while node.parent is not None and node.parent.key < key:
            node = node.parent
        return node.parent


def sumWithParent(root):
    root = minimum(root)
    sum = 0
    while root is not None:
        sum += root.key
        root = nextNode(root)
    return sum


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
print(sumWithParent(A))