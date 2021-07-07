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


def divide(L):
    L1 = Node()
    L2 = Node()
    head1 = L1
    head2 = L2
    L = L.next
    isFirst = True
    while L is not None:
        if isFirst:
            L1.next = L
            L1 = L1.next
            isFirst = False
        else:
            L2.next = L
            L2 = L2.next
            isFirst = True
        L = L.next
    L1.next = None
    L2.next = None
    print_list(head1)
    print()
    print_list(head2)


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
print_list(L)
print()
divide(L)