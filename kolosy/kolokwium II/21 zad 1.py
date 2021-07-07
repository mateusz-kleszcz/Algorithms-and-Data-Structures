#wyszukiwanie binarne zmodyfikowane tak, aby szukało pierwszego elementu mniejszego od wartości x
def binary_search(arr, l, r, x):

    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid][0] == x:
            return arr[mid - 1][1]
        elif arr[mid][0] < x:
            l = mid + 1
        else:
            r = mid - 1

    return l - 1


def getSolution(F, T, prev, p, i, j):
    h, a, b, w = T[i]
    capacity = h * (b - a)
    if i < 0: return []
    if i == 0:
        if j >= w: return [0]
        return []
    if j >= w and F[i][j] == F[prev[i]][j - w] + capacity:
        return getSolution(F, T, prev, p, prev[i], j - w) + [i]
    return getSolution(F, T, prev, p, i - 1, j)


def select_buildings(T, p):
    n = len(T)

    TIndexes = sorted(range(n), key=lambda x: T[x][1])
    # sortuje budynki po początkach
    T.sort(key=lambda x:x[1])

    F = [[0] * (p + 1) for _ in range(n)]

    # znajduje binarnie budynek który nie nachodzi na i-ty
    ends = [(T[i][2], i) for i in range(n)]
    ends.sort()
    prev = [-1] * n
    for i in range(n):
        a = T[i][1]
        prev[i] = binary_search(ends, 0, n, a)

    h, a, b, w = T[0]
    capacity = h * (b - a)
    for i in range(w, p + 1):
        F[0][i] = capacity

    for i in range(1, n):
        #obliczam ile osób zmieści się w i-tym budynku
        h, a, b, w = T[i]
        capacity = h * (b - a)

        #tak jak w plecakowym problemie, sprawdzam czy opłaca się wybudować budynek
        #porównuję opłacalnośc nie z poprzednim elementem, a poprzednim który mogłem użyć
        for j in range(1, p + 1):
            F[i][j] = F[i - 1][j]
            if j >= w:
                if prev[i] == -1:
                    F[i][j] = max(F[i][j], capacity)
                else:
                    F[i][j] = max(F[i][j], F[prev[i]][j - w] + capacity)

    solution = getSolution(F, T, prev, p, n - 1, p)

    #odtworzenie oryginalnych indeksów
    solutionWithOriginalIndexes = []
    for i in solution:
        print(T[i])
        solutionWithOriginalIndexes.append(TIndexes[i])

    solutionWithOriginalIndexes.sort()

    return solutionWithOriginalIndexes


T = [(1,8,12,5),(4,7,8,2),(3,2,3,6),(9,7,8,5),(8,21,22,8),(5,4,7,10),(1,21,24,10),(7,14,16,1)]
p = 32

print(select_buildings(T, p))