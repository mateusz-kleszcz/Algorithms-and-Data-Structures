def getMaxLength(T):
    maxLength = 0
    for el in T:
        if len(el) > maxLength:
            maxLength = len(el)
    return maxLength


def countingSort(T, k):
    n = len(T)
    E = 26
    counters = [0] * E
    for el in T:
        i = ord(el[k - 1]) - 97
        counters[i] += 1
    for i in range(1, E):
        counters[i] += counters[i - 1]

    sorted = [0] * n
    for i in range(n - 1, -1, -1):
        index = ord(T[i][k - 1]) - 97
        counters[index] -= 1
        sorted[counters[index]] = T[i]

    return sorted


def sortString(T):
    n = len(T)
    maxLen = getMaxLength(T)

    counters = [0] * maxLen
    for el in T:
        l = len(el) - 1
        counters[l] += 1
    for i in range(1, maxLen):
        counters[i] += counters[i - 1]

    sortedByLen = [0] * n
    for i in range(n - 1, -1, -1):
        l = len(T[i]) - 1
        counters[l] -= 1
        sortedByLen[counters[l]] = T[i]

    stringToSort = []
    lastIndex = n - 1
    for i in range(maxLen, 0, -1):
        newStrings = []
        while len(sortedByLen[lastIndex]) == i:
            newStrings += [sortedByLen[lastIndex]]
            lastIndex -= 1
        stringToSort = newStrings + stringToSort
        stringToSort = countingSort(stringToSort, i)

    return stringToSort


tab = ['aaa', 'a', 'b', 'adaaaa','aba', 'aab']
print(sortString(tab))