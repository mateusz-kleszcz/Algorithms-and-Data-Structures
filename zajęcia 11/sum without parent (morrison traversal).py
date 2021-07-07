class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


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


def prevNode(node):
    key = node.key
    node = node.left
    while node.right is not None and node.right.key < key:
        node = node.right

    return node


def sumMorrisTraversal(root):
    sum = 0
    curr = root

    while curr is not None:
        if curr.left is None:
            sum += curr.key
            curr = curr.right
        else:
            prev = prevNode(curr)
            if prev.right is None:
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                sum += curr.key
                curr = curr.right

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
print(sumMorrisTraversal(A))