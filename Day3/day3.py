import sys
import re
from collections import defaultdict, Counter

inFile = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
data = open(inFile).read().strip()

result = 0
result_enabled = 0
enabled = True

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

for i in range(len(data)):
    if (data[i:].startswith("do()")):
        enabled = True
    if (data[i:].startswith("don't()")):
        enabled = False
    instruction = re.match(pattern, data[i:])
    if instruction is not None:
        num1, num2 = int(instruction.group(1)), int(instruction.group(2))
        result += num1 * num2
        if enabled:
            result_enabled += num1 * num2

print(result)
print(result_enabled)