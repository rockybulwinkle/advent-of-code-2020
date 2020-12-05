import sys

import common

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} file")

passports = common.load_passports(sys.argv[1])

count_p1 = 0
count_p2 = 0
for idx,i in enumerate(passports):
    if i.valid_p1():
        count_p1+=1

    valid = i.valid_p2()
    if valid:
        count_p2+=1
    print(idx, valid, i)
    print()

print(count_p1)
print(count_p2)
    
