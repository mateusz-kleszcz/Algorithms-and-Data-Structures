from random import randint

def getMinAndMax(T):
    n = len(T)
    min = max = T[n - 1]

    for i in range(0, n - 1, 2):
        if T[i] < T[i + 1]:
            if T[i] < min:
                min = T[i]
            if T[i + 1] > max:
                max = T[i + 1]
        else:
            if T[i + 1] < min:
                min = T[i + 1]
            if T[i] > max:
                max = T[i]

    return min, max


def findMaxAdjacentDifference(T):

    min, max = getMinAndMax(T)
    n = len(T)

    buckets = [[] for _ in range(n)]
    minBuckets = [0 for _ in range(n)]
    maxBuckets = [0 for _ in range(n)]
    delta = (max - min) / n

    for el in T:
        if el == max:
            index = n - 1
        else:
            index = int((el - min) / delta)
        buckets[index].append(el)

    for i in range(n):
        if len(buckets[i]) != 0:
            min, max = getMinAndMax(buckets[i])
            minBuckets[i] = min
            maxBuckets[i] = max
        else:
            minBuckets[i] = -1
            maxBuckets[i] = -1

    maxDiff = -1
    j = 0
    for i in range(1, n):
        if maxBuckets[i] == -1: continue
        diff = minBuckets[i] - maxBuckets[j]
        if maxDiff < diff: maxDiff = diff
        j = i

    return maxDiff


tab = [12, 42, 54, 78, 93, 11, 15, 48]
print(findMaxAdjacentDifference(tab))