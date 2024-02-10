import caesar as caesar  #english letters only
import atbash as atbash

whatMethod = input('single character: c-ceasar cypher, a-atbash : ')
decOrEnc = input('do you want to decrypt or encrypt: d/e: ')

if decOrEnc == 'd':
    text = input('input encrypted message: ')
else:
    text = input('input message you want to encrypt: ')

if whatMethod == 'c':#CEASAR
    shift = int(input('ceasar shift: '))
    if decOrEnc == 'd':
        print(caesar.decrypt(text, shift))
    else:
        print(caesar.encrypt(text, shift))

elif whatMethod == 'a':#ATBASH
    print(atbash.encrypt(text))

