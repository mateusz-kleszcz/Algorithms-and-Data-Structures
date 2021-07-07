from random import randint

def findMinSeqWithColors(T, k):
    n = len(T)
    counter = 0
    minJ = n - 1
    minI = 0
    colors = [0] * k
    i = 0

    for j in range(n):
        color = T[j]
        if colors[color] == 0:
            counter += 1
        colors[color] += 1
        if counter == k:
            while colors[T[i]] > 1:
                colors[T[i]] -= 1
                i += 1
            if minJ - minI > j - i:
                minJ = j
                minI = i

    return minI, minJ


A = [randint(0, 4) for _ in range(20)]
print(A)
print(findMinSeqWithColors(A, 5))