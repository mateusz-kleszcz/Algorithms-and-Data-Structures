# f(i, j) - minimalna liczba skoków żeby dotrzeć do pola i oraz mieć j jednostek energii PRZED zjedzeniem smakołyka
# f(i, j) = min 0 <= k < i {f(k, j + i - k + A[k]}
# rozwiązanie to najmniejsze z f(n - 1, k), gdzie 0 <= k < n
# rozwiązanie ze spamiętywaniem bo nie znamy kolejności w jakiej żab będzie skakał

def memoized(f, A, i, j):
    n = len(A)

    if i == 0 and j == 0:
        return 0

    if f[i][j] is not None:
        return f[i][j]

    minJumps = float('inf')
    for k in range(i):
        energyInK = j + i - k - A[k]
        # zabezpieczenie przed tym, żeby żaba wykonała skok z ujemną energią na pole i
        # ale spadając wpierdoliła smakołyka i jej energia była większa od 0
        if energyInK >= i - k - A[k] and energyInK < n:
            value = memoized(f, A, k, energyInK) + 1
            if value < minJumps:
                minJumps = value

    f[i][j] = minJumps

    return f[i][j]


def zbigniew(A):
    n = len(A)

    f = [[None] * n for _ in range(n)]

    f[0][0] = 0

    for i in range(n):
        memoized(f, A, n - 1, i)

    return min(f[n - 1])