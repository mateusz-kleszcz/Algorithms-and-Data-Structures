class Node:
    def __init__(self, freeX, freeY, allX, allY, height):
        self.freeX = freeX
        self.freeY = freeY
        self.allX = allX
        self.allY = allY
        self.height = height
        self.children = []
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


def tower(arr):
    n = len(arr)

    root = Node(-float('inf'), float('inf'), -float('inf'), float('inf'), 0)

    for el in arr:
        x, y = el

        


arr = [(1, 3), (2, 5), (0, 3), (8, 9), (4, 6)]