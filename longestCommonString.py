
# Algorytm sprawdza nadluzszy wspolny podciag z obu wyrazow.

stringOne = input()
stringTwo = input()

stringLengthOne = len(stringOne)
stringLengthTwo = len(stringTwo)

tab = []

# Do kazdej z liter z pierwszego slowa, tworzymy tablice o wartosci 0.

for i in range(stringLengthOne + 1):
    tab.append([0] * (stringLengthTwo + 1))

# Sprawdzamy kazda litere w pierwszym slowie, jesli litera ze slowa pierwszego, jest taka sama, jak z slowa drugiego, maksymalny podciag rosnie o 1.

for j in range(stringLengthOne):
    character = stringOne[j]
    for x in range(stringLengthTwo):
        character2 = stringTwo[x]
        if character == character2:
            tab[j+1][x+1] = tab[j][x] + 1
            continue
        tab[j+1][x+1] = max(tab[j+1][x], tab[j][x+1])

maxN = -1000

# Przyrownanie wartosci najdluzszego podciagu tych samych liter z obu wyrazow.

for i in range(stringLengthOne):
    for j in range(stringLengthTwo):
        if maxN < tab[i][j]:
            maxN = tab[i][j]

print(maxN + 1)