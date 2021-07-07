# każdy ciąg liter mogę zamienić na liczbę, skoro zakładamy że ciąg składa się wyłącznie z liter a i b
# to ciąg liter a i b możemy potraktować jak ciąg binarny 0 i 1
# maksymalna wartość jaką możemy uzyskać to 2^k - 1
# tworzymy tablicę długości 2^k, będzie to tablica liczników
# bierzemy pierwszy podciąg długości k i traktując go jak ciąg 0 i 1 zamieniamy go na liczbę w systemie dziesiętnym
# następny podciąg tworzymy w ten sposób, że bierzemy poprzednią liczbę, jeżeli na jej początku stało a to odejmujemy 2^(k-1)
# mnożymy ją przez 2 i dodajemy wartość następnęgo znaku
# np. dla k = 3 i ciągu znaków bbab pierwszy podciąg to bba -> 110(2) = 6(10), następny podciąg to bab, czyli "odcinamy" b na początku
# i dodajemy b na końcu
# w ten sposób możemy utworzyć liczby ze wszystkich podciągów w czasie liniowym O(n)
# gdybyśmy tworzyli je za każdym razem od nowa to złożoność wynosiłaby O(n + k)
# po utworzeniu każdej liczby zwiększamy jej wartość w tablicy długości 2^k którą utworzyliśmy na początku (początek algorytmu counting sort)
# ponownie przechodzimy pętlą i zamieniamy kolejne podciągi na liczby, tym razem jednak nie zwiększamy wartości liczników
# tylko sprawdzamy owe wartości i szukamy która jest największa, ponownie ma to złożoność O(n)
# znalezioną liczbę mogę odtworzyć na ciąg znaków
# złożoność tego algorytmu to O(n) - nie muszę przechodzić przez tablicę wielkości 2^k
# algorytm wymaga dodatkowe O(2^k) pamięci

def countNewValue(s, E, k, prev, i):
    firstLetterOfPrev = ord(s[i - k]) - 97
    firstLetterValue = firstLetterOfPrev * (E ** (k - 1))
    newLetterValue = (ord(s[i]) - 97)
    new = (prev - firstLetterValue) * E + newLetterValue
    return new


def find(s, k):
    E = 2 #długość alfabetu, tak gdyby nie robić tylko liter a i b xd
    counters = [0] * (E ** k)
    n = len(s)

    first = 0
    for i in range(k):
        first += (ord(s[i]) - 97) * (E ** (k - i - 1))
    counters[first] += 1

    prev = first
    for i in range(k, n):
        new = countNewValue(s, E, k, prev, i)
        counters[new] += 1
        prev = new

    prev = first
    maxNum = first

    for i in range(k, n):
        new = countNewValue(s, E, k, prev, i)
        prev = new
        if counters[new] > counters[maxNum]:
            maxNum = new

    string = ''

    while maxNum > 0:
        char = chr(maxNum % E + 97)
        string = char + string
        maxNum //= E

    while (len(string) < k):
        string = 'a' +string

    return string


string = 'aabaabaabba'
k = 3
print(find(string, k))