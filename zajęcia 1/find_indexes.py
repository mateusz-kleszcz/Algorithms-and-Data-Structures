def find_indexes(tab, x):
    left = 0
    right = len(tab) - 1
    while left < right:
        if tab[left] + tab[right] < x:
            left += 1
        elif tab[left] + tab[right] > x:
            right -= 1
        else:
            return left, right
    return -1


tab = [1, 2, 3, 5, 6, 7, 8, 17]
print(find_indexes(tab, 12))