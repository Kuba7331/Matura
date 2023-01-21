coinList = [1, 2, 5, 10, 50, 100, 200]
price = int(input())
coins = []

for i in range(len(coinList) -1, -1, -1):
    while price - coinList[i] >=0:
        price -= coinList[i]
        coins.append(coinList[i])

for j in coins:
    print(str(j)," ", end=None)

