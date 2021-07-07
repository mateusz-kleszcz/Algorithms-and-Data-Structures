def sections(t):
    n = len(t)
    t.sort()

    counter = 1
    minimum = t[0]
    for i in range(1, n):
        if t[i] >= minimum + 1:
            counter += 1
            minimum = t[i]

    return counter


t = [0.25, 0.5, 1.4]
print(sections(t))