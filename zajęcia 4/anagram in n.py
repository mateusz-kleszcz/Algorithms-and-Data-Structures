def anangram(A, B, k):

    if len(A) != len(B):
        return False

    counters = [0] * k

    for char in A:
        i = ord(char)
        counters[i] += 1
    for char in B:
        i = ord(char)
        counters[i] -= 1

    for i in range(len(A)):
        index = ord(A[i])
        if counters[index] != 0:
            return False

    return True


a = 'aab'
b = 'aaa'
print(anangram(a, b, 256))