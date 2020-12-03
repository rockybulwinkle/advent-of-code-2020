import sys
import common

if len(sys.argv) != 4:
    print(f"{sys.argv[0]} mapfile stepx stepy")
    exit(-1)

file = sys.argv[1]
map = common.Map(file)
sled = common.Sled(map)

stepx = int(sys.argv[2])
stepy = int(sys.argv[3])

print(sled.go(0, 0, stepx, stepy))
