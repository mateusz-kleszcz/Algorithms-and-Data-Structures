from zad2testy import runtests

class Node:
    def __init__(self, left=None, leftval=0, right=None, rightval=0):
        self.left = left  # lewe podrzewo
        self.leftval = leftval  # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right = right  # prawe poddrzewo
        self.rightval = rightval  # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X = None  # miejsce na dodatkowe dane


def memoized(T, k):

    if T.left is None and T.right is None:
        T.X = [-float('inf')] * (k + 1)
        T.X[0] = 0
        return

    if T.left is not None and T.left.X is None:
        memoized(T.left, k)

    if T.right is not None and T.right.X is None:
        memoized(T.right, k)

    values = [-float('inf')] * (k + 1)
    values[0] = 0

    for i in range(1, k + 1):
        val = -float('inf')
        if T.left is not None:
            val = T.left.X[i - 1] + T.leftval
        if T.right is not None:
            val = max(val, T.right.X[i - 1] + T.rightval)
        maximum = val
        if T.left is not None and T.right is not None:
            for j in range(2, k + 1):
                val = max(val, T.left.X[j - 2] + T.right.X[i - j] + T.leftval + T.rightval)
                if val > maximum:
                    maximum = val
        values[i] = maximum

    T.X = values


def findMax(T):

    k = len(T.X)

    if T.left is None and T.right is None:
        return T.X[k - 1]

    l, r = -float('inf'), -float('inf')

    if T.left is not None:
        l = findMax(T.left)

    if T.right is not None:
        r = findMax(T.right)

    return max(l, r, T.X[k - 1])


def valuableTree(T, k):

    memoized(T, k)

    return findMax(T)


runtests(valuableTree)