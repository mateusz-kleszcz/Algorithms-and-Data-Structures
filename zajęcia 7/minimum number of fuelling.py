def fueling(l, S):
    n = len(S)

    i = -1
    counter = 0
    lastFuelling = 0
    T = []

    while i < n - 2:
        if S[i + 1] - lastFuelling > l:
            return -1
        while S[i + 1] - lastFuelling <= l:
            i += 1
        counter += 1
        lastFuelling = S[i]
        T.append(S[i])

    if S[i + 1] - lastFuelling > l:
        return -1

    return counter, T


l = 8
S = [2, 3, 4, 5, 7, 9, 11, 13, 17, 25]
P = [7, 3, 1, 15, 9]
print(fueling(l, S))