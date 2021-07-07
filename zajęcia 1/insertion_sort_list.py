class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def tab_to_list(tab):
    head = Node()
    last = head
    for i in tab:
        last.next = Node(i, None)
        last = last.next
    return head


def print_all(L):
    if L is not None:
        print(L.value, end=' ')
        print_all(L.next)


def insert_to_list(L, node):
    while L.next is not None and L.next.value < node.value:
        L = L.next
    node.next = L.next
    L.next = node


def insertion_sort(L):
    sorted = Node()
    L = L.next
    while L is not None:
        next = L.next
        insert_to_list(sorted, L)
        L = next
    return sorted


L = tab_to_list([1, 6, 3, 4, 8, 11, 64, 2, 27])
print_all(insertion_sort(L))