import collections

input_file = open("lorem.txt", 'r')

words = input_file.read().split(" ")

frequencies = collections.defaultdict(int)

for word in words:
    frequencies[word] += 1

high_frequencies = {}

for word in frequencies:
    if frequencies[word] > 5:
        high_frequencies[word] = frequencies[word]

sorted_frequencies = sorted(high_frequencies, key=high_frequencies.get, reverse=True)

print sorted_frequencies
