string1 = input()
string2 = input()

def whichIsLonger(stringOne, stringTwo):
    if len(stringOne) > len(stringTwo):
        return print(stringOne, "is longer a string.")
    elif len(stringTwo) > len(stringOne):
        return print(stringTwo, "is longer a string.")
    elif len(stringOne) == len(stringTwo):
        return print("Both strings have an equal length.")

whichIsLonger(string1, string2)