import curses.ascii

def encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':#ili ovako .isupper()
            result += chr((ord(char) + shift - 65) % 26 + 65) #ord> char to number, 65> range between 0-26
        elif char in 'abcdefghijklmnopqrstuvwxyz':#ili ovako .islower()
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)