class FastListNode:
    def __init__(self, a):
        self.a = a # przechowywana liczba całkowita
        self.next = [] # lista odsyłaczy do innych elementów; początkowo pusta
    def __str__(self): # zwraca zawartość węzła w postaci napisu
        res = 'a: ' + str(self.a) + '\t' + 'next keys: '
        res += str([n.a for n in self.next])
        return res


def fast_list_prepend(L, a):

    counter = 1
    while counter - 1 <= len(L.next):
        a.next.append(L)
        L = L.next[counter - 1]
        counter += 1

    a.next.append(L)

    return a


b = FastListNode(3)
c = FastListNode(4)
d = FastListNode(9)
e = FastListNode(12)
f = FastListNode(21)
g = FastListNode(103)
h = FastListNode(107)
i = FastListNode(119)
b.next = [c, d, f]
c.next = [d, e, g]
d.next = [e, f, h]
e.next = [f, g, i]
f.next = [g, h]
g.next = [h, i]
h.next = [i]

a = FastListNode(1)

print(fast_list_prepend(b, a).__str__())