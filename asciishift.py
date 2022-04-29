import vnchar

def encode(key, text):
    result = ""
    for letter in text:
        # ascii = (ord(letter) + key - 32 ) % 95 + 32   #From 32 -> 127
        ascii = (ord(letter) + key) % 256               #From 0 -> 255
        result = result + chr(ascii)
    return result

#Trường hợp biết trước Key
def decode(key, text):
    # dkey = 95 - (i % 95)      #From 32 -> 127
    dkey = 256 - (key % 256)    #From 0 -> 255
    return encode(dkey, text)

#Trường hợp không biết trước Key (Vét cạn)
def decode(text):
    results = []
    for i in range(1, 255):
        # dkey = 95 - (i % 95)  #From 32 -> 127
        dkey = 256 - (i % 256)  #From 0 -> 255
        ptext = encode(dkey, text)
        point = vnchar.checkSentence(ptext.lower())
        result = [i, ptext, point]
        results.append(result)
    return results