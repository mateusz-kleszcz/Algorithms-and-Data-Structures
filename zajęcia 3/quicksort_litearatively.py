from random import  randint

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def top(self):
        return self.items[-1]

    def pop(self):
        self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def partition(T, l, r):
    random_index = randint(l, r)
    T[random_index], T[r] = T[r], T[random_index]
    pivot = T[r]
    i = l
    for j in range(l, r):
        if T[j] < pivot:
            T[i], T[j] = T[j], T[i]
            i += 1
    T[i], T[r] = T[r], T[i]
    return i


def quicksort(T, l, r):
    S = Stack()
    S.push(l)
    S.push(r)
    while not S.isEmpty():
        r = S.top(); S.pop()
        l = S.top(); S.pop()
        p = partition(T, l, r)
        if l < p - 1:
            S.push(l)
            S.push(p - 1)
        if p + 1 < r:
            S.push(p + 1)
            S.push(r)
    return T


tab = [21, 37, 69, 420, 11, 23, 56, 11]
quicksort(tab, 0, len(tab) - 1)
print(tab)