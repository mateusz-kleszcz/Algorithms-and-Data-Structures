def count(num):
    nums = [0] * 10
    while num > 0:
        digit = num % 10
        nums[digit] += 1
        num //= 10

    one = 0
    more = 0
    for el in nums:
        if el == 1:
            one += 1
        elif el > 1:
            more += 1

    return one, more


def reverse(T):
    n = len(T)
    for i in range(n // 2):
        T[i], T[n - i - 1] = T[n - i - 1], T[i]


def counting_sort(T, k):
    n = len(T)
    counters = [0] * 11

    for i in range(n):
        el = T[i][k]
        counters[el] += 1
    for i in range(1, 11):
        counters[i] += counters[i - 1]

    sorted = [0] * n
    for i in range(n):
        el = T[i][k]
        counters[el] -= 1
        sorted[counters[el]] = T[i]

    return sorted


def pretty_sort(T):
    n = len(T)

    values = [0] * n
    for i in range(n):
        one, more = count(T[i])
        values[i] = (T[i], one, more)

    values = counting_sort(values, 2)
    reverse(values)
    values = counting_sort(values, 1)

    print(values)

    for i in range(n):
        T[i] = values[i][0]

    return T


tab = [114577, 455, 1266, 2344, 67333, 123]
pretty_sort(tab)
print(tab)