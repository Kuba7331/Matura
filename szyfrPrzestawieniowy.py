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