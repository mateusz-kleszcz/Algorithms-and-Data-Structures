def count_amount_of_numbers(num):
    T = [0] * 10
    while num > 0:
        digit = num % 10
        T[digit] += 1
        num //= 10
    one = 0
    more = 0
    for i in range(10):
        if T[i] == 1:
            one += 1
        elif T[i] > 1:
            more += 1
    return one, more


def pretty_sort(T):
    n = len(T)
    pretty = [0] * n
    for i in range(n):
        one, more = count_amount_of_numbers(T[i])
        pretty[i] = (T[i], one, more)

    counters = [0] * 11
    for el in pretty:
        counters[el[2]] += 1
    for i in range(1, 11):
        counters[i] += counters[i - 1]

    sorted = [0] * n
    for i in range(n - 1, -1, -1):
        more = pretty[i][2]
        counters[more] -= 1
        sorted[counters[more]] = pretty[i]

    for i in range(11):
        counters[i] = 0
    for el in sorted:
        counters[el[1]] -= 1
    for i in range(1, 11):
        counters[i] += counters[i - 1]
    for i in range(11):
        counters[i] += n

    for i in range(n):
        one = sorted[i][1]
        T[counters[one]] = sorted[i][0]
        counters[one] += 1


T = [67333, 455, 123, 2344, 114577, 1266]
pretty_sort(T)
print(T)