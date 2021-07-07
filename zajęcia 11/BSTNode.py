class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def find(root, key):
    while root is not None:
        if root.key == key:
            return root
        if root.key < key:
            root = root.right
        else:
            root = root.right

    return None


# zakładam różne wartości klucza
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


def maximum(root):
    while root.right is not None:
        root = root.right

    return root


def prevNode(node):
    key = node.key
    if node.left is not None:
        node = node.left
        return maximum(node)
    else:
        while node.parent is not None and node.parent.key > key:
            node = node.parent
        return node.parent


def nextNode(node):
    key = node.key
    if node.right is not None:
        node = node.right
        return minimum(node)
    else:
        while node.parent is not None and node.parent.key < key:
            node = node.parent
        return node.parent


def delete(node):
    if node.left is None and node.right is None:
        if node.parent.left == node:
            node.parent.left = None
        elif node.parent.right == node:
            node.parent.right = None
        del node
    else:
        curr = node
        prev = prevNode(node)
        curr.key = prev.key
        if prev.left is not None:
            prev.parent.right = prev.left
        del prev

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

delete(A.left)