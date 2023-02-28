point = [5,10]
function = [2, 4]

# Algorytm sprawdza polozenie punktu, wzgledem polozenia funkcji.

def pointPosition(point, function):
    if function[0] * point[0] + function[1] > point[1]: # Jesli y wspolrzedna punktu, jest mniejsza wartosci funkcji, dla tych samych argumentow, to punkt znajduje sie pod prosta.
        return print("Punkt znajduje sie pod prosta.")
    elif function[0] * point[0] + function[1] < point[1]: # Jesli y wspolrzedna punktu, jest wieksza od wartosci funkcji, dla tego samego argumentu, to punkt jest nad prosta.
        return print("Punkt znajduje sie nad prosta.")
    elif function[0] * point[0] + function[1] == point[1]: # Jesli y wspolrzedna, jest rowna wartosci funkcji, dla tego samego argumentu, to punkt znajduje sie na funckji.
        return print("Punkt nalezy do prostej.")

pointPosition(point,function)