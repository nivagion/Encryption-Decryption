import caesar as caesar  #english letters only

whatMethod = input('single character: c-ceasar cypher, o-other: ')
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

elif whatMethod == 'o':#OTHER METHOD
    print('no other methods to enc/dec yet')

