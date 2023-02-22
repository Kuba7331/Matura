import random
import time

# Implementujemy nieposortowana tablice losowych liczb o 5000 elementach, z zakresu od 1-100

a = []

for i in range(0, 10):
    a.append(random.randint(1,100))

print("Un-sorted list:")
print(a)

# Sortowanie babelkowe - najprostszy algorytm sortowania. Sprawdza dwa elementy od poczatku listy, tak zeby posortowac liste rosnaco.
# Jesli element po lewej stronie, jest wiekszy od elementu po prawej stronie, zamienia sie go miejscami.

def bubbleSort(listOfNumbers):

    # Tworzymy dwie petle zagniezdzone
    # Pierwsza petla sluzy, do przejscia przez dokladnie cala tabele
    # Druga petla, sprawdza, czy elementy sa posortowane. Jej zakres zmniejsza sie z kazdym nastepnym prawidlowo posortowanym elementem.
    # (Jesli z 10-elementowej tablicy, mamy dwa elementy posortowane, to zakres sortowania odbywa sie w zakresie indeksow 0-7)

    for x in range(len(listOfNumbers)):
        for z in range(1, len(listOfNumbers) - x):
            if listOfNumbers[z - 1] > listOfNumbers[z]:
                listOfNumbers[z-1], listOfNumbers[z] = listOfNumbers[z], listOfNumbers[z-1]
    return listOfNumbers

print("Sorted list")
timeStart = time.time()
print(bubbleSort(a))
timeStop = time.time()
print("In time:", str(round(timeStop - timeStart, 2)))


