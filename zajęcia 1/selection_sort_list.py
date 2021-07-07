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


def selection_sort(L):
    L = L.next
    temp = L
    while temp is not None:
        min = temp
        curr = temp.next
        while curr is not None:
            if min.value > curr.value:
                min = curr
            curr = curr.next
        temp.value, min.value = min.value, temp.value
        temp = temp.next
    return L


L = tab_to_list([6, 3, 4, 8, 11, 64, 2, 27])
print_all(selection_sort(L))