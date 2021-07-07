from random import randint, seed


def merge(tab, left, right, pivot):
    #pomocniczy podział na 2 podzbiory
    n1 = pivot - left + 1
    t1 = [0] * n1
    for i in range(n1):
        t1[i] = tab[i + left]
    n2 = right - pivot
    t2 = [0] * n2
    for i in range(n2):
        t2[i] = tab[i + pivot + 1]
    #utworzenie wskaźników
    i = 0 # na początek pierwszej tablicy
    j = 0 # na początek drugiej tablicy
    q = left # na początek tablicy wynikowej
    # scalanie dwóch zbiorów (biorę mniejszy z początkowych elementów tablicy t1, t2 i wstawiam go do tablicy wyjściowej)
    while i < n1 and j < n2:
        if t1[i] < t2[j]:
            tab[q] = t1[i]
            i += 1
        else:
            tab[q] = t2[j]
            j += 1
        q += 1
    # któryś podzbiór może być dłuższy, jeżeli coś zostało to przepisuję do tablicy wynikowej
    while i < n1:
        tab[q] = t1[i]
        q += 1
        i += 1
    while i < n2:
        tab[q] = t2[i]
        q += 1
        i += 1


def sort(tab, left, right):
    if left < right:
        pivot = (left + right) // 2
        sort(tab, left, pivot)
        sort(tab, pivot + 1, right)
        merge(tab, left, right, pivot)


def mergesort(T):
     n = len(T) - 1
     sort(T, 0, n)
     return T


seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]

print("przed sortowaniem: T =", T) 
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T)-1):
  if T[i] > T[i+1]:
    print("Błąd sortowania!")
    exit()
    
print("OK")