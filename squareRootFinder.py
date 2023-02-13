number = 49
begin = 0
end = number
accuracy = 0.05

def squareRoot(begin, end, accuracy):
    global number
    while abs(end - begin) >= accuracy:
        middle = (end + begin) / 2
        if middle ** 2 == number:
            return middle
        elif middle ** 2 > number:
            end = middle
        else:
            begin = middle
    return (end + begin) / 2

print(squareRoot(begin, end, accuracy))