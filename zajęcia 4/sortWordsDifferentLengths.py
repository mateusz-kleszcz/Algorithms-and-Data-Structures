def countingSort(T, maxLen, k):
    n = len(T)

    counters = [0] * 26
    for el in T:
        counters[ord(el[k - 1]) - 97] += 1
    for i in range(1, 26):
        counters[i] += counters[i - 1]

    sorted = [0] * n
    for i in range(n - 1, -1, -1):
        index = ord(T[i][k - 1]) - 97
        counters[index] -= 1
        sorted[counters[index]] = T[i]

    return sorted


def sortWords(T):
    n = len(T)
    maxLen = 0
    for el in T:
        if len(el) > maxLen:
            maxLen = len(el)

    wordsToSort = []
    for i in range(maxLen, 0, -1):
        for el in T:
            if len(el) == i:
                wordsToSort.append(el)
        wordsToSort = countingSort(wordsToSort, maxLen, i)

    return wordsToSort



words = ['aab', 'baaad', 'sagh', 'aaaaaa', 'asdf', 'a']
print(sortWords(words))