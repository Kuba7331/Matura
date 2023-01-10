import math

isPrimeNumber = int(input())

def isPrime(numberToCheck):
    if numberToCheck < 2 :
        return False
    for i in range(2, int(math.sqrt(numberToCheck)) + 1):
        if numberToCheck % i == 0:
            return False
    return True

print(isPrime(isPrimeNumber))