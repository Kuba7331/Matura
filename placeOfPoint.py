point = [5,10]
function = [2, 4]

def pointPosition(point, function):
    if function[0] * point[0] + function[1] > point[1]:
        return print("Punkt znajduje sie pod prosta.")
    elif function[0] * point[0] + function[1] < point[1]:
        return print("Punkt znajduje sie nad prosta.")
    elif function[0] * point[0] + function[1] == point[1]:
        return print("Punkt nalezy do prostej.")

pointPosition(point,function)