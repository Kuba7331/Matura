import random

a = []

for i in range(0, 20):
    a.append(random.randint(1,100))

print("Un-sorted list:")
print(a)


def bubbleSort(listOfNumbers):
    for x in range(len(listOfNumbers)):
        for z in range(1, len(listOfNumbers) - x):
            if listOfNumbers[z - 1] > listOfNumbers[z]:
                listOfNumbers[z-1], listOfNumbers[z] = listOfNumbers[z], listOfNumbers[z-1]
    return listOfNumbers

print("Sorted list")
print(bubbleSort(a))