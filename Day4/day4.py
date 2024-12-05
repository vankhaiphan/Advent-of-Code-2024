import sys
import re
from collections import defaultdict, Counter

inFile = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
data = open(inFile).read().strip()

matrix = data.split('\n')
row = len(matrix)
col = len(matrix[0])

total = 0
new_total = 0

for r in range(row):
    for c in range(col):
        if c + 3 < col and matrix[r][c] == 'X' and matrix[r][c + 1] == 'M' and matrix[r][c + 2] == 'A' and matrix[r][c + 3] == 'S':
            total += 1
        if r + 3 < row and matrix[r][c] == 'X' and matrix[r + 1][c] == 'M' and matrix[r + 2][c] == 'A' and matrix[r + 3][c] == 'S':
            total += 1
        if c + 3 < col and r + 3 < row and matrix[r][c] == 'X' and matrix[r + 1][c + 1] == 'M' and matrix[r + 2][c + 2] == 'A' and matrix[r + 3][c + 3] == 'S':
            total += 1
        if c + 3 < col and matrix[r][c] == 'S' and matrix[r][c + 1] == 'A' and matrix[r][c + 2] == 'M' and matrix[r][c + 3] == 'X':
            total += 1
        if r + 3 < row and matrix[r][c] == 'S' and matrix[r + 1][c] == 'A' and matrix[r + 2][c] == 'M' and matrix[r + 3][c] == 'X':
            total += 1
        if c + 3 < col and r + 3 < row and matrix[r][c] == 'S' and matrix[r + 1][c + 1] == 'A' and matrix[r + 2][c + 2] == 'M' and matrix[r + 3][c + 3] == 'X':
            total += 1
        if c + 3 < col and r - 3 >= 0 and matrix[r][c] == 'X' and matrix[r - 1][c + 1] == 'M' and matrix[r - 2][c + 2] == 'A' and matrix[r - 3][c + 3] == 'S':
            total += 1
        if c + 3 < col and r - 3 >= 0 and matrix[r][c] == 'S' and matrix[r - 1][c + 1] == 'A' and matrix[r - 2][c + 2] == 'M' and matrix[r - 3][c + 3] == 'X':
            total += 1

        if r + 2 < row and c + 2 < col and matrix[r][c]=='M' and matrix[r+1][c+1]=='A' and matrix[r+2][c+2]=='S' and matrix[r+2][c]=='M' and matrix[r][c+2]=='S':
            new_total += 1
        if r + 2 < row and c + 2 < col and matrix[r][c]=='M' and matrix[r+1][c+1]=='A' and matrix[r+2][c+2]=='S' and matrix[r+2][c]=='S' and matrix[r][c+2]=='M':
            new_total += 1
        if r + 2 < row and c + 2 < col and matrix[r][c]=='S' and matrix[r+1][c+1]=='A' and matrix[r+2][c+2]=='M' and matrix[r+2][c]=='M' and matrix[r][c+2]=='S':
            new_total += 1
        if r + 2 < row and c + 2 < col and matrix[r][c]=='S' and matrix[r+1][c+1]=='A' and matrix[r+2][c+2]=='M' and matrix[r+2][c]=='S' and matrix[r][c+2]=='M':
            new_total += 1
print(total)
print(new_total)