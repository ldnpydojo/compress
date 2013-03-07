from itertools import izip, count
def encode(plaintext):
    frequencies = frequency(plaintext)
    dic = dict(izip(set(plaintext), count()))
    #print frequencies
    print dic
    cipher = [dic[word] for word in plaintext]
    return dic, cipher

def decode(dic, cipher):
    for word in cipher:
        plaintext
    return plaintext

def frequency(data):
    d = {}
    for word in data:
        if d.has_key(word):
            d[word] += 1
        else:
            d[word] = 1

    return d
