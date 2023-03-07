
string = "abcdefghijklmn"
key = 16 % 26

# Szyfr Cezara - algorytm, sluzacy do szyfrowania ciagu znakow, poprzez przesuniecie calego alfabetu o podany indeks. (np. litera A w normalnym alfabecie, to litera C w szyfrze Cezara, gdzie przesuwamy litery o 2 indeksy w alfabecie)

def CaesarCode(string, key):
    coded = ""
    for i in string:

        # W wypadku, gdy nasz wybrany klucz, bedzie przekraczal alfabet, to przechodzimy do nastepnej iteracji przez niego.
        # (czyli od nowa przechodzimy przez alfabet)
        # Dodajemy nowy juz znak, do nowego stringa, ktory przechowuje zakodowanego poprzedniego stringa.

        if chr(ord(i) + key) > "z":
            coded += chr(ord(i) + key - 26)
        else:

            # Po prostu przesuwamy znak o tyle indeksow, ile podalismy w kluczu.

            coded += chr(ord(i) + key)
    return coded

print(CaesarCode(string,key))
