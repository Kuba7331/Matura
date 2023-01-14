interval = 50

tabel = [False, False] + [True] * (interval - 2)

for i in range(2, interval):
    multiplicity = 2
    while multiplicity * i < interval:
        tabel[multiplicity * i] = False
        multiplicity += 1

for j in range(len(tabel)):
    print(str(j) + " " + str(tabel[j]))