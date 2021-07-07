# Mateusz Kleszcz

def printSolution(T, F, P, index, current, maxi, sum=0): #złożoność co najmniej O(n^2), choć samo wypisanie powinno zajmować więcej (ilość ciągów wykładnicza)
    # warunek brzegowy rekurencji, jeżeli znaleźliśmy ciąg o najdłuższej długości, to wypisujemy go na podstawie tablicy P
    if current == maxi + 1:
        i = 0
        # nie chciałem komplikować wywołania rekurencyjnego i wprowadzać dodatkowego parametru, ale pierwszym wyrazem do wypisania może być ten o indeksie pierwszym lub drugim
        # w tablicy P, wolałem więc po prostu sprawdzić czy przypadkiem nie wypisuje czegoś błędnego na początku
        if T[i] < T[P[i]]:
            print(T[i], end=' ')
        # wypisywanie podciągu na podstawie tablicy P
        while P[i] != -1:
            print(T[P[i]], end=' ')
            i = P[i]
        print()
        return 1

    #w F[i] mam informację o tym, ile elementów jest mniejszych od T[i], szukam więc w tablicy F indeksów które mają wartość 1, potem rekurencyjnie szukam tych które mają wartości 2 itp aż do n
    for i in range(index, len(T)):
        if F[i] == current:
            P[index] = i #zapisuje sobie ten indeks w tablicy P
            sum += printSolution(T, F, P, i, current + 1, maxi)
            P[index] = -1 #po wywołaniu rekurencji ustawiam sobie P z powrotem na -1, tak aby nie marnować pamięci na tworzenie nowych tablic
    return sum
    # nie jestem pewien o co chodzi z wypisywaniem ciągów "w kolejności", ale postarałem się zachować kolejność przypominającą tę z przykładu
    # znacznie to jednak skomplikowało pierwotną funkcję, która kolejności nie zachowywała i spowolniło program


def printAllLIS(A):
    n = len(A)

    # szukam maksymalnej długości LIS, dokładnie tak jak na wykładzie, złożoność n^2
    # da się w nlogn, ale znalezienie wszystkich ciągów i tak zajmie co najmniej n^2
    F = [1] * n
    P = [-1] * n #tutaj tylko deklaracja tablicy parentów, żeby była poza funkcją rekurencyjną
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1

    return printSolution(A, F, P, 0, 1, F[n - 1]) #funkcja wypisująca wszystkie LISy i zwracająca ich ilość