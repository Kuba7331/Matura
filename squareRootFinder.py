number = 49
begin = 0
end = number
accuracy = 0.05

# Algorytm szuka pierwiastka dla podanej liczby zoptymalizowana metoda, dziel i zwyciezaj.
# Metoda polega na wybraniu srodkowej liczby z przedzialu od 0 do naszej liczby. Wyznaczamy poczatek przedzialu (0), oraz jego koniec (nasza liczba).
# Jesli liczba w srodku przedzialu podniesiona do kwadratu jest rowna naszej liczbie, to oznacza to, ze jest to pierwiastek tej liczby.
# Jesli srodek do kwadratu jest wiekszy, to koniec przedzialu zostaje przyrownany do srodka. Dzieje sie odwrotnie, gdyby liczba srodkowa przedzialu podniesiona do kwadratu bylaby mniejsza od szukanej liczby.
# Sekwencja powtarza sie do momentu, az wartosc bezwzgledna z roznicy miedzy liczba koncowa a poczatkowa bedzie mniejsza od naszej dokladnosci.
# Dokladnosc w algorytmie pelni role granicy, ktora swiadczy o tym, ze jesli zostala ona przekroczona, to oznacza to, ze ta liczba jest pierwiastkiem szukanej przez nas liczby.
# Innymi slowy, zakres liczb sie zaweza, az odnajdziemy liczbe, ktora albo przekroczy granice dokladnosci, lub jej kwadrat bedzie szukana nasza liczba.
def squareRoot(begin, end, accuracy):
    global number
    while abs(end - begin) >= accuracy:
        middle = (end + begin) / 2
        if middle ** 2 == number:
            return middle
        elif middle ** 2 > number:
            end = middle
        else:
            begin = middle
    return int(round(middle, 1))

print(squareRoot(begin, end, accuracy))