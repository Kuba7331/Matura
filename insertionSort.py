import random
import time

tabel = []

tabelLength = 5000

for i in range(0, tabelLength - 1):
    tabel.append(random.randint(0,100))

print("Tabel before insertion sort:")

for j in tabel:
    print(j, end=" ")

def insertionSort(listOfNumbers):
    for i in range(1, tabelLength - 1):
        j = i - 1
        comp = listOfNumbers[i]
        while j > -1 and listOfNumbers[j] > comp:
            listOfNumbers[j+1] = listOfNumbers[j]
            j -= 1
        listOfNumbers[j+1] = comp
    return listOfNumbers

print("\nTabel after insertion sort:")

timeStart = time.time()

tabel = insertionSort(tabel)

timeStop = time.time()

for x in tabel:
    print(str(x), end=" ")

print("\nIn time: ", str(round(timeStop - timeStart, 2)))

