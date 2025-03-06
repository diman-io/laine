import sys

s = 0
for line in sys.stdin:
    if line.strip():
        s += int(line.strip()[-1])

print(s)
