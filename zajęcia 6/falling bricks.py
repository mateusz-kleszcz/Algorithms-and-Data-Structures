def falling(bricks):
    n = len(bricks)
    F = [1] * n

    for i in range(1, n):
        for j in range(i):
            if bricks[i][0] >= bricks[j][0] and bricks[i][1] <= bricks[j][1] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1

    return n - max(F)


bricks = [(2, 6), (1, 7), (3, 5), (4, 4.5)]
print(falling(bricks))