import random

point1 = [1,2]
point2 = [2,4]

point = [3,6]

# Algorytm sprawdza, czy dany punkt nalezy do pewnej prostej/odcinka. Dziala to poprzez przyrownanie funkcji liniowej obu punktow polozonych na prostej, do wartosci sprawdzanego punktu.

def ifOnLine(point1,point2,point):
    a = (point2[1] - point1[1]) / (point2[0] - point1[0])
    b = point2[1] - a*point2[0]
    if a*point[0] + b == point[1]:
        return True
    return False

if ifOnLine(point1,point2,point) == True:
    print("Punkt nalezy do prostej.")
else:
    print("Punkt nie należy do prostej.")

