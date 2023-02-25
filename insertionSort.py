import random
import time

tabel = []

tabelLength = 10

for i in range(0, tabelLength - 1):
    tabel.append(random.randint(0,100))

print("Tabel before insertion sort:")

for j in tabel:
    print(j, end=" ")

# Insertion sort - prosty algorytm sortowania, ktory nie wymaga dodatkowej pamieci komputera.

def insertionSort(tab):

    # Zaczyna sie iteracje petli przechodzaca przez cala tablice, od drugiego elementu tablicy

    for i in range(1, len(tab)):

        # Przyrownujemy wartosc zmiennej j do zmiennej i

        j = i

        # Tworzymy petle, ktora dziala do momentu, az element tab[j-1] napotka element wiekszy od siebie.

        while j > 0 and tab[j - 1] > tab[j]:

            # W wypadku, gdy liczba porownywana z lewej strony jest wieksza od prawej, dochodzi do zamiany elementow listy miejscami.

            tab[j], tab[j - 1] = tab[j - 1], tab[j]

            # Przesuwamy mniejszy element w lewa strone tablicy, do momentu, az napotka na mniejszy element od siebie.
            # Dziala to poprzez zmniejszanie indeksu tablicy o 1.

            j -= 1
    return tab

print("\nTabel after insertion sort:")

timeStart = time.time()

tabel = insertionSort(tabel)

timeStop = time.time()

for x in tabel:
    print(str(x), end=" ")

print("\nIn time: ", str(round(timeStop - timeStart, 2)))

