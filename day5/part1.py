import sys

import common

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} file")


ids = list()
with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.strip()
        ids.append(common.seatid(line))

print(max(ids))

#just continue part2 here...

min_ = min(ids)
max_ = max(ids)

for i in range(min_, max_+1):
    if \
            i not in ids and\
            i+1 in ids and\
            i-1 in ids:
                print(i)
