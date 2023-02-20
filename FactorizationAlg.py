number = int(input())

# Definiujemy tablice ktora bedzie przechowywac czynniki naszej liczby.

factors = []

# Zmienna printable definiuje, czy mozemy rozlozyc dana liczbe na czynniki

printable = True


def factorizationAlg(numberToCheck):
    global printable

    # Sprawdzamy czy liczba jest wieksza od 1

    if numberToCheck > 1:

        # Pierwsza liczba, przez ktora dzielimy, jest liczba 2. Nie 1, poniewaz, kazda liczba podzielona przez 1 jest sobie rowna.

        i = 2

        # Definiujemy petle, ktora wykonuje sie do momentu, kiedy nasza liczba bedzie rowna 1, czyli bedzie rozlozona na czynniki.

        while numberToCheck != 1:

            # Sprawdzamy, czy liczba jest podzielna przez dane i.

            if numberToCheck % i == 0:

                # Przyrownujemy wartosc liczby do dzielenia calkowitego, przez liczbe i, zeby moc ja dalej rozkladac na czynniki

                numberToCheck //= i

                # Dodajemy liczbe, przez ktora nasza liczba byla podzielna do tablicy z czynnikami

                factors.append(i)
            else:

                # Jesli dana liczba nie jest podzielna przez i, dodajemy do i jedynke, by sprawdzic czy jest dana liczba jest podzielna przez nastepne liczby.

                i+=1
    else:
        print("Liczba " + str(numberToCheck) + " nie jest rozkładalna na czynniki!")
        printable = False

factorizationAlg(number)

if printable == True:
    print("Czynniki liczby: " + str(number))
    for i in factors:
        print(str(i), end=" ")

