def partition(tab, left, right):
    x = left + (right - left) // 2
    pivot = tab[x]
    i = left
    j = right
    while True:
        while tab[i] < pivot:
            i += 1
        while tab[j] > pivot:
            j -= 1
        if i >= j:
            return j
        tab[i], tab[j] = tab[j], tab[i]


def quicksort(tab, left, right):
    if left < right:
        pivot = partition(tab, left, right)
        quicksort(tab, left, pivot - 1)
        quicksort(tab, pivot + 1, right)


tab = [5,4,3,2,1]
quicksort(tab, 0, len(tab) - 1)
print(tab)