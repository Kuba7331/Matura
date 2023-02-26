import  random

tab = []

# Generujemy 10-elementowa tablice, z losowymi liczbami z zakresu 1-10.

for i in range(0, 10):
    tab.append(random.randint(0,10))

print("Tabel:")

for j in tab:
    print(j, end=" ")

# Funkcja sprawdza najdluzszy rosnacy ciag liczb w tablicy.

def longestAscSubStr(arr):
    n = len(arr)
    max_len = 1  # maksymalna długość podciągu niemalejącego
    cur_len = 1  # aktualna długość podciągu niemalejącego
    for i in range(1, n):   # petla przechodzi przez 2-gi element tablicy, do jej konca.
        if arr[i] > arr[i-1]: # porownujemy liczby miedzy soba, jesli liczba, po prawej stronie jest wieksza od tej po lewej, dodajemy 1 do najdluzszego podciagu rosnacych liczb w tablicy.
            cur_len += 1
        else: # sprawdzamy aktualny podciag, jesli jest wiekszy od maksymalnego, to maksymalny przyjmuje wartosc aktualnego, w innym wypadku, aktualna dl. ciagu jest rowna 1.
            max_len = max(max_len, cur_len)
            cur_len = 1
    max_len = max(max_len, cur_len)  # sprawdzamy ostatni podciąg
    return max_len

print("\nLongest ascending number string in tabel has a length of:", longestAscSubStr(tab),"numbers")