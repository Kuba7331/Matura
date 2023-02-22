import random

# Implementujemy tablice 10 elementowa

a = []

# Generujemy dla niej 10 losowych liczb w zakresie od 1-100

for i in range(0, 10):
    a.append(random.randint(1,100))

# Sortujemy tablice

a.sort()

for j in a:
    print(j, end=" ")

numberToCheck = int(input())

# Binary Search - algorytm sprawdzajacy, metoda dziel i zwyciezaj, czy dana liczba znajduje sie w konkretnej strukturze danych

def binarySearch(numbersList, numberToCheck):

    # Jesli liczba jest mniejsza, od pierwszego POSORTOWANEGO elementu w liscie, to sie w niej nie znajduje

    if numberToCheck < numbersList[0]:
        return False

    # Jesli liczba jest wieksza od ostatniego elementu listy, ktory jest najwiekszy w calej liscie, rowniez sie w niej nie znajduje.

    elif numberToCheck > numbersList[len(numbersList) - 1]:
        return False

    # Implementujemy zmienna startowa, ktora wyznacza poczatek listy, zmienna koncowa, ktora wyznacza indeks konca listy, oraz srodek listy, przez dzielenie calkowite poczatku i konca.

    start = 0
    end = len(numbersList)

    # Tworzymy petle, ktora wykonuje sie do momentu, az zmienna start, bedzie rowna zmiennej end

    while start != end:

        # Srodek wyznaczamy co kazda iteracje petli, by pozbyc sie polowy mozliwych rozwiazan, zawezajac przy tym zakres szukania.

        mid = (start + end) // 2

        # Jesli dana szukana liczba, jest wieksza od liczby znajdujacej sie w srodku listy, przyrownujemy wartosc zmiennej start, do wartosci srodka o jeden wiekszego
        # zeby zmniejszyc zakres szukania liczby o polowe listy

        if numberToCheck > numbersList[mid]:
            start = mid + 1

        # W wypadku, gdy dana liczba jest mniejsza, to zmienna konca, przyrownujemy wartosci srodka o jeden mniejszego, by tak samo zmniejszyc zakres szukania o polowe listy,

        elif numberToCheck < numbersList[mid]:
            end = mid - 1

        # Kiedy liczba o indeksie srodkowym jest liczba szukana, zwraca sie wartosc True, co oznacza, ze dana liczba jest w liscie

        elif numbersList[mid] == numberToCheck:
            return True
    return False

if binarySearch(a, numberToCheck) == True:
    print("Liczba", numberToCheck, "znajduje sie w liscie")
else:
    print("Liczba",numberToCheck, "nie znajduje sie w liscie")