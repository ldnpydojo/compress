import random
import collections
import unittest
import itertools

text = "hello there"

def learn(text):
    list_of_text = text.split()
    predictor = collections.defaultdict(list)

    for word, word2, next_word in zip(list_of_text[:-2], list_of_text[1:-1], list_of_text[2:]):
        predictor[word, word2].append(next_word)
    return predictor

def random_word(predictor, cached=[]):
    if not cached:
        foo = list(itertools.chain(*predictor.values()))
        cached.extend(foo)
    return random.choice(cached)

def compress(n, text):
    #re.sub(text, r'[.,:;]', '')
    list_of_text = text.split()
    return ' '.join(list_of_text[:2] + list_of_text[3::n])

def uncompress(n, predictor, text):
    list_of_text = text.split()
    output_words = []
    output_words.append(list_of_text.pop(0))
    for word in list_of_text:
        output_words.append(word)
        last_word = tuple(output_words[-2:])
        for _ in range(n-1):
            print last_word
            new_word = random.choice(predictor.get(last_word, random_word(predictor)))
            output_words.append(new_word)
            last_word = last_word[1:] + (new_word,)
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

