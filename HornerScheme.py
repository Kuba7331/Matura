
# Schemat Hornera, to sposob obliczania wielomianu, wykorzystujac przy tym jak najmniejsza ilosc mnozen. Jest to rowniez algorytm dzielenia wielomianu.


# Schemat Hornera w wersji rekurencyjnej

def hornerSchemeRe(factors, rank,x):

    # W wypadku, gdy stopien wielomianu jest zerowy, zwracamy wszystkie dane wyzej czynniki stopnia zerowego.

    if rank == 0:
        return factors[0]

    # W innym wypadku, wykonujemy algorytm rekurencyjnie, dla o 1 mniejszego stopnia, od tego, jakiego dalismy w argumencie, do momentu, az stopien ten bedzie rowny 0.
    # Wypisuje on na koncu uzyskane czynniki po zmniejszeniu wielomianu o jeden, az do zera.

    else:
        return hornerSchemeRe(factors, rank-1, x) * x + factors[rank]

# Schemat Hornera w wersji iteracyjnej

def hornerSchemeIt(factors, rank, x):

    # W wersji iteracyjnej, podobnie jak w rekurencyjnej, jesli wielomian jest stopnia zerowego, to zwracamy jego czynniki o stopniu 0.

    if rank == 0:
        return factors[0]

    # Przypisujemy wartosc wyniku do czynnika stopnia zerowego.

    result = factors[0]

    # Definiujemy petle, ktora wykonuje sie od stopnia zerowego, do stopnia podanego w wielomianie.

    for i in range(rank):

        # Wynikiem jest iloczyn podanego x wraz z wynikiem, do ktorego przypisalismy wartosc czynnika stopnia zerowego i sumy czynnika o stopniu o jeden wiekszym od podanej zmiennej w petli.

        result = result*x + factors[i + 1]
    return result

# Definiujemy podstawowe elementy wielomianu, czynniki, jego stopien, oraz wartosc x, dla ktorego chcemy obliczyc caly wielomian.

factors = [2, 3, 1]
rank = 2
x = 2

print(str(hornerSchemeRe(factors,rank,x)))
print(str(hornerSchemeIt(factors,rank,x)))