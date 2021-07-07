def binary_search_recursively(tab, x, left, right):
    mid = (left + right) // 2
    if tab[mid] == x:
        return mid
    if left > right:
        return -1
    if tab[mid] > x:
        return binary_search_recursively(tab, x, left, mid - 1)
    elif tab[mid] < x:
        return binary_search_recursively(tab, x, mid + 1, right)


def binary_search(tab, x):
    left = 0
    right = len(tab) - 1
    while left <= right:
        mid = (left + right) // 2
        if tab[mid] > x:
            right = mid - 1
        elif tab[mid] < x:
            left = mid + 1
        else:
            return mid
    return -1


tab = [0, 2, 4, 5, 7, 8, 9, 4, 5]
print(binary_search_recursively(tab, 8, 0, len(tab) - 1))