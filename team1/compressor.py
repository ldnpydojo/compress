import re
import sys
from collections import Counter
import cPickle

def encode(words):
    counted_words = Counter(words)
    ixs_to_words = dict(enumerate(k for (k,v) in counted_words.most_common()))
    words_to_ixs = {v: k for k, v in ixs_to_words.items()}

    cipher = []
    for word in words:
        if counted_words[word] == 1:
            cipher.append(word)
            del ixs_to_words[words_to_ixs[word]]
        else:
            cipher.append(words_to_ixs[word])

    print 'Input: %s words, %s chars' % (len(words), len(''.join(words)))
    print 'dictionary (%s items): %s\t...%s' % (
        len(ixs_to_words),
        str(ixs_to_words)[:200], str(ixs_to_words)[-100:]
    )
    print 'ciphertext (%s items): %s' % (len(cipher), str(cipher)[:100])
    return ixs_to_words, cipher

def decode(ixs_to_words, cipher):
    decoded = []
    for k in cipher:
        if isinstance(k, int):
            decoded.append(ixs_to_words[k])
        else:
            decoded.append(k)
    return decoded

def encode_file(path1, path2,
        word_re=r"(?:\w+(?:[':-]\w+)? ?)|(?:\r|\n)+|. +|."):
    #words = open(path1).read().split()
    words = re.findall(word_re, open(path1).read())
    encoded = encode(words)
    with open(path2, 'w') as f:
        cPickle.dump(encoded, f, cPickle.HIGHEST_PROTOCOL)

def decode_file(path1, path2):
    with open(path1) as f:
        ixs_to_words, cipher = cPickle.load(f)
    words = decode(ixs_to_words, cipher)
    with open(path2, 'w') as f:
        f.write(''.join(words))


if __name__ == '__main__':
    if sys.argv[1] == 'encode':
        encode_file(sys.argv[2], sys.argv[3])
    else:
        decode_file(sys.argv[2], sys.argv[3])


