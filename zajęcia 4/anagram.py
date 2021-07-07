def isAnagram(A, B):
    counters = [0] * 26
    for char in A:
        index = ord(char) - 97
        counters[index] += 1

    for char in B:
        index = ord(char) - 97
        counters[index] -= 1

    for i in range(26):
        if counters[i] != 0:
            return False

    return True


a = 'aaaba'
b = 'baaaa'
print(isAnagram(a,b))