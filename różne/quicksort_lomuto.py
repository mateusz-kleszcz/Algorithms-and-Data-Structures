def partition(tab, left, right):
    pivot = tab[right]
    i = left - 1
    for j in range(left, right):
        if tab[j] < pivot:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i + 1], tab[right] = tab[right], tab[i + 1]
    return i + 1


def quicksort(tab, left, right):
    if left < right:
        pivot = partition(tab, left, right)
        quicksort(tab, left, pivot - 1)
        quicksort(tab, pivot + 1, right)


tab = [5,4,3,2,7]
quicksort(tab, 0, len(tab) - 1)
print(tab)