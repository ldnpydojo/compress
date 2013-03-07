import collections

input_file = open("lorem.txt", 'r')

words = input_file.read().split(" ")

frequencies = collections.defaultdict(int)

for word in words:
    frequencies[word] += 1


sorted_frequencies = sorted(frequencies, key=frequencies.get, reverse=True)

print sorted_frequencies
