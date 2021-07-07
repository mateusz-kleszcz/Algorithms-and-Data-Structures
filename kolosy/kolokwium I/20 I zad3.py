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


def longest_incomplete(A, k):
    n = len(A)

    values = [0] * k
    counter = -1
    for el in A:
        x = binary_search(values, el)
        if x == -1:
            j = counter
            values[counter + 1] = el
            while j >= 0 and values[j] > el:
                values[j + 1] = values[j]
                j -= 1
            values[j + 1] = el
            counter += 1

    counters = [0] * k
    i = 0
    j = 0
    counter = 0
    maxLength = 0
    length = 0
    for j in range(n):
        x = binary_search(values, A[j])
        if counters[x] == 0: counter += 1
        counters[x] += 1
        if counter == k:
            y = binary_search(values, A[i])
            while counters[y] > 0:
                i += 1
                length -= 1
                counters[y] -= 1
                if counters[y] == 0: break
                y = binary_search(values, A[i])
            counter -= 1

        length += 1
        if maxLength < length:
            maxLength = length

    return maxLength


A = [1, 100, 5, 100, 1, 5, 1, 5]
print(longest_incomplete(A, 3))