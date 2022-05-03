import vnchar

#Mã hóa
def encode(key, text):
    result = ""
    for letter in text:
        # ascii = (ord(letter) + key - 32 ) % 95 + 32   #From 32 -> 127
        ascii = (ord(letter) + key) % 256               #From 0 -> 255
        result = result + chr(ascii)
    return result

#Giải mã trường hợp biết trước Key
def decode(key, text):
    # dkey = 95 - (i % 95)      #From 32 -> 127
    dkey = 256 - (key % 256)    #From 0 -> 255
    return encode(dkey, text)

#Trường hợp không biết trước Key (Vét cạn)
def decode(text):
    results = []
    for i in range(1, 256):
        # dkey = 95 - (i % 95)  #From 32 -> 127
        dkey = 256 - (i % 256)  #From 0 -> 255
        ptext = encode(dkey, text) #Tiến hành giải mã
        point = vnchar.checkSentence(ptext.lower()) #Xử lý Tiếng Việt
        result = [i, ptext, point]
        results.append(result)
    results = sorted(results, key=lambda x: x[2], reverse=True)
    return results #Kết quả trả về là Danh sách bản rõ ứng viên