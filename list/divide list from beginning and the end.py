# Input : 1 —> 2 —> 3 —> 4 —> 5 —> 6
# Output: 1 —> 6 —> 2 —> 5 —> 3 —> 4
class Node:
    def __init__(self):
        self.value = None
        self.next = None


def printList(L):
    while L is not None:
        print(L.value, '->', end=' ')
        L = L.next
    print('|')


def tab2list(T):
    H = Node()
    C = H
    for i in range(len(T)):
        X = Node()
        X.value = T[i]
        C.next = X
        C = X
    return H.next


def reverse(L):
    if L is None or L.next is None:
        return L

    prev = None
    curr = L
    while curr is not None:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    return prev


def rearrange(L):
    if L.next is None or L.next.next is None:
        return L

    fast = L
    slow = L
    prev = None

    while fast is not None:
        if fast.next is not None:
            fast = fast.next
        fast = fast.next
        prev = slow
        slow = slow.next

    prev.next = None

    even = reverse(slow)
    odd = L
    H = odd

    while even is not None:
        tmp = even.next
        even.next = odd.next
        odd.next = even
        odd = odd.next.next
        even = tmp

    return H


L = tab2list([1, 2, 3, 4, 5, 6])
printList(rearrange(L))