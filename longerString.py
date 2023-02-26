string1 = input()
string2 = input()

# Algorytm sprawdza ktory wyraz/ciag znakow jest dluzszy, po liczbie jego znakow. (Funkcja len())

def whichIsLonger(stringOne, stringTwo):

    # W wypadku, gdy dlugosc znaku pierwszego jest wieksza od drugiego, to analogicznie, pierwszy jest dluzszy.

    if len(stringOne) > len(stringTwo):
        return print(stringOne, "is longer a string.")

    # W przeciwnym razie, drugi jest dłuzszy.

    elif len(stringTwo) > len(stringOne):
        return print(stringTwo, "is longer a string.")

    # W wypadku, gdy oba stringi maja ta sama dlugosc, to sa sobie rowne.

    elif len(stringOne) == len(stringTwo):
        return print("Both strings have an equal length.")

whichIsLonger(string1, string2)