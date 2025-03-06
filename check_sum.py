import sys

s = 0
for line in sys.stdin:
    if line.strip():
        s += int(line.rsplit(',', maxsplit=1)[-1])

print(s)
