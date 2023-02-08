def ifCross(point1, point2, point3, point4):

    if point1 == point3 or point1 == point4 or point2 == point3 or point2 == point4:
        return True
    else:
        a = (point2[1] - point1[1]) / (point2[0] - point1[0])
        b = point1[1] - (a * point1[0])
        if a*point3[0] + b >= point3[1] and a*point4[0] + b <= point4[1]:
            return True
        elif a*point3[0] + b <= point3[1] and a*point4[0] + b >= point4[1]:
            return True
    return False

print(ifCross([1,2],[6,12],[1,8],[6,0]))