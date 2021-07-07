# dzielimy tablicę na n równych przedziałów oraz obliczamy sumę elementów każdego z przedziałów
# wszystkie sumy wsadzamy do tablicy jako krotkę - pierwszy indeks to suma, drugi to numer przedziału
# sortujemy tablicę rosnąco po wartościach sumie dowolnym szybkim algorytmem sortującym (np. quicksort)
# tablica zawiera informacje które przedziały tworzą kolejne najmniejsze sumy - przepisujemy kolejno te przedziały do tablicy B
# obliczenie sumy i ma złożoność O(n^2), sortowanie O(nlogn), przepisanie do B O(n^2)
# cały algorytm ma złożoność O(n^2) i potrzebuje dodatkowe logn pamięci
# :D

from random import randint

def partition(T, l, r):
    x = T[r][0]
    i = l
    for j in range(l, r):
        if T[j][0] < x:
            T[i], T[j] = T[j], T[i]
            i += 1
    T[i], T[r] = T[r], T[i]
    return i


def quicksortTuples(T, l, r):
    while l < r:
        p = partition(T, l, r)
        if (p - l) < (r - p):
            quicksortTuples(T, l, p - 1)
            l = p + 1
        else:
            quicksortTuples(T, p + 1, r)
            r = p - 1


def sumSort(A, B, n):
    sums = [0] * n
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += A[i * n + j]
        sums[i] = (sum, i)
    quicksortTuples(sums, 0, n - 1)
    for i in range(n):
        index = sums[i][1]
        for j in range(n):
            B[i * n + j] = A[index * n + j]


n = 4
A = [randint(1, n ** 2) for _ in range(n ** 2)]
B = [0] * (n ** 2)
print(A)
sumSort(A, B, n)
print(B)