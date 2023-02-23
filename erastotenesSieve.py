interval = 50

# Sito Erastotenesa - algorytm sluzacy do wyznaczania liczb pierwszych, poprzez wykreslanie wielokrotnosci liczb z listy.

# Implementujemy tablice, dla ktorej przypisujemy dwie poczatkowe wartosci False, jako ze, 0 i 1 to nie sa liczby pierwsze, a dla reszty True.

tabel = [False, False] + [True] * (interval - 2)

# Tworzymy petle, ktora zaczyna sie od 2 i dziala do konca wyznaczonego przez nas zakresu.

for i in range(2, interval):

    # Poczatkowa wielokrotnosc jaka sprawdzamy, zaczynamy od 2, poniewaz dla 1, kazda liczba bylaby jej wielokrotnoscia

    multiplicity = 2

    # Tworzymy petle, ktora dziala do momentu, az iloczyn wielokrotnosci i zmiennej "i" w petli, bedzie wiekszy od koncowej liczby wyznaczonego zakresu.

    while multiplicity * i < interval:

        # Dla kazdego indeksu, ktory jest wielokrotnoscia i, przypisujemy wartosc False, poniewaz liczby te, nie sa pierwsze.

        tabel[multiplicity * i] = False

        # By przejsc do nastepnych wielokrotnosci liczb, zwiekszami zmienna wielokrotnosci o 1.

        multiplicity += 1

# Wypisujemy wszystkie liczby pierwsze w danym zakresie.

# Innymi slowy, liczba pierwsza, jest kazda NOWA liczba wielokrotnosci, ktora nie jest wielokrotnoscia poprzednich liczb. (zgodnie z tym algorytmem)

for j in range(len(tabel)):
    print(str(j) + " " + str(tabel[j]))