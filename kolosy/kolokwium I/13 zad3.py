def count(counters, word):
    for char in word:
        i = ord(char)
        counters[i] += 1


def possible(u, v, w): #O(n + k)
    E = 256

    countersUandV = [0] * E
    count(countersUandV, u)
    count(countersUandV, v)

    counters = [0] * E
    count(counters, w)

    for i in range(E):
        if counters[i] > countersUandV[i]:
            return False

    return True


def betterPossible(u, v, w):
    E = 256

    if len(u) + len(v) < len(w):
        return False

    countersUandV = [0] * E
    count(countersUandV, u)
    count(countersUandV, v)

    countersW = [0] * E
    count(countersW, w)

    for i in range(len(w)):
        if countersW[ord(w[i])] > countersUandV[ord(w[i])]:
            return False

    return True


u = 'aaa'
v = 'aba'
w = 'aabaaa'
print(betterPossible(u, v, w))