import random

a = []

for i in range(0, 10):
    a.append(random.randint(1,100))

a.sort()

for j in a:
    print(j, end=" ")

numberToCheck = int(input())

def binarySearch(numbersList, numberToCheck):
    if numberToCheck < numbersList[0]:
        return False
    elif numberToCheck > numbersList[len(numbersList) - 1]:
        return False
    start = 0
    end = len(numbersList)
    mid = (start + end) // 2
    while start != end:
        mid = (start + end) // 2
        if numberToCheck > numbersList[mid]:
            start = mid + 1
        elif numberToCheck < numbersList[mid]:
            end = mid - 1
        elif numbersList[mid] == numberToCheck:
            return True
    return False

if binarySearch(a, numberToCheck) == True:
    print("Liczba", numberToCheck, "znajduje sie w liscie")
else:
    print("Liczba",numberToCheck, "nie znajduje sie w liscie")