from random import randint, seed


class Node:
  def __init__(self):
    self.next = None
    self.value = None


def getTail(L):
    curr = L
    while curr.next is not None:
      curr = curr.next

    return curr


def partition(L):
  pivot = getTail(L)  # pivotem niech będzie ostatni elemnt listy

  prev = None
  curr = L
  HL = None  # wskaźnik na to co jest mniejsze od pivota
  TP = pivot # wskaźnik na miejsce gdzie przepinamy elementy równe pivotowi
  HR = Node()  # wskaźnik na to co będzie większe od pivota
  TR = HR  # ogon tego co będzie większe od pivota
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

  # zwracam podzieloną listę na el mniejsze, równe i większe
  return HL, pivot, HR


def qsort( L ):
  # print("Tu proszę napisać swoją funckję")

  # warunek brzegowy rekurencji, lista ma jeden element, albo dostaliśmy pustą listę na starcie
  if L is None or L.next is None:
    return L

  # wskaźnik na nowo utworzoną listę
  newHead = None
  HL, pivot, HR = partition(L)

  # jeżeli HL nie ma fragmentów albo jest równy pivotowi to nie musimy już sortować lewej części
  if HL is not None and HL is not pivot:
    newHead = qsort(HL)

  # podpinam el równe pivotowi do listy wynikowej
  if newHead is not None:
    getTail(newHead).next = pivot
  else:
    newHead = pivot

  # sortuję prawą część i podpinam do listy wynikowej
  if HR is not None:
    getTail(newHead).next = qsort(HR)

  L = newHead
  return L


def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next
  
  
def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")

  
  
  

seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]
L = tab2list( T )

print("przed sortowaniem: L =", end=" ")
printlist(L) 
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
  print("List jest pusta, a nie powinna!")
  exit(0)

P = L
while P.next != None:
  if P.value > P.next.value:
    print("Błąd sortowania")
    exit(0)
  P = P.next
    
print("OK")

