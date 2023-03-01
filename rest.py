coinList = [1,2, 5, 10, 20, 50, 100, 200, 500]
price = int(input())
coins = []

# Algorytm wypisuje nam najlepsze ulozenie monet, aby uzyskac dana liczbe, z podanych nominalow z listy coinList.
# Algorytm wykonuje sie do momentu, az roznica miedzy cena, a danym nominalem bedzie rowna 0.
# Dzialamy od konca listy coinList, dodajemy kazdy element, ktory sprawil, ze dana liczba jest wieksza, lub rowna 0. Po czym od naszej ceny, odejmujemy liczbe z sprawdzanego nominalu i dalej przechodzimy przez petle.
# Petla przerywa sie, w momencie, kiedy roznica miedzy cena a sprawdzanym nominalem jest mniejsza od 0, po czym sprawdza, czy dla mniejszych nominalow bedzie wieksza od 0.
# Jesli jest, dodaje dany nominal do listy ulozenia monet do zaplaty.

for i in range(len(coinList) -1, -1, -1):
    while price - coinList[i] >=0:
        price -= coinList[i]
        coins.append(coinList[i])

for j in coins:
    print(str(j)," ", end=None)
