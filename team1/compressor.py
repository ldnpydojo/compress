import re
from itertools import izip, count
from collections import Counter
import pickle

def encode(words):
    counted_words = Counter(words)
    words_in_order = [item[0] for item in counted_words.most_common()]

    ixs_to_words = dict(enumerate(words_in_order))
    words_to_ixs = {v: k for k, v in ixs_to_words.items()}
    cipher = [words_to_ixs[word] for word in words]
    return ixs_to_words, cipher

def decode(ixs_to_words, cipher):
    return [ixs_to_words[ix] for ix in cipher]

def encode_file(path1, path2):
    words = re.split(r'\b', open(path1).read())
    encoded = encode(words)
    with open(path2, 'w') as f:
        pickle.dump(encoded, f)

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


