def tower(A):
    n = len(A)

    f = [1] * n

    for i in range(n):
        for j in range(i):
            if A[i][0] >= A[j][0] and A[i][1] <= A[j][1] and f[j] + 1 > f[i]:
                f[i] = f[j] + 1

    return max(f)


A = [(1,4),(0,5),(1,5),(2,6),(2,4)]
print(tower(A))
A = [(10,15),(8,14),(1,6),(3,10),(8,11),(6,15)]
print(tower(A))