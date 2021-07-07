from math import log

def insertion(tab):
    n = len(tab)
    for i in range(1, n):
        key = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > key:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key
    return tab


def fast_sum(tab, a):
    n = len(tab)

    # tworzę n kubełków
    buckets = [[] for _ in range(n)]

    for i in range(n):
        value = tab[i]
        x = log(value, a)
        index = int(x * n)
        buckets[index].append(value)

    result = []

    for bucket in buckets:
        insertion(bucket)
        result += bucket

    return result


T1 = [0.1, 0.5, 0.2, 0.78, 0.01 ]
T2 = [0.9, 0.7, 0.7, 0.5, 0.3, 0.2, 0.9]
T3 = [0.1, 0.9,0.2,0.8,0.3,0.7,0.4,0.6]

D1 = [2**x for x in T1]
D2 = [2**x for x in T2]
D3 = [3**x for x in T3]
print(fast_sum(D1, 2))
print(fast_sum(D2, 2))
print(fast_sum(D3, 3))