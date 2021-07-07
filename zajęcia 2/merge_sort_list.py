class Node:
    def __init__(self):
        self.value = None
        self.next = None


def print_list(L):
    while L is not None:
        print(L.value, end='->')
        L = L.next
    print()


def insert_to_node(node, L):
    start = L
    while L.next is not None:
        L = L.next

    node.next = None
    L.next = node
    return start


def split_list(L):
    mid = L.next
    prev_mid = L
    end = L.next
    while end is not None:
        end = end.next
        if end is not None:
            prev_mid = prev_mid.next
            end = end.next
            mid = mid.next
    prev_mid.next = None
    return L.next, mid


def merge(L1, L2):
    result = Node()
    L1 = L1.next
    L2 = L2.next
    if L1 is None:
        return L2
    if L2 is None:
        return L1
    while L1 is not None and L2 is not None:
        tmp = Node()
        if L1.value <= L2.value:
            tmp.value = L1.value
            insert_to_node(tmp, result)
            L1 = L1.next
        else:
            tmp.value = L2.value
            insert_to_node(tmp, result)
            L2 = L2.next
    while L1 is not None:
        tmp = Node()
        tmp.value = L1.value
        insert_to_node(tmp, result)
        L1 = L1.next
    while L2 is not None:
        tmp = Node()
        tmp.value = L2.value
        insert_to_node(tmp, result)
        L2 = L2.next
    return result


def merge_sort(L):
    if L.next is None:
        return L
    if L.next.next is None:
        return L
    a, b = split_list(L)
    L1 = Node()
    L1.next = a
    L2 = Node()
    L2.next = b
    left = merge_sort(L1)
    right = merge_sort(L2)
    merged = merge(left, right)
    return merged


L = Node()
new_node = Node()
new_node.value = 2
L.next = new_node
new = Node()
new.value = 7
new_node.next = new
a = Node()
a.value = 3
insert_to_node(a, L)
b = Node()
b.value = 1
insert_to_node(b, L)
c = Node()
c.value = 6
insert_to_node(c, L)
d = Node()
insert_to_node(d, L)
d.value = 11

print_list(L)
sorted = merge_sort(L)
print_list(sorted)