class Node:
    def __init__(self):
        self.value = None
        self.next = None


def print_list(L):
    if L is not None:
        print(L.value, end=' ')
        print_list(L.next)


def insert_to_list(L, node):
    first = L
    while L.next is not None:
        L = L.next
    L.next = node
    return first


def bubble_sort(L):
    first = L
    while L.next is not None:
        prev = L
        curr = L.next
        front = L.next.next
        while curr.next is not None:
            if curr.value > front.value:
                prev.next = front
                curr.next = front.next
                front.next = curr
                curr, front = front, curr
            prev = prev.next
            curr = curr.next
            front = front.next
        L = L.next
    return first


L = Node()
for i in [1, 8, 2, 16, 64, 7]:
    a = Node()
    a.value = i
    insert_to_list(L, a)

print_list(bubble_sort(L))