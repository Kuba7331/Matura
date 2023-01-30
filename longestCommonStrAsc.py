import  random

tab = []

for i in range(0, 10):
    tab.append(random.randint(0,10))

print("Tabel:")

for j in tab:
    print(j, end=" ")

def longestAscSubStr(tabel):
    tabLength = len(tabel)
    max = -1000
    pointer = 0
    for i in range(len(tabel)):
        if pointer < i:
            pointer = i
        while pointer < tabLength - 1 and tabel[pointer] < tabel[pointer + 1]:
            pointer += 1
        varOne = pointer - i + 1
        if varOne > max:
            max = varOne
        pointer = 0
    return max

print("\nLongest ascending number string in tabel has a length of:", longestAscSubStr(tab),"numbers")