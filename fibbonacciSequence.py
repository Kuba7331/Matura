
tabFib = [1, 1]

fibNumber = int(input())

def FibonacciSeq(number):
    if number <= 2:
        return 1
    else:
        for i in range(2, number):
            tabFib.append(tabFib[i-1] + tabFib[i-2])
    return tabFib[number - 1]

print(FibonacciSeq(fibNumber))