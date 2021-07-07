def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        mini = i
        for j in range(i, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]


arr = [2, 5, 8, 1, 0]
selectionSort(arr)
print(arr)


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + "->" + str(self.next)


def tab_to_lista(tab):
    head = Node("!")
    last = head
    for i in tab:
        last.next = Node(i, None)
        last = last.next
    return head


# zalozenie z wartownikiem
def insertionSort(head):
    nowa = Node("!")
    p = head.next
    while p != None:
        head.next = head.next.next
        cp, cp2 = nowa, nowa.next
        while cp2 != None and p.val > cp2.val:
            cp, cp2 = cp2, cp2.next
        cp.next = p
        p.next = cp2
        p = head.next
    return nowa


def bubbleSort(head):
    if head == None:
        return None
    if head.next == None:
        return head
    marker = head
    while marker:
        marker = marker.next
        back = head.next
        front = head.next.next
        while front:
            if back.val > front.val:
                front.val, back.val = back.val, front.val
            back = back.next
            front = front.next
    return head


tab = [0, 4, 2]
lista = tab_to_lista(tab)
print(tab)
print(lista)
print(bubbleSort(lista))


def maxi_mini(arr):
    maxi = mini = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > maxi:
            maxi = arr[i]
        elif arr[i] < mini:
            mini = arr[i]
    return maxi, mini


def binary_search(arr, num):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < num:
            left = mid + 1
        elif arr[mid] > num:
            right = mid - 1
        else:
            return mid
    return -1


def sum2(x, tabl):
    l = 0
    r = len(tabl) - 1
    while l != r:
        if tabl[l] + tabl[r] == x:
            return l, r
        elif tabl[l] + tabl[r] > x:
            r -= 1
        else:
            l += 1
    return -1


# parking space

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, values):
        self.head = self.tail = None
        self.length = 0
        if values:
            self.extend(values)

    def __len__(self):
        return self.length

    def append(self, val):
        node = Node(val)
        if not self:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def extend(self, values):
        for val in values:
            self.append(val)


def reverse(ll):
    curr = self.head

    while curr.next:
        temp = curr.next
        curr.next = curr


lst = LinkedList([1, 4, 2, 1, 3, 4])
















