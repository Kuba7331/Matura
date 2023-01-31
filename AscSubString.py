import random

tab = []

for i in range(0,10):
    tab.append(random.randint(0,10))

for j in tab:
    print(j, end=" ")

length = [0] * len(tab)

for i in range(len(tab) - 1, -1, -1):
    x = tab[i]
    for j in range(i+1, len(tab), 1):
        if tab[j] > x:
            x = tab[j]
            length[i] += 1
    length[i] += 1

print("\n")
print("Ilosc rosnacych elementow dla kazdej liczby od lewej do prawej.")

for k in length:
    print(k, end=" ")
