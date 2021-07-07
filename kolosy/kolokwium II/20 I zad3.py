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

    f = [0] * k
    for i in range(k):
        counter = 0
        maximum = 0
        for j in range(n):
            if A[j] == values[i]:
                if counter > maximum:
                    maximum = counter
                counter = 0
            else:
                counter += 1
        if counter > maximum:
            maximum = counter
        f[i] = maximum

    return max(f)


A = [1,100, 5, 100, 1, 5, 1, 5]
print(longest_incomplete(A, 3))