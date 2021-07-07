from queue import PriorityQueue

class Leaf():
    def __init__(self, left=None, right=None, index=None):
        self.left = left
        self.right = right
        self.index = index


S = ["a", "b", "c" ,"d", "e", "f" ]
F = [10 , 11 , 7 , 13, 1 , 20 ]

q = PriorityQueue()

n = len(S)
for i in range(n):
    leaf = Leaf(None, None, i)
    q.put((F[i], leaf))

newQueueObject = None
while not q.empty():
    if newQueueObject is not None:
        q.put(newQueueObject)
    nextItem1 = q.get()
    nextItem2 = q.get()
    value = nextItem1[0] + nextItem2[0]
    newLeaf = Leaf(nextItem2, nextItem1)
    newQueueObject = (value, newLeaf)

def getSolution(A,tuple, code):
    leaf = tuple[1]
    if leaf.left is None and leaf.right is None:
        A[leaf.index] = code

    if leaf.left is not None:
        getSolution(A, leaf.left, code + '0')
    if leaf.right is not None:
        getSolution(A, leaf.right, code + '1')
    return A

root = newQueueObject
A = [0] * n
getSolution(A, root, '')

length = 0
for i in range(n):
    print(f'{S[i]}: {A[i]}')
    length += F[i] * len(A[i])

print('długość napisu:', length)