class Node:
    def __init__(self):
        self.value = Node
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


def getTail(L):
    curr = L
    while curr.next is not None:
        curr = curr.next

    return curr


def partition(L):
    pivot = getTail(L) # pivotem niech będzie ostatni elemnt listy

    prev = None
    curr = L
    HL = None # wskaźnik na to co jest mniejsze od pivota
    TP = pivot # wskaźnik na elemnty równe pivotowi
    HR = Node() # wskaźnik na to co będzie większe od pivota
    TR = HR # ogon tego co będzie większe od pivota
    while curr is not pivot:
        # szukamy pierwszej mniejszej od pivota wartości w liście, będzie ona nową głową
        if curr.value < pivot.value:
            if HL is None:
                HL = curr
            prev = curr
            curr = curr.next
        # jeżeli wartości są równe to przepinam element za pivota
        elif curr.value == pivot.value:
            tmp = curr.next
            curr.next = None
            TP.next = curr
            TP = TP.next
            if prev is not None: prev.next = tmp
            curr = tmp
        # jeżeli wartości są większe to przepinam je na koniec listy
        else:
            tmp = curr.next
            curr.next = None
            TR.next = curr
            TR = TR.next
            if prev is not None: prev.next = tmp
            curr = tmp

    # zainicjowałem HR jako pusty wskaźnik na początku, cała lista z elementami większymi od pivota zaczyna się od 2 elementu
    HR = HR.next
    # do HL jest też podpięty wskaźnik z elementami równymi pivot, a w HL chcę mieć elementy tylko mniejsze
    if prev is not None: prev.next = None
    return HL, pivot, HR


def quicksort(head):
    # warunek brzegowy rekurencji, lista ma jeden element, albo dostaliśmy pustą listę na starcie
    if head is None or head.next is None:
        return head

    #wskaźnik na nowo utworzoną listę
    newHead = None
    HL, pivot, HR = partition(head)
    # jeżeli HL nie ma fragmentów albo jest równy pivotowi to nie musimy już sortować lewej części
    if HL is not None and HL is not pivot:
        newHead = quicksort(HL)

    # podpinam el równe pivotowi do listy wynikowej
    if newHead is not None:
        getTail(newHead).next = pivot
    else:
        newHead = pivot

    # sortuję prawą część i podpinam do listy wynikowej
    if HR is not None:
        getTail(newHead).next = quicksort(HR)

    return newHead


tab = [0, 2, 2, 2, 4, 2, 2]
L = tab2list(tab)
S = quicksort(L)
printList(S)