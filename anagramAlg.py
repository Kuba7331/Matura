
string1 = input()
string2 = input()

def AnagramAlg(stringToCheck):
    dict = {}
    for char in stringToCheck:
        dict[char] = 0
    for i in stringToCheck:
        dict[i] += 1
    return dict

if AnagramAlg(string1) == AnagramAlg(string2):
    print("Both word are anagrams.")
else:
    print("Words are not anagrams.")