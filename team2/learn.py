import random
import collections
import unittest

text = "hello there"

def learn(text):
    list_of_text = text.split()
    predictor = collections.defaultdict(list)

    for word, next_word in zip(list_of_text[:-1], list_of_text[1:]):
        predictor[word].append(next_word)
    return predictor

def compress(n, text):
    #re.sub(text, r'[.,:;]', '')
    list_of_text = text.split()
    return ' '.join(list_of_text[::n])

def uncompress(n, predictor, text):
    list_of_text = text.split()
    output_words = []
    for word in list_of_text:
        output_words.append(word)
        last_word = word
        for _ in range(n-1):
            new_word = random.choice(predictor.get(last_word, ['spam']))
            output_words.append(new_word)
            last_word = new_word
    return ' '.join(output_words)


def normalize(text):
    return "\n".join(text.split())

class Tests(unittest.TestCase):
    def test_compress(self):
        self.assertEquals(compress(2, "hello world goodbye cat"), "hello goodbye")
        self.assertEquals(compress(3, "hello world hello cat goodbye dog"), "hello cat")
        


if __name__ == "__main__":
    text = open("sources/shaks.txt").read()
    n = 2
    p = learn(text)

    source = text[10000:20000]
    compressed = compress(n, source)
    output = uncompress(n, p, compressed)
    with open("output.txt", "w") as fh:
        fh.write(normalize(output))
    with open("source.txt", "w") as fh:
        fh.write(normalize(source))

