
# Ciag Fibbonacciego - algorytm wyznaczajacy ciag liczb, skladajacy sie z sumy dwoch poprzednich liczb (1, 1, 2, 3, 5, 8...)

# Tworzymy dwuelementowa tablice, skladajaca sie z dwoch poczatkowych liczb z ciagu Fibbonacciego.

tabFib = [1, 1]

# Wpisujemy dlugosc ciagu

fibNumber = int(input())

# t

def FibonacciSeq(number):

    # Sprawdzamy czy podana przez nas liczba jest mniejsza, lub rowna dwa, jesli jest, wypisujemy tylko 1 zgodnie z definicja ciagu.

    if number <= 2:
        return 1

    # Dla liczb wiekszych od 2, sumujemy sumy dwoch poprzednich liczb i owy element, dodajemy do listy, ten proces powtarza sie az do momentu koncowego indeksu podanego w zakresie petli.

    else:
        for i in range(2, number):
            tabFib.append(tabFib[i-1] + tabFib[i-2])
    return tabFib[number - 1]

print(FibonacciSeq(fibNumber))