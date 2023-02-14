
string = "abcdefghijklmn"
key = 16 % 26

def CaesarCode(string, key):
    coded = ""
    for i in string:
        if chr(ord(i) + key) > "z":
            coded += chr(ord(i) + key - 26)
        else:
            coded += chr(ord(i) + key)
    return coded

print(CaesarCode(string,key))
