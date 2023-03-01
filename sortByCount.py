import random
import time

# Sortowanie poprzez zliczanie - algorytm sortowania, ktory uklada nam tabele wpisujac liczby do tablicy pomocniczej o tym samym indeksie, jaki ma liczba.
# Jesli liczba sie powtarza, dodaje sie kolejna jedynke do indeksu liczby w tablicy pojedynczej.
# Tworzy sie kolejna tablice, wyjsciowa, do ktorej dodaje sie kazdy element, powtorzony tyle razy, ile bylo zapisane w tablicy pomocniczej, od poczatku, do jej konca.

def countSort(tabel):
    howMuch = [0] * (max(tabel) + 1)
    for i in range(len(tabel)):
        howMuch[tabel[i]] += 1
    sortedTab = []
    for j in range(len(howMuch)):
        while howMuch[j] > 0:
            howMuch[j] -= 1
            sortedTab.append(j)
    return sortedTab





tab = []

for i in range(0, 10):
    tab.append(random.randint(0,10))

print("Tab before count sort:")

for j in tab:
    print(j, end=" ")

print("\nSorted tab:")

timeStart = time.time()
tab = countSort(tab)
timeStop = time.time()

for x in tab:
    print(x, end=" ")

print("\nIn time: ", int(round(timeStop - timeStart, 3)))


