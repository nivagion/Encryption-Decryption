
def encrypt(text):
    result = ''
    lowerNormal = 'abcdefghijklmnopqrstuvwxyz'
    upperNormal = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
    lowerReversed = 'zyxwvutsrqponmlkjihgfedcba' #could have used> lowerReversed = lowerNormal[::-1]
    upperReversed = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    
    for i in range(len(text)):
        if text[i] in lowerNormal:
            pos = lowerNormal.index(text[i]) # returns at what position is text[i] in lowerNormal
            result += lowerReversed[pos]
        elif  text[i] in upperNormal:
            pos = upperNormal.index(text[i])
            result += upperReversed[pos]
        else:
            result += text[i]
        
    return result

def decrypt(text):
    pass
    