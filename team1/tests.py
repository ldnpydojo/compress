from compressor import encode, decode

data = [
    ['a', 'b', 'b', 'b'],
    ['bone', 'leg', 'eye', 'head', 'leg', 'leg', 'bone'],
    ['a', 'a', 'a', 'a', 'a']
]

for lst in data:
    assert decode(encode(lst)) == lst


print "ok!"
