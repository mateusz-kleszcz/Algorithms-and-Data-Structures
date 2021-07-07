def word(S, t):
    n = len(t)
    f = [-float('inf')] * n

    for i in range(n):
        for s in S:
            substr = t[i - len(s): i]
            if i > len(s):
                if s == substr:
                    f[i] = max(f[i], min(len(s), f[i - len(s)]))
            elif i == len(s):
                if s == substr:
                    f[i] = max(f[i], len(s))

    print(f)


print(word(['ab', 'abab', 'ba', 'bab', 'b'], 'ababbab'))