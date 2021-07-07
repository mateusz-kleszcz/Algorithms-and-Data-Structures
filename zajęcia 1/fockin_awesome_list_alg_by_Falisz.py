class Node:
    def __init__(self):
        self.value = None
        self.next = None


def print_list(L):
    if L is not None:
        print(L.value, end=' ')
        print_list(L.next)


def insert_to_node(node, L):
    start = L
    while L.next is not None and L.next.value < node.value:
        L = L.next

    node.next = L.next
    L.next = node
    return start


def del_max(L):
    max_curr = L.next
    max_prev = L
    prev = L
    while prev.next is not None:
        if prev.next.value > max_curr.value:
            max_prev = prev
            max_curr = prev.next
        prev = prev.next
    max_prev.next = max_curr.next
    return L


def reverse(L):
    if L is None:
        return

    prev = None
    nxt = L.next
    while L is not None:
        L.next = prev
        prev = L
        L = nxt
        if nxt is not None:
            nxt = nxt.next
    return prev


L = Node()
new_node = Node()
new_node.value = 2
L.next = new_node
new = Node()
new.value = 5
new_node.next = new
a = Node()
a.value = 1
insert_to_node(a, L)
b = Node()
b.value = 3
insert_to_node(b, L)
c = Node()
c.value = 7
insert_to_node(c, L)
print_list(rev(L))