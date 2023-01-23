import random
import time

tabel = []


for i in range(0, 5000):
    tabel.append(random.randint(0,10000))

print("Tabel before merge sort:")
for i in tabel:
    print(i, end=" ")

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

