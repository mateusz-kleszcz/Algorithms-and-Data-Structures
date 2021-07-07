def partition(T, left, right):
    pivot = T[right]
    i = left
    for j in range(left, right):
        if T[j] < pivot:
            T[i], T[j] = T[j], T[i]
            i += 1
    T[i], T[right] = T[right], T[i]
    return i


def quickselect(T, left, right, k):
    if left == right:
        return T[left]

    pivot = partition(T, left, right)

    if k == pivot:
        return T[k]
    elif k > pivot:
        return quickselect(T, pivot + 1, right, k)
    else:
        return quickselect(T, left, pivot - 1, k)


tab = [3, 8, 0, 1, 9, 4, 6, 2, 10, 7, 5, 11, 13, 14, 16, 12, 15, 17, 19, 18]
print(quickselect(tab, 0, len(tab) - 1, 9))