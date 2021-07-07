def find_min_max(tab):
     n = len(tab)
     min = max = tab[n]
     for i in range(0, n - 1, 2):
         if tab[i] < tab[i + 1]:
            if tab[i] < min:
                min = tab[i]
            if tab[i + 1] > max:
                max = tab[i + 1]
         else:
             if tab[i] > min:
                 min = tab[i]
             if tab[i + 1] < max:
                 max = tab[i + 1]
     return min, max


tab = [7, 8, 2, 4, 5, 11, 64, 32, 2]
print(find_min_max(tab))