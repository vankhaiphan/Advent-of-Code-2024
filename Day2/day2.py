import sys
from collections import defaultdict, Counter

def is_safe(arr):
    inc_or_dec = (arr == sorted(arr) or arr == sorted(arr, reverse=True))
    check = True
    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i+1])
        if not 1 <= diff <= 3:
            check = False 
    return inc_or_dec and check

inFile = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
data = open(inFile).read().strip()

lines = data.split('\n')

reports = 0
new_reports = 0

for line in lines:
    arr = list(map(int, line.split()))
    if is_safe(arr):
        reports += 1
    
    check = False
    for i in range(len(arr)):
        ar = arr[:i] + arr[i + 1:]
        if is_safe(ar):
            check = True
    if check:
        new_reports += 1
print(reports)
print(new_reports)



