interval = [-7,4]
a = interval[0]
b = interval[1]

accuracyX = accuracyY = 0.05

def functionY(x):
    return (2 * x) + 4

def findingZeroPoints(begin, end, accuracyX, accuracyY):
    while abs(end - begin) >= accuracyX:
        middle = (begin + end) / 2
        if abs(functionY(middle)) < accuracyY:
            break
        elif functionY(begin) * functionY(middle) <= 0:
            end = middle
        else:
            begin = middle
    return (begin + end) / 2

print(findingZeroPoints(a,b,accuracyX,accuracyY))


