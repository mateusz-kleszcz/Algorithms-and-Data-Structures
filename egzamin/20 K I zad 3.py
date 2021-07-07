# złożoność O(nlogk)
# szukam najdłuższego ciągu który nie zawiera k liczb
# jeżeli liczba którą rozważam po dodaniu do ciągu sprawi że będzie on zawierał k liczb, to przesuwam początek mojego ciągu
# tak żeby po dodaniu tej liczby do ciągu nie zawierał on k liczb
# oraz sprawdzam czy długość podciągu który znalazłem nie była największa

from queue import Queue

def binary_search(tab, x):
    left = 0
    right = len(tab) - 1
    while left <= right:
        mid = (left + right) // 2
        if tab[mid] > x:
            right = mid - 1
        elif tab[mid] < x:
            left = mid + 1
        else:
            return mid
    return -1


def longest_incomplete(A, k):
    n = len(A)

    # mapowanie tablicy wartości, wszystkie wartości będę wyszukiwał binarnie
    # np wartości w A to 1, 100 i 5, czyli binary_search(values, 1) = 0, binary_search(values, 5) = 1, binary_serch(values, 100) = 2
    # zapewni mi to, że szukanie wartości będzie trwało logk a nie k
    values = [0] * k
    counter = -1
    for el in A:
        x = binary_search(values, el)
        if x == -1:
            j = counter
            values[counter + 1] = el
            while j >= 0 and values[j] > el:
                values[j + 1] = values[j]
                j -= 1
            values[j + 1] = el
            counter += 1

    counters = [0] * k # ile razy w ciągu powtórzyły się liczby
    lastIndexes = [-1] * k # ostatni indeks który już rozważyłem, na którym znajduje się liczba
    lastValues = Queue() # kolejka w której będę trzymał którą liczbę muszę usunąć z mojego podciągu, aby nie zawierał k liczb
    counter = 0 # ile z k liczb wykorzystałem w podciągu który rozważam
    maxLength = 0 # długość najdłuższego podciągu

    for i in range(n):
        # rozważam liczbe i znajduje jej zmapowany indeks
        num = A[i]
        x = binary_search(values, num)
        # jeżeli liczby nie ma jeszcze w moim podciągu który rozważam to zwiększam licznik liczb i dodaje ją do kolejki
        if counters[x] == 0:
            counter += 1
            lastValues.put(num)

        # jeżeli w moim podciągu jest już k liczb
        if counter == k:
            # znajduje liczbę od której mogę zacząć nowy podciąg, tak żeby nie zawierał już wszystkich k liczb i zawierał obecnie rozważaną liczbę i
            last = lastValues.get()
            lastI = binary_search(values, last)
            counters[lastI] = 0
            counter -= 1
            # sprawdzam długość tego ciągu który poprzednio znalazłem
            length = i - 1 - lastIndexes[x]
            if length > maxLength:
                maxLength = length

        lastIndexes[x] = i
        counters[x] += 1

    return maxLength