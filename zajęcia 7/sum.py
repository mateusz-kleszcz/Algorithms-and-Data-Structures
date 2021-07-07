def sum(t):
    n = len(t)
    if n % 2:
        return t[n // 2]
    else:
        return (t[n // 2 - 1] + t[n // 2]) / 2