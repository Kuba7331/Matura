number = int(input())

factors = []
printable = True


def factorizationAlg(numberToCheck):
    global printable
    if numberToCheck > 1:
        i = 2
        while numberToCheck != 1:
            if numberToCheck % i == 0:
                numberToCheck //= i
                factors.append(i)
            else:
                i+=1
    else:
        print("Liczba " + str(numberToCheck) + " nie jest rozkładalna na czynniki!")
        printable = False

factorizationAlg(number)

if printable == True:
    print("Czynniki liczby: " + str(number))
    for i in factors:
        print(str(i), end=" ")

