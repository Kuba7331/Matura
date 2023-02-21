
string1 = input()
string2 = input()

# Anagram, to slowo, ktore od zawiera taka sama ilosc tych samych liter w sobie.

def AnagramAlg(stringToCheck):

    # Tworzymy słownik, do ktorego bedziemy wpisywac litery, oraz ich ilosc w slowie

    dict = {}
    for char in stringToCheck:
        dict[char] = 0
    for i in stringToCheck:
        dict[i] += 1

    # Zwracamy dany slownik

    return dict

# Jesli w obu slowach, wystepuja te same litery o tej samej ilosci, to dane slowo jest anagramem.

if AnagramAlg(string1) == AnagramAlg(string2):
    print("Both word are anagrams.")
else:
    print("Words are not anagrams.")