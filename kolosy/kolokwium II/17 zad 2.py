def goodThief(A, n):

    f = [0] * n
    f[0] = A[0]
    f[1] = max(A[0], A[1])

    for i in range(2, n):
        f[i] = max(f[i - 2] + A[i], f[i - 1])

    return f[n - 1]