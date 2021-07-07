# 1. dzielimy ciąg na n - k + 1 podciągów - są to wszystkie możliwe podciągi
# bierzemy n - ty z kolei znak i kolejne k - 1 znaków (złożoność O((n - k + 1) * k) ~ O(k*n)
# 2. sortujemy wszystkie podciągi pozycyjnie (złożoność O(k(n + 2)) ~ O(k*n)
# 3. kolejne podciągi jeżeli są identyczne to występują po sobie
# sprawdzamy po kolei który podciąg występuje najwięcej razy po sobie O(n)

def countingSort(T, index):
    n = len(T)
    counters = [0] * 2
    for el in T:
        counters[ord(el[index]) - 97] += 1

    counters[1] += counters[0]

    sorted = [0] * n
    for i in range(n):
        nr = ord(T[i][index]) - 97
        counters[nr] -= 1
        sorted[counters[nr]] = T[i]

    return sorted


def find(seq, k):
    n = len(seq)
    subNum = n - k + 1
    subs = [0] * subNum
    for i in range(subNum):
        s = ''
        for j in range(k):
            s += seq[i + j]
        subs[i] = s

    for i in range(k):
        subs = countingSort(subs, i)

    max = 1
    maxSub = subs[0]
    counter = 1
    for i in range(1, subNum):
        if subs[i] == subs[i - 1]:
            counter += 1
        elif counter > max:
            max = counter
            maxSub = subs[i - 1]
            counter = 1

    return maxSub


sequence = 'ababaaaabb'
k = 3
print(find(sequence, k))