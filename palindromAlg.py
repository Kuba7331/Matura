string1 = input()
newWord = string1.replace(" ", "")

def isPalindrom(stringToCheck):
    middleOfString = len(stringToCheck) // 2
    for i in range(middleOfString):
        if stringToCheck[i] != stringToCheck[len(stringToCheck) - 1 - i]:
            return False
    return True

if isPalindrom(newWord) == True:
    print("Word", string1, "is a palindrome.")
else:
    print("Word", string1,"is not a palindrome.")