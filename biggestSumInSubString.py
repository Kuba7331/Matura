import random

tab = []

for i in range(0, 5):
    tab.append(random.randint(-10,10))

for j in tab:
    print(j, end=" ")

sumNum = tab[0]
sumMax = 0

for i in range(1, len(tab)):
    if sumNum < 0:
        sumNum = tab[i]
    else:
        sumNum += tab[i]
    sumMax = max(sumNum, sumMax)

print("\n",str(sumMax))