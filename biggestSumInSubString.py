import random

tab = []

# Generujemy 5-elementowa tablice z liczbami calkowitymi

for i in range(0, 5):
    tab.append(random.randint(-10,10))

for j in tab:
    print(j, end=" ")

# Przypisujemy wartosc sumNum do pierwszego elementu tablicy, oraz maksymalna AKTUALNA sume liczb, ktora jest rowna zero.

sumNum = tab[0]
sumMax = 0

# Tworzymy petle, ktora wykonuje sie od 1 do konca tablicy.

for i in range(1, len(tab)):

    # Jesli suma liczb, jest mniejsza od 0, to przypisujemy jej wartosc do zmiennej i. (nastepnej liczby przy pierwszej iteracji)

    if sumNum < 0:
        sumNum = tab[i]
    else:

        # W innym wypadku, do sumy liczb, dodajemy element tablicy, o indeksie i. (dla pierwszej iteracji nastepny element)

        sumNum += tab[i]

    # Sposrod sumy liczb sprawdzamy ktora liczba jest wieksza. (W pierwszej iteracji sumMax = 0, wiec sprawdzamy miedzy uzyskana suma liczb a 0.)

    sumMax = max(sumNum, sumMax)

# Wypisujemy najwieksza sume liczb z listy w ciagu.

print("\n",str(sumMax))