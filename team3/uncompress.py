import re


def uncompress(compressed):
    data = compressed.split("\n", 1)
    hash_table = data[0].split("|")

    words = data[1].split(" ")

    uncompressed = []

    marker_re = re.compile(r'\$(\d+)')

    for word in words:
        match = marker_re.match(word)
        if match:
            key = int(match.group(1))
            if 0 <= key < len(hash_table):
                uncompressed.append(hash_table[key])
            else:
                uncompressed.append(word)
        else:
            uncompressed.append(word)

    return " ".join(uncompressed)





