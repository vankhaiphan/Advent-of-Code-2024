import sys
from collections import defaultdict, Counter

inFile = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
data = open(inFile).read().strip()

lines = data.split('\n')

left = []
right = []
distance = 0
similarity = 0
counter = Counter()

for line in lines:
    l, r = line.split()
    l, r = int(l), int(r)
    left.append(l)
    right.append(r)
    counter[r] += 1

left = sorted(left)
right = sorted(right)

for (l, r) in zip(left,right):
    distance += abs(l - r)
print(distance)

for l in left:
    similarity += l*counter.get(l, 0)
print(similarity)


