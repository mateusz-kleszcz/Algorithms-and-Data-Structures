def trailer(t, k):
    n = len(t)
    t.sort(reverse=True)

    counter = 0
    weight = 0
    for i in range(n):
        if t[i] + weight <= k:
            counter += 1
            weight += t[i]

    return counter


t = [2, 2, 4, 8, 1, 8, 16]
print(trailer(t, 27))