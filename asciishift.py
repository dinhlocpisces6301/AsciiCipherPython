def encode(key, text):
    result = ""
    for letter in text:
        ascii = ( ord(letter) + key - 32 ) % 95 + 32
        result = result + chr(ascii)
    return result


def decode(key, text):
    dkey = 95 - (key % 95)
    return encode(dkey, text)

def decode(text):
    results = []
    for i in range(1, 95):
        dkey = 95 - i % 95
        result = encode(dkey, text)
        results.append(result)
    return results