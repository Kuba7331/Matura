import random

tab = []

# Generujemy 10-elementowa tablice losowych liczb

for i in range(0,10):
    tab.append(random.randint(0,10))

# Wypisujemy te elementy

for j in tab:
    print(j, end=" ")

# Dla kazdego elementu tablicy przypisujemy druga wartosc, rowna 0, okreslajaca liczbe nastepnych cyfr, ktore sa wieksze od niej po prawej stronie w ciągu

length = [0] * len(tab)

# Tworzymy petle, ktora malejaca sprawdza kazdy element, czy jest wiekszy od nastepnego, jesli tak, dodaje 1 do zmiennej "length" od indeksu danej liczby


for i in range(len(tab) - 1, -1, -1):
    print(i)
    # Sprawdzanym elementem jest ostatni element tablicy jako pierwszy
    # Przypisujemy zmienna do sprawdzanego elementu tablicy

    x = tab[i]

    # Tworzona jest petle sprawdzajaca ktory element jest wiekszy od ostatniego elementu

    for j in range(i+1, len(tab), 1):

        # Jeśli dany element jest wiekszy od wyznaczonego wyzej, zmienia sie wartosc sprawdzanego elementu, na wiekszy, oraz dodaje sie 1 do dlugosci rosnacego podciagu wzgledem sprawdzanego znaku

        if tab[j] > x:
            x = tab[j]
            length[i] += 1

    # W wypadku, gdy nie ma zadnego wiekszego podciagu rosnacego wzgledem sprawdzanej liczby, wtedy wartosc tego podciagu jest rowna 1.

    length[i] += 1

print("\n")
print("Ilosc rosnacych podciagow od danej liczby.")

# Wypisanie dlugosci rosnacych podciagow, wzgledem kazdego elementu w tablicy

for k in length:
    print(k, end=" ")
