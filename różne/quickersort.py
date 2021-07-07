from random import randint

def partition(T, l, r):
    x = T[r]
    i = l - 1
    for j in range(l, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]

    pe = i + 1
    i = l - 1
    for j in range(l, pe):
        if T[j] < x:
            i += 1
            T[i], T[j] = T[j], T[i]

    return i + 1, pe


def quickersort(T, l, r):
    ps, pe = partition(T, l, r)
    if l < ps:
        quickersort(T, l, ps - 1)
    if pe < r:
        quickersort(T, pe + 1, r)


T = [randint(0, 10) for _ in range(100)]
print(T)
quickersort(T, 0, len(T) - 1)
print(T)