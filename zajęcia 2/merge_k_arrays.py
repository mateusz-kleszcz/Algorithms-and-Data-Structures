def merge(T1, T2):
    i = 0
    j = 0
    n1 = len(T1)
    n2 = len(T2)
    T = [0] * (n1 + n2)
    while i < n1 and j < n2:
        if T1[i] < T2[j]:
            T[i + j] = T1[i]
            i += 1
        elif T1[i] >= T2[j]:
            T[i + j] = T2[j]
            j += 1
    while i < n1:
        T[i + j] = T1[i]
        i += 1
    while j < n2:
        T[i + j] = T2[j]
        j += 1
    return T


def merge_arrays(T):
    series_length = 1
    n = len(T)
    while series_length <= n:
        n = len(T)
        if n % 2:
            merged = [0] * (n // 2 + 1)
        else:
            merged = [0] * (n // 2)
        for i in range(0, n, 2):
            if i + 1 >= n:
                merged[i // 2] = T[i]
            else:
                merged[i // 2] = merge(T[i], T[i + 1])
        T = merged
        series_length *= 2
    return T


t = [[12, 321], [11, 17], [3, 15]]
T = merge_arrays(t)
print(T)