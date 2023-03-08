
# Szyfr przestawieniowy - algorytm zamienia miejsca znakow ze soba wzajemnie o okreslony klucz. (wartosc n-indeksow, dla którego ma byc miejsce zamienionego znaku)
# Przy szyfrze przestawieniowym dlugosc znakow sie nie zmienia, a jedynie polozenie wszystkich jego znakow miejscami schematem.
# Zawartosc znakow z danego stringa sie nie zmienia.

def transpositionCipher(text):
    encrypted = []
    for i in range(1, len(text), 2):
        encrypted.append(text[i])
        encrypted.append(text[i-1])
    if len(text) % 2 == 1:
        encrypted.append(text[-1])
    return encrypted

textToPrint = ""
text = "abcdefg"

for i in transpositionCipher(text):
    textToPrint+=i

print(textToPrint)