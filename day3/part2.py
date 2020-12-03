import sys
import common

map = common.Map('input.txt')
sled = common.Sled(map)
steps = [
            [1,1],
            [3,1],
            [5,1],
            [7,1],
            [1,2]
        ]
product = 1
for stepx, stepy in steps:
    product *= sled.go(0, 0, stepx, stepy)

print (product)
