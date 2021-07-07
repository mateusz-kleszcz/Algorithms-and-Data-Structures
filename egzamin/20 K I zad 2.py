class FastListNode:
    def __init__(self, a):
        self.a = a # przechowywana liczba całkowita
        self.next = [] # lista odsyłaczy do innych elementów; początkowo pusta
    def __str__(self): # zwraca zawartość węzła w postaci napisu
        res = 'a: ' + str(self.a) + '\t' + 'next keys: '
        res += str([n.a for n in self.next])
        return res


def fast_list_prepend(L, a):

    first = FastListNode(a)

    if L is None:
        return FastListNode(a)

    counter = 0
    while True:
        first.next.append(L)
        if counter >= len(L.next):
            break
        L = L.next[counter]
        counter += 1

    return first