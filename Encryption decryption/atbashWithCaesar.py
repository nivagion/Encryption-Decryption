import caesar as caesar
import atbash as atbash

def encrypt(text, shift):
    text = caesar.encrypt(text, shift) #caesar than atbash
    result = atbash.encrypt(text) 
    return result



def decrypt(text, shift):
    text = atbash.encrypt(text) #atbash than caesar
    result = caesar.decrypt(text, shift)
    return result