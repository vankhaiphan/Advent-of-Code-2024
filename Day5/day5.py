import sys
import re
from collections import defaultdict, Counter, deque

inFile = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
data = open(inFile).read().strip()

rules, queries = data.split('\n\n')
lines = rules.split('\n')

before = defaultdict(set)
after = defaultdict(set)

totalMid = 0
totalCorMid = 0

for line in lines:
    x, y = line.split('|')
    x, y = int(x), int(y)
    before[y].add(x)
    after[x].add(y)

for query in queries.split('\n'):
    update = [int(i) for i in query.split(',')]
    isOrdered = True
    for i, x in enumerate(update):
        for j, y in enumerate(update):
            if (i < j and y in before[x]):
                isOrdered = False
    if isOrdered:
        totalMid += update[len(update) // 2]
    else:
        ordered = []
        queue = deque([])
        num = {v: len(before[v] & set(update)) for v in update}
        for v in update:
            if num[v] == 0:
                queue.append(v)
        while queue:
            x = queue.popleft()
            ordered.append(x)
            for y in after[x]:
                if y in num:
                    num[y] -= 1
                    if num[y] == 0:
                        queue.append(y)
        totalCorMid += ordered[len(ordered) // 2]
print(totalMid)
print(totalCorMid)