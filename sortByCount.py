import random
import time


def countSort(tabel):
    howMuch = [0] * (max(tab)+1)
    for i in range(len(tabel)):
        howMuch[tabel[i]] += 1
    sortedTab = []
    for j in range(len(howMuch)):
        while howMuch[j] > 0:
            howMuch[j] -= 1
            sortedTab.append(j)
    return sortedTab


tab = []

for i in range(0, 1000000):
    tab.append(random.randint(0,100))

print("Tab before count sort.")

for j in tab:
    print(j, end=" ")

print("\nSorted tab:")

timeStart = time.time()
tab = countSort(tab)
timeStop = time.time()

for x in tab:
    print(x, end=" ")

print("\nIn time: ", int(round(timeStop - timeStart, 3)))


