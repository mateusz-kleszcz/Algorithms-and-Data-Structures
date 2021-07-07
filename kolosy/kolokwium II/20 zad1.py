class Node:
    def __init__(self):
        self.children = 0 # liczba dzieci węzła
        self.child = []
        self.firstLongest = 0
        self.secondLongest = 0


def heavy_path(T):

    if T.children == 0:
        return 0, 0

    bestPath = 0
    for i in range(T.children):
        bestChildren, bestPath = heavy_path(T.child[i][0])
        bestChildren += T.child[i][1]
        if bestChildren > T.firstLongest:
            T.firstLongest = bestChildren
        elif bestChildren > T.secondLongest:
            T.secondLongest = bestChildren

    best = max(T.firstLongest + T.secondLongest, bestPath)

    return T.firstLongest, best



A = Node()
B = Node()
C = Node()
A.children = 2
A.child = [ (B,5), (C,-1) ]
print(heavy_path(A))