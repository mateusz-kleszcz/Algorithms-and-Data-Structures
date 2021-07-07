def minimumCost(l, S, P):
    n = len(S)

    i = 0
    curr = 0
    currIndex = -1
    petrol = l
    cost = 0

    while i <= n - 1:

        minimum = float('inf')
        next = -1
        nextIndex = -1

        while S[i] - curr <= l:
            if P[i] <= minimum:
                minimum = P[i]
                next = S[i]
                nextIndex = i
            i += 1
            if i == n: break

        if curr != 0:
            if P[currIndex] < P[nextIndex]:
                cost += (l - petrol) * P[currIndex]
                petrol = l - (next - curr)
            else:
                cost += (next - curr - petrol) * P[currIndex]
                petrol = 0
        else: petrol -= next

        if nextIndex != n - 1:
            curr = next
            i = nextIndex + 1
            currIndex = nextIndex

    cost -= petrol * P[currIndex]

    return cost


# test 1
S = [2, 4, 6, 9, 11, 13, 16, 18, 20, 25]
C = [4, 3, 2, 3, 3, 5, 4, 2, 4, 4]
L = 7
print(minimumCost(L, S, C))
# result = 41
# ---------
# test 2
S = [1, 9, 15, 16, 17, 27, 28]
C = [1, 100, 10, 15, 1, 30, 30]
L = 14
# result: 32
# ---------
print(minimumCost(L, S, C))