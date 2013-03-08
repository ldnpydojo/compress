import sys
import collections
import uncompress


# Handle arguments
if '-u' in sys.argv:
    print uncompress.uncompress(open(sys.argv[-1], 'r').read())
    sys.exit(0)

if len(sys.argv) > 2:
    in_file = sys.argv[1]
    out_file = sys.argv[2]
else:
    print "INFILE OUTFILE, -u for uncompress"
    sys.exit()

# Read input file
input_file = open(in_file, 'r')
original = input_file.read()
words_split = original.split(" ")
input_file.close()

# Calc Frequencies
frequencies = collections.defaultdict(int)

for word in words_split:
    frequencies[word] += 1

# Get highest frequencies over len 3 only.
high_frequencies = {}

for word in frequencies:
    if frequencies[word] > 5 and len(word) > 3:
        high_frequencies[word] = frequencies[word]

sorted_frequencies = sorted(high_frequencies, key=high_frequencies.get, reverse=True)
print "Sorted Frequencies:"
print sorted_frequencies

output = original
lookup = []  # Lookup table for frequent words

for i, word in enumerate(sorted_frequencies):
    print word,
    print i,
    lookup.append(word)
    target = ' %s ' % word
    print target
    output = output.replace(target, " $%s " % i)

with open(out_file, 'w') as fh:
    fh.write("|".join(lookup))
    fh.write("\n")
    fh.write(output)

print "Wrote to: %s" % (out_file)
