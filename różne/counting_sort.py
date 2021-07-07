#only for array from in this example 0..19
MAX = 20

def counting_sort(T):
    counters = [0] * MAX
    for el in T:
        counters[el] += 1
    for i in range(1, MAX):
        counters[i] += counters[i - 1]

    sortedTab = [0] * len(T)
    for i in range(len(T)):
        counters[T[i]] -= 1
        sortedTab[counters[T[i]]] = T[i]
    return sortedTab


tab = [1, 12, 11, 0, 0, 3, 5, 7, 11, 19, 7, 8, 7, 9, 4, 5]
print(counting_sort(tab))