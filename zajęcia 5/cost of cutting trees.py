def cost(T):
    n = len(T)
    include2 = T[0] + T[1]
    include1 = T[1]
    exclude = T[0]
    for i in range(2, n):
        newExclude = max(exclude, include1, include2)
        include2 = include1 + T[i]
        include1 = exclude + T[i]
        exclude = newExclude
    return max(exclude, include1, include2)


# f(i, k) - największy koszt do i-tego elementu, jeżeli ostatnie k drzew było wycięte
# f(0, 0) = f(0, 1) = T[0]
# f(0, 2) = 0
# f(i, 0) = f(i - 1, 1) + T[i]
# f(i, 1) = f(i - 1, 2) + T[i]
# f(i, 2) = max(f(i - 1, 0), f(i - 1, 1), f(i - 1, 2))
# return max(f(n - 1, 0), f(n - 1, 1), f(n - 1, 2))
# złożoność: O(n * k) (w naszym przypadku k = 2 -> O(n)
def costDynamically(T):
    n = len(T)

    F = [[0] * 3 for _ in range(n)]
    F[0][0] = F[0][1] = T[0]
    F[0][2] = 0

    for i in range(n):
        F[i][0] = F[i - 1][1] + T[i]
        F[i][1] = F[i - 1][2] + T[i]
        F[i][2] = max(F[i - 1][0], F[i - 1][1], F[i - 1][2])

    return max(F[n - 1][0], F[n - 1][1], F[n - 1][2])


tab = [5, 5, 10, 40, 50, 35]
print(cost(tab))
print(costDynamically(tab))