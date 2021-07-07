def partition(T, l, r):
    pivot = T[r]
    i = l
    for j in range(l, r):
        if T[j] < pivot:
            T[i], T[j] = T[j], T[i]
            i += 1
    T[i], T[r] = T[r], T[i]
    return i


def quickselect(T, left, right, k):
    if left == right:
        return T[left]
    pivot = partition(T, left, right)
    if pivot == k:
        return
    elif pivot < k:
        return quickselect(T, pivot + 1, right, k)
    else:
        return quickselect(T, left, pivot - 1, k)


def section(T, p, q):
    quickselect(T, 0, len(T) - 1, p)
    quickselect(T, p, len(T) - 1, q)
    selected = [0] * (q - p + 1)
    for i in range(q - p + 1):
        selected[i] = T[p + i]
    return selected


heights = [172, 168, 185, 193, 177, 178, 169, 180, 182]
selected = section(heights, 2, 3)
print(selected)