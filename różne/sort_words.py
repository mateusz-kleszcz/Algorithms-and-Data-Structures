def getMaxLength(tab):
    maxLen = 0
    for el in tab:
        if len(el) > maxLen:
            maxLen = len(el)
    return maxLen


def countingSort(T, p):
    n = len(T)

    counters = [0] * 26
    for el in T:
        charNum = ord(el[p])
        counters[charNum - 97] += 1
    for i in range(1, 26):
        counters[i] += counters[i - 1]


    return sorted


def sortWords(T):
    maxLength = getMaxLength(T)
    sorted = T
    for i in range(maxLength):
        sorted = countingSort(sorted, i)
        print(sorted)
    return sorted


tab = ['aabb', 'baaca', 'bsda', 'asdf', 'safdfafs']
sort = sortWords(tab)
print(sort)