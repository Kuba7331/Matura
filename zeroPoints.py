interval = [-7,4]
a = interval[0]
b = interval[1]

accuracyX = accuracyY = 0.05



def functionY(x):
    return (2 * x) + 4 # -10 i 10 -100

# Algorytm sprawdza, czy w danym przedziale, dla podanej funkcji istnieje miejsce zerowe.
# Accuracy X i Y sluza do okreslenia granicy. Jesli dany wynik bedzie mniejszy od 0.05, to uznawane jest, ze nalezy do tego punktu.
# Sprawdzenie, czy wystepuje dane miejsce zerowe nastepuja na zasadzie sprawdzenia, dla ktorego x, wartosc funkcji bedzie mniejsza od zera.
# Z kazda iteracji petli zawezamy przedzial, do momentu, az ten przekroczy wartosc 0.05 dla wartosci Y. Wtedy oznacza to, ze znajduje sie tam miejsce zerowe.
# Funkcja zwraca argument x, dla ktorego function(x) jest mniejsza od 0.05.

def findingZeroPoints(begin, end, accuracyX, accuracyY):
    while abs(end - begin) >= accuracyX:
        middle = (begin + end) / 2
        if abs(functionY(middle)) < accuracyY:
            break
        elif functionY(begin) * functionY(middle) <= 0:
            end = middle
        else:
            begin = middle
    return round(middle,1)

print(findingZeroPoints(a,b,accuracyX,accuracyY))


