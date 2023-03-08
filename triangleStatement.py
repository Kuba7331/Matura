import random

triangleTab = []

for i in range(0,3):
    triangleTab.append(random.randint(1,100))



for x in range(0, len(triangleTab)):
    for y in range(0, len(triangleTab) - 1):
        if triangleTab[y] > triangleTab[y+1]:
            triangleTab[y], triangleTab[y+1] = triangleTab[y+1], triangleTab[y]

print("Boki trojkata rosnaco:")

for j in triangleTab:
    print(j, end=" ")

# Algorytm trojkata - algorytm ten sprawdza, czy z danych bokow mozna otrzymac trojkat.
# Dziala tutaj twierdzenie, mowiace o tym, ze jesli suma dwoch bokow jest wieksza od najdluzszego boku, to mozna z danych bokow stworzyc trojkat.

def triangleStatement(triangle):
    if triangle[0] + triangle[1] > triangle[2]:
        return True
    else:
        return False

if triangleStatement(triangleTab) == True:
    print("\nDane boki moga stworzyc trojkat.")
else:
    print("\nDane boki nie moga stworzyc trojkata.")

