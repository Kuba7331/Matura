import random
import time

tabel = []


for i in range(0, 10):
    tabel.append(random.randint(0,10))

print("Tabel before merge sort:")
for i in tabel:
    print(i, end=" ")

# Merge Sort - sortowanie poprzez scalanie. Algorytm ten, sortuje tablice, dzielac je na dwie posortowane juz polowy, az napotka pojedynczy element.
# Jesli dany element jest mniejszy od wyznaczonego srodka, laduje on po lewej stronie tablicy. Jesli jest wiekszy, laduje po prawej stronie tablicy.
# Kazda z połów tablicy, ma swoj srodek. Zatem, dla pojedynczych elementow, porownuje sie je miedzy srodkami nastepnych, coraz to wiekszych polow, az wroci sie do postaci calej tablicy.

def mergeSort(listOfNumbers):
    middle = len(listOfNumbers) // 2
    leftTab = list(listOfNumbers[:middle])
    rightTab = list(listOfNumbers[middle:])
    leftTab.sort()
    rightTab.sort()
    leftPointer = rightPointer = middlePointer = 0
    while leftPointer < len(leftTab) and rightPointer < len(rightTab):
        if leftTab[leftPointer] <= rightTab[rightPointer]:
            listOfNumbers[middlePointer] = leftTab[leftPointer]
            leftPointer += 1
        else:
            listOfNumbers[middlePointer] = rightTab[rightPointer]
            rightPointer += 1
        middlePointer += 1
    while leftPointer < len(leftTab):
        listOfNumbers[middlePointer] = leftTab[leftPointer]
        leftPointer += 1
        middlePointer += 1
    while rightPointer < len(rightTab):
        listOfNumbers[middlePointer] = rightTab[rightPointer]
        rightPointer += 1
        middlePointer += 1
    return listOfNumbers

print("\nTabel after merge sort.")
timeStart = time.time()
tabel = mergeSort(tabel)
timeStop = time.time()

for j in tabel:
    print(j, end=" ")
print("\nIn time: ", str(round(timeStop-timeStart, 2)))

