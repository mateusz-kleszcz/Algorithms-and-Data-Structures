class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.f = 0


def tree(v):

    if v is None: return 0, 0

    l, bestL = tree(v.left)
    r, bestR = tree(v.right)

    v.f = max(0, v.value, v.value + l, v.value + r)
    best = max(bestL, bestR, v.f, bestL + bestR)
    return v.f, best


a = Node(-4)
b = Node(10)
c = Node(-8)
d = Node(4)
a.left = b
a.right = c
b.left = d

print(tree(a)[1])