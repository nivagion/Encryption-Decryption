import caesar as caesar  #english letters only
import atbash as atbash
import atbashWithCaesar as atbcae

whatMethod = input('single character: c-ceasar cypher, a-atbash, atc-atbash+cypher : ')
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

if whatMethod == 'atc':#ATBASH + CAESAR
    shift = int(input('ceasar shift: '))
    if decOrEnc == 'd':
        print(atbcae.decrypt(text, shift))
    else:
        print(atbcae.encrypt(text, shift))

