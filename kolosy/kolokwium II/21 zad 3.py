from queue import PriorityQueue
from zad3testy import runtests

def getFuel(T, u, v, i, j):

    if T[i][j] == 0:
        return 0

    value = T[i][j]
    T[i][j] = 0

    if i + 1 >= 0 and i + 1 < v and T[i + 1][j] > 0:
        value += getFuel(T, u, v, i + 1, j)
    if i - 1 >= 0 and i - 1 < v and T[i - 1][j] > 0:
        value += getFuel(T, u, v, i - 1, j)
    if j + 1 >= 0 and j + 1 < v and T[i][j + 1] > 0:
        value += getFuel(T, u, v, i, j + 1)
    if j - 1 >= 0 and j - 1 < v and T[i][j - 1] > 0:
        value += getFuel(T, u, v, i, j - 1)

    return value


def plan(T):
    u = len(T[0])
    v = len(T)

    values = [0] * u

    for i in range(u):
        values[i] = getFuel(T, u, v, 0, i)

    result = []
    q = PriorityQueue()
    fuel = 0
    for i in range(u - 1):
        if values[i] > 0:
            q.put((-values[i], i))
        if fuel <= 0:
            if not q.empty():
                value, index = q.get()
                fuel += abs(value)
                result.append(index)
        fuel -= 1

    result.sort()
    return result


runtests(plan)