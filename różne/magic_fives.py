def median5(tab):
    n = len(tab)
    for i in range(n):
        j = i
        while j > 0 and tab[j - 1] > tab[j]:
            tab[j - 1], tab[j] = tab[j], tab[j - 1]
            j -= 1
    if n % 2:
        return tab[n // 2]
    else:
        return (tab[n // 2 - 1] + tab[n // 2]) / 2


def medianMedians(tab):
    n = len(tab)
    if n <= 5:
        return median5(tab)
    medians = [0] * ((len(tab) + 4) // 5)
    for i in range(0, len(tab), 5):
        lenOfSubarray = 5 if i + 5 < len(tab) else len(tab) % 5
        t = [0] * lenOfSubarray
        for j in range(lenOfSubarray):
            t[j] = tab[i + j]
        medians[i // 5] = median5(t)
    return medianMedians(medians)


tab = [123, 12,3,12,312,12,312,123,31,23,12,3,124,124,123,124,124,12,4]
print(medianMedians(tab))