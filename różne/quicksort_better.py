def partition(tab, left, right):
    x = tab[right]
    i = left - 1
    for j in range(left, right):
        if tab[j] < x:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i + 1], tab[right] = tab[right], tab[i + 1]
    return i + 1


def quicksort(tab, left, right):
    while left < right:
        pivot = partition(tab, left, right)
        if (pivot - left) <= (right - pivot):
            quicksort(tab, left, pivot - 1)
            left = pivot + 1
        else:
            quicksort(tab, pivot + 1, right)
            right = pivot - 1


tab = [4, 2, 7, 3, 2, 1, 3, 7, 6, 9, 4, 2, 0]
quicksort(tab, 0, len(tab) - 1)
print(tab)