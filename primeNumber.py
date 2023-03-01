import math

isPrimeNumber = int(input())

# Algorytm sprawdza, czy podana przez uzytkownika liczba, jest liczba pierwsza.
# Liczba pierwsza, to liczba, ktora jest podzielna przez 1 i siebie.
# Sprawdzamy, czy liczba jest pierwsza, metoda dzielenia z reszta, poczawszy od 2, do pierwiastka sprawdzanej liczby, poniewaz wiemy, ze nastepne liczby po tym pierwiastku, beda juz sprawdzone, bo to beda tylko i wylacznie ich wielokrotnosci.
# Jesli przez caly proces dzielenia naszej liczby, przez wszystkie jej dzielniki, do jej pierwiastka, reszta bedzie rowna 0, to dana liczba nie jest liczba pierwsza.

def isPrime(numberToCheck):
    if numberToCheck < 2 :
        return False
    for i in range(2, int(math.sqrt(numberToCheck)) + 1):
        if numberToCheck % i == 0:
            return False
    return True

print(isPrime(isPrimeNumber))