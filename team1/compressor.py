import re
from itertools import izip, count
from collections import Counter
import pickle

def encode(words):
    counted_words = Counter(words)
#    words = list(set(words))
    scores = {word: len(word) * counted_words[word] for word in set(words)}

    ixs_to_words = dict(enumerate(set(words)))
    words_to_ixs = {v: k for k, v in ixs_to_words.items()}

    cipher = []
    for word in words:
        if counted_words[word] == 1:
            cipher.append(word)
        else:
            cipher.append(words_to_ixs[word])
    return ixs_to_words, cipher

def decode(ixs_to_words, cipher):
    decoded = []
    for k in cipher:
        if isinstance(k, int):
            decoded.append(ixs_to_words[k])
        else:
            decoded.append(k)
    return decoded

def encode_file(path1, path2):
    #words = open(path1).read().split()
    words = re.findall(r"[\w']+|[.,!?;]", open(path1).read())
    encoded = encode(words)
    with open(path2, 'w') as f:
        pickle.dump(encoded, f, pickle.HIGHEST_PROTOCOL)

def decode_file(path1, path2):
    with open(path1) as f:
        ixs_to_words, cipher = pickle.load(f)
    words = decode(ixs_to_words, cipher)
    with open(path2, 'w') as f:
        f.write(' '.join(words))

if __name__ == '__main__':
    import sys
    if sys.argv[1] == 'encode':
        encode_file(sys.argv[2], sys.argv[3])
    else:
        decode_file(sys.argv[2], sys.argv[3])


